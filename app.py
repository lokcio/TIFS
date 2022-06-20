import logging
import os
from dotenv import load_dotenv

# specjalnie to tu jest
load_dotenv()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from lagom.integrations.flask import FlaskIntegration
from container import container

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('POSTGRESQL_USERNAME')}:" \
                                        f"{os.getenv('POSTGRESQL_PASSWORD')}" \
                                        f"@{os.getenv('POSTGRESQL_ADDRESS')}:" \
                                        f"{os.getenv('POSTGRESQL_PORT')}/" \
                                        f"{os.getenv('POSTGRESQL_DATABASE')}"
db = SQLAlchemy(app)
container[SQLAlchemy] = db
app_with_deps = FlaskIntegration(app, container)

# Run the app
if __name__ == '__main__':
    from Service.StartupService import StartupService
    from Service.TaskRunnerService import TaskRunnerService
    from Controller.fileController import file_controller

    app.register_blueprint(file_controller)
    startup_service = container[StartupService]
    startup_service.prepare_database()
    startup_service.load_configuration()
    task_runner_service = container[TaskRunnerService]
    task_runner_service.start_tasks()

    app.run()
