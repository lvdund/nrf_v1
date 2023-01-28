from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

from Services import *
from Services.NFDiscovery.discovery import *
from Services.NFManagement.management import *

app = Flask(__name__)
api = Api(app)

# swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger_manager.yaml'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint( SWAGGER_URL, API_URL, config={'app_name': 'list api'} )
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix = SWAGGER_URL)

# nf management
api.add_resource(NFInstance_Document, '/nnrf-nfm/v1/nf-instances/<nfInstanceId>')

if __name__ == "__main__":
    app.run()