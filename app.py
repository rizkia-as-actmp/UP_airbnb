# # Importing the necessary modules and libraries
# from flask import Flask
# from flask_cors import CORS
# from sqlalchemy import create_engine
# from routes.blueprint import newBlueprint
# from controllers.controller import Controller
# from config import loadConfig

# config = loadConfig(".", "json")

# app = Flask(__name__, template_folder=config.flask_templates_directory) 
# CORS(app)

# app.secret_key = config.app_secret_key

# engine = create_engine(config.db_url)

# conn = engine.connect()

# controller = Controller(connection=conn, config=config)

# bp = newBlueprint(controller)

# app.register_blueprint(bp)


# if __name__ == '__main__': 
#     app.run()


# =======================================================================================

from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from routes.blueprint import newBlueprint
from controllers.controller import Controller
from config import loadConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

config = loadConfig(".", "json")

app = Flask(__name__, template_folder=config.flask_templates_directory) 
CORS(app)
app.secret_key = config.app_secret_key

engine = create_engine(config.db_url)
Session = sessionmaker(bind=engine)

session = Session()
conn = engine.connect()
try:
    controller = Controller(connection=conn, config=config)

    bp = newBlueprint(controller)

    app.register_blueprint(bp)

    session.commit()
except Exception as e:
    # Rollback the transaction in case of an exception
    session.rollback()
    raise  # Re-raise the exception to propagate it further

finally:
    # Close the session
    session.close()


if __name__ == '__main__': 
    app.run()



