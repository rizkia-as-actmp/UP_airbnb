from flask import request, redirect, url_for, render_template,session
from models.ticket import Ticket
from datetime import datetime

class TicketController():
    def __init__(self, connection, config):
        self.ticket = Ticket(connection=connection)
        self.config = config

    def addTicket(self):
        if self.config.session_is_logged_in not in session:
            return redirect( url_for("blueprint.loginPage") )
        else:
            if request.method == "POST" :
                print(session[self.config.session_user_id])
                hostId = request.form["hostId"]
                holderId = session[self.config.session_user_id]
                validAt = request.form["checkIn"]
                expiredAt = request.form["checkOut"]
                price = request.form["price"]

                date1 = datetime.strptime(validAt, "%Y-%m-%d")
                date2 = datetime.strptime(expiredAt, "%Y-%m-%d")
                duration = date2 - date1

                self.ticket.setTicketData(
                    holder_id = holderId ,
                    host_id = hostId ,
                    valid_at = validAt ,
                    expired_at = expiredAt ,
                    is_finish = False ,
                    price = int(duration.days) * int(price)
                )

                self.ticket.createTicket()

                return redirect(url_for('blueprint.homePage'))
            
            else:
                hostId = request.args["hostId"]
                price = request.args["price"]

                return render_template("add_ticket.html", hostId=hostId , price=price)
        

    def myTicketPage(self):
        tickets = self.ticket.getListTicket(session[self.config.session_user_id])
        return render_template("my_ticket.html", tickets=tickets)
