from flask_restful import Resource
from webargs.flaskparser import use_args

from backendAPI import utils, args, auth
from backendAPI.constants import misc_webargs


class Login(Resource):
    @use_args(args.argsGetUsers)
    def post(self, args):
        pass

