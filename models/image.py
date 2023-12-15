from sqlc.image import Querier, CreateImageParams
from utils import findOut

class Image(Querier):
    def __init__(self, connection,
    id=None,
    host_id=None,
    image_bytes=None
    ):
        super().__init__(connection)
        self.id = id
        self.host_id = host_id
        self.image_bytes = image_bytes

    def setImageData(self, host_id=None, image_bytes=None):
        self.host_id = host_id
        self.image_bytes = image_bytes
       
    def createImage(self):
        arg = CreateImageParams(
            host_id = self.host_id,
            image_bytes = self.image_bytes
        )

        cursorResult = self.create_image(arg=arg)
        self._conn.commit()

        return cursorResult
    
    def getHostImage(self, hostId):
        cursorResult = self.get_image(host_id=hostId)
        result = cursorResult.fetchone()
        return result
    
    def getListHostImage(self, listHostId):
        cursorResult = self.get_list_image(host_id=listHostId)
        result = cursorResult.fetchall()
        return result
    
    def deleteImage(self, host_id):
        self.delete_image(host_id=host_id)
        self._conn.commit()
    

        
