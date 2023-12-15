from flask import Blueprint

def newBlueprint(controller) :
    blueprint = Blueprint('blueprint', __name__)

    hostController = controller.host
    blueprint.route('/', methods=['GET'])(hostController.homePage)
    blueprint.route('/my-host', methods=['GET'])(hostController.myHostPage)
    blueprint.route('/add-a-host', methods=['GET', 'POST'])(hostController.addHostPage)
    blueprint.route('/detail-host', methods=['GET', 'POST'])(hostController.detailHostPage)
    blueprint.route('/owner-detail-host', methods=['GET'])(hostController.ownerDetailHostPage)
    blueprint.route('/delete-host', methods=['GET'])(hostController.deleteHost)
    blueprint.route('/update-host', methods=['GET','POST'])(hostController.updateHost)

    accountController = controller.account
    blueprint.route('/login', methods=['GET', 'POST'])(accountController.loginPage)
    blueprint.route('/register', methods=['GET', 'POST'])(accountController.registerPage)
    blueprint.route('/logout', methods=['GET'])(accountController.logout)
    blueprint.route('/account', methods=['GET'])(accountController.getAccount)

    profilePictureController = controller.profilePicture
    blueprint.route('/add-profile-picture', methods=['GET', 'POST'])(profilePictureController.addProfilePicture)
    blueprint.route('/profile-picture', methods=['GET'])(profilePictureController.getProfilePicture)

    imageController = controller.image
    blueprint.route('/host-image', methods=['GET'])(imageController.getHostImage)
    # blueprint.route('/list-host-image', methods=['GET'])(imageController.getListHostImage)

    ticketController = controller.ticket
    blueprint.route('/add-ticket', methods=['GET','POST'])(ticketController.addTicket)
    # blueprint.route('/ticket', methods=['GET'])(ticketController.getListTicket)
    blueprint.route('/my-ticket', methods=['GET'])(ticketController.myTicketPage)



    return blueprint