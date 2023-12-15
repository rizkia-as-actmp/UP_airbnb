from sqlc.ticket import Querier, CreateTicketParams
from utils import findOut

class Ticket(Querier):
    def __init__(self, connection,
    id=None,
    holder_id = None,
    host_id = None,
    valid_at = None,
    expired_at = None,
    is_finish = None,
    price = None
    ):
        super().__init__(connection)
        self.__id = id
        self.holder_id = holder_id
        self.host_id = host_id
        self.valid_at = valid_at
        self.expired_at = expired_at
        self.is_finish = is_finish
        self.price = price

    def setTicketData(self, holder_id, host_id, valid_at, expired_at, is_finish, price):
        self.holder_id = holder_id
        self.host_id = host_id
        self.valid_at = valid_at
        self.expired_at = expired_at
        self.is_finish = is_finish
        self.price = price
    
    def createTicket(self):
        arg = CreateTicketParams(
            holder_id = self.holder_id, 
            host_id = self.host_id, 
            valid_at = self.valid_at, 
            expired_at = self.expired_at, 
            is_finish = self.is_finish, 
            price = self.price
            )

        cursorResult = self._create_ticket(arg)
        self._conn.commit()
        return cursorResult

    def getListTicket(self, holderId):
        cursorResult = self._get_list_ticket(holder_id=holderId)
        result = cursorResult.fetchall()
        return result