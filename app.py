import logging
import os

from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from lagom import Singleton, Container
from lagom.integrations.flask import FlaskIntegration

# from Connector.Database import Database
from Controller.testController import test_controller
from Service.StartupService import StartupService
from container import container

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


app = Flask(__name__)

app_with_deps = FlaskIntegration(app, container)
app.register_blueprint(test_controller)

# Run the app
if __name__ == '__main__':
    startup_service = container[StartupService]
    startup_service.load_configuration()
    app.run()