from sqlc.account import Querier, CreateAccountParams

class Account(Querier):
    def __init__(self, connection,
    id=None,
    full_name=None,
    email=None,
    password=None
   ):
        super().__init__(connection)
        self.id = id
        self.full_name = full_name
        self.email = email
        self.password = password

    def setAccountData(self, id=None, full_name=None, email=None, password=None):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.password = password
       
    def createAccount(self):
        arg = CreateAccountParams(
            self.full_name,
            self.email,
            self.password
        )

        cursorResult = self.create_account(arg=arg)
        result = cursorResult.lastrowid
        self._conn.commit()

        return result
    
    def getAccount(self, id):
        cursorResult = self.get_account(id=id)
        result = cursorResult.fetchone()
        return result
    
    def getAccountByEmail(self, email):
        cursorResult = self.get_account_by_email(email=email)
        result = cursorResult.fetchone()

        return result
    

        
