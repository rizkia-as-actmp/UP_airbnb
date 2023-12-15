from sqlc.pp import Querier, CreatePPParams

class ProfilePicture(Querier):
    def __init__(self, connection,
    id=None,
    account_id=None,
    image_bytes=None
    ):
        super().__init__(connection)
        self.__id = id
        self.account_id = account_id
        self.image_bytes = image_bytes

    def setProfilePictureData(self, account_id, image_bytes):
        self.account_id = account_id
        self.image_bytes = image_bytes
       
    def createProfilePicture(self):
        arg = CreatePPParams(
            account_id  = self.account_id,
            image_bytes = self.image_bytes
        )

        result = self.create_pp(arg=arg)
        self._conn.commit()

        return result
    
    def getProfilePicture(self, accountId):
        cursorResult = self.get_pp(account_id=accountId)
        result = cursorResult.fetchone()
        return result
    
    def deleteProfilePicture(self, accountId):
        return self.delete_pp(account_id=accountId)
    

        
