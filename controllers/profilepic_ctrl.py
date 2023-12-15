from flask import render_template, request, redirect, url_for, send_file
from models.profilepic import ProfilePicture
from PIL import Image as PILImage
import io
from werkzeug.utils import secure_filename   
import os

class ProfilePictureController():
    def __init__(self, connection, config):
        self.pp = ProfilePicture(connection=connection)
        self.config = config

    def addProfilePicture(self):
        if request.method == "POST":
            accountId = request.args['accountId']
            pictureFile = request.files["file"]

            filename = secure_filename(pictureFile.filename)
            pictureFile.save(os.path.join(self.config.temp_image_processor_path, filename))

            with open(f"{self.config.temp_image_processor_path}/{filename}", "rb") as imageBufferedReader:
                imageRawBinary = imageBufferedReader.read()
                self.pp.setProfilePictureData(accountId, imageRawBinary)

                result = self.pp.createProfilePicture()


            os.remove(f"./temp-image-processor/{filename}")

            return redirect(url_for("blueprint.homePage"))
        
        else:
            return render_template("add_profile_picture.html")
        
    def getProfilePicture(self):
        accountId = request.args['accountId']
        print(accountId)
        imageRawBinary = self.pp.getProfilePicture(accountId=accountId)[2]


        image = PILImage.open(io.BytesIO(imageRawBinary))
        image.save(f"{self.config.temp_image_processor_path}/send.png")

        return send_file(f"{self.config.temp_image_processor_path}/send.png", mimetype='image/png')