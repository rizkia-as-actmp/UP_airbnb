from flask import render_template, request, redirect, url_for, session,jsonify
from models.account import Account
from utils import findOut

class AccountController():
    def __init__(self, connection, config):
        self.account = Account(connection=connection)
        self.config = config
        
    def registerPage(self):
        if request.method == "POST":
            fullName = request.form["full-name"]
            email = request.form["email"]
            password = request.form["password"]

            print(password)

            self.account.setAccountData(full_name=fullName, email=email, password=password)
            lastId = self.account.createAccount()

            return redirect(url_for("blueprint.addProfilePicture", accountId=lastId))
        
        else:
            return render_template("register.html")
        

    def loginPage(self):
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]

            accountFromDB = self.account.getAccountByEmail(email=email)

            if accountFromDB[2] == email and accountFromDB[3] == password :
                session[self.config.session_is_logged_in] = True
                session[self.config.session_user_id] = accountFromDB[0]
                session[self.config.session_user_fullname] = accountFromDB[1]
                session[self.config.session_user_email] = accountFromDB[2]

            findOut(accountFromDB)

            return redirect(url_for("blueprint.homePage"))
        
        else:
            return render_template("login.html")
        
    def getAccount(self):
        ownerId = request.args["ownerId"]
        account = self.account.getAccount(id=ownerId)

        user_dict = {
            'fullname': account[1],
        }

        return jsonify(user_dict)
        
    def logout(self):
        session.pop(self.config.session_is_logged_in, None)
        session.pop(self.config.session_user_id, None)
        session.pop(self.config.session_user_fullname, None)
        session.pop(self.config.session_user_email, None)

        return redirect(url_for("blueprint.loginPage"))
            