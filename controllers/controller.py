from .host_ctrl import HostController
from .account_ctrl import AccountController
from .profilepic_ctrl import ProfilePictureController
from .image_ctrl import ImageController
from .ticket_ctrl import TicketController

class Controller:
    def __init__(self, connection, config):
        self.config = config
        self.connection = connection
        self.host = HostController(connection=connection, config=config)
        self.account = AccountController(connection=connection, config=config)
        self.profilePicture = ProfilePictureController(connection=connection, config=config)
        self.image = ImageController(connection=connection, config=config)
        self.ticket = TicketController(connection=connection, config=config)
        