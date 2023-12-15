from flask import render_template, send_file, session, redirect, url_for, request
from models.host import Host
from models.image import Image
import os
from werkzeug.utils import secure_filename   
from utils import findOut
from PIL import Image as PILImage
import io
import ast

# from utils import findOut

class HostController():
    def __init__(self, connection, config):
        self.host = Host(connection=connection)
        self.config = config
        self.connection = connection

    def homePage(self):
        if self.config.session_is_logged_in not in session:
            return redirect( url_for("blueprint.loginPage") )
        else:
            hosts = self.host.listHost()
            listHostId = []
            listOwnerId = []
            for host in hosts :
                listHostId.append(host[0])
                listOwnerId.append(host[1])

            return render_template('home.html', hosts=hosts, listHostId=listHostId, listOwnerId=listOwnerId)
        
    def detailHostPage(self):
        if self.config.session_is_logged_in not in session:
            return redirect( url_for("blueprint.loginPage") )
        else:
            hostId = request.args["hostId"]
            print(hostId)
            hostDetail = self.host.getHost(id=hostId)

            facilities = ast.literal_eval(hostDetail[6])
            
            return render_template('detail.html', hostDetail=hostDetail, facilities=facilities)



        
    def myHostPage(self):
        if self.config.session_is_logged_in not in session:
            return redirect( url_for("blueprint.loginPage") )
        else:
            hosts = self.host.listHostByOwner(ownerId=session[self.config.session_user_id])
            listHostId = []
            for host in hosts :
                listHostId.append(host[0])

            

            return render_template('my_host.html', hosts=hosts, listHostId=listHostId)
        
    def ownerDetailHostPage(self):
        if self.config.session_is_logged_in not in session:
            return redirect( url_for("blueprint.loginPage") )
        else:
            if request.method == "POST" :
                holderId = request.form["hostId"]
                hostId = request.form["holderId"]
                validAt = request.form["checkIn"]
                expiredAt = request.form["checkOut"]
                # price = request.form["title

                print(f"holderId {holderId}")
                print(hostId)
                print(validAt)
                print(expiredAt)

                # self.ticket.setTicketData(
                #     holder_id = holderId ,
                #     host_id = hostId ,
                #     valid_at = validAt ,
                #     expired_at = expiredAt ,
                #     is_finish = False ,
                #     # price = price
                # )
            else :
                hostId = request.args["hostId"]
                hostDetail = self.host.getHost(id=hostId)

                facilities = ast.literal_eval(hostDetail[6])

                return render_template('owner_detail_host.html', hostDetail=hostDetail, facilities=facilities)
        

    def addHostPage(self):
        if self.config.session_is_logged_in not in session:
            return redirect( url_for("blueprint.loginPage") )
        else:
            if request.method == "POST":
                title = request.form["title"]
                description = request.form["description"]
                location = request.form["address"]
                placeType = request.form["placeType"]
                facilities = request.form.getlist("facilities")
                price = request.form["price"]
                imageFile = request.files['file']

                print(facilities)


                self.host.setHostData(session[self.config.session_user_id], title, description, placeType, location, f"{facilities}", price)
                lastInsertId = self.host.createHost()

                if lastInsertId :
                    filename = secure_filename(imageFile.filename)
                    imageFile.save(os.path.join(self.config.temp_image_processor_path, filename))

                    image = PILImage.open(f"{self.config.temp_image_processor_path}/{filename}")


                    x, y = image.size
                    image = image.resize((int(x/10),int(y/10)))


                    image.save(f"{self.config.temp_image_processor_path}/{filename}",optimize = True,  quality = 95)

                    with open(f"{self.config.temp_image_processor_path}/{filename}", "rb") as imageBufferedReader:
                        imageRawBinary = imageBufferedReader.read()
                        Image(connection=self.connection, host_id=lastInsertId, image_bytes=imageRawBinary).createImage()

                    os.remove(f"{self.config.temp_image_processor_path}/{filename}")

                return redirect(url_for("blueprint.myHostPage"))
            else:
                return render_template("create_a_host.html")
        
        
    def deleteHost(self):
        if self.config.session_is_logged_in not in session:
            return redirect( url_for("blueprint.loginPage") )
        else:
            hostId = request.args['hostId']
            Image(connection=self.connection).deleteImage(host_id=hostId)
            self.host.deleteHost(id=hostId)

            return redirect(url_for("blueprint.myHostPage"))
    
    def updateHost(self):
        if self.config.session_is_logged_in not in session:
            return redirect( url_for("blueprint.loginPage") )
        else:
            if request.method == "POST":
                hostId = request.form["hostId"]
                title = request.form["title"]
                description = request.form["description"]
                location = request.form["address"]
                placeType = request.form["placeType"]
                facilities = request.form.getlist("facilities")
                price = request.form["price"]


                self.host.updateHost(hostId=hostId, title=title, description=description, location=location, type=placeType, facilities=f"{facilities}", price=price)

                return redirect(url_for("blueprint.myHostPage"))
            else:
                hostId = request.args['hostId']
                title = request.args['title']
                desc = request.args['desc']
                address = request.args['address']
                price = request.args['price']

                return render_template("update_a_host.html", hostId=hostId, title=title, desc=desc, address=address, price=price)
            