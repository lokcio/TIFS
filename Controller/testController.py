from flask import Blueprint
from lagom import injectable
from lagom.experimental.integrations.flask import FlaskBlueprintIntegration

# from Connector.Database import Database
# from app import container
from Model.Task import Task
from Service.BasicAnalyzeService import BasicAnalyzeService
from container import container

test_controller = Blueprint('test_controller', __name__)
test_controller_with_deps = FlaskBlueprintIntegration(test_controller, container)



@test_controller_with_deps.route("/save_it/<string:thing_to_save>", methods=['GET'])
def save_to_db(thing_to_save, basic_service: BasicAnalyzeService = injectable):
    basic_service.process_task(Task())
    return 'saved'