from flask import Flask
from flask_restful import Api
from webargs.flaskparser import parser, abort

from backendAPI import db
from backendAPI import routes

app = Flask(__name__)

db.init_app(app)
api = Api(app)


# This error handler is necessary for usage with Flask-RESTful
@parser.error_handler
def handle_request_parsing_error(err, req, schema, error_status_code, error_headers):
    abort(error_status_code, errors=err.messages)

api.add_resource(routes.OperateUsers, '/api/users/')
api.add_resource(routes.OperateUsersId, '/api/users/<id>')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
