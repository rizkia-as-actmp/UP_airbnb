from sqlc.host import Querier, CreateHostParams, UpdateHostParams

class Host(Querier):
    def __init__(self, connection, id=None, owner_id=None, title=None, description=None, type=None, location=None, facilities=None, price=None):
        super().__init__(connection)
        self.id = id
        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.type = type
        self.location = location
        self.facilities = facilities
        self.price = price

    def createHost(self):
        arg = CreateHostParams(
            self.owner_id,
            self.title,
            self.description,
            self.type,
            self.location,
            self.facilities,
            self.price
            )
        
        cursorResult = self.create_host(arg=arg)
        result = cursorResult.lastrowid
        self._conn.commit()

        return result
    
    
    
    def setHostData(self, owner_id, title, description, type, location, facilities, price):
        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.type = type
        self.location = location
        self.facilities = facilities
        self.price = price
    
    def getHost(self, id):
        cursorResult = self.get_host(id=id)
        results = cursorResult.fetchone()

        return results
    
    def deleteHost(self, id):
        self.delete_host(id=id)
        self._conn.commit()
    
    def listHost(self):
        cursorResult = self.list_host()
        results = cursorResult.fetchall()

        return results
    
    def listHostByOwner(self, ownerId):
        cursorResult = self.list_host_by_owner(owner_id=ownerId)
        results = cursorResult.fetchall()

        return results
    
    def updateHost(self, hostId, title, description, type, location, facilities, price) :
        arg = UpdateHostParams(
            title,
            description,
            type,
            location,
            facilities,
            price,
            hostId
        )
        
        self.update_host(arg=arg)
        self._conn.commit()