from flask_restful import Resource
from webargs.flaskparser import use_args

from backendAPI import args


class OperateUsers(Resource):

    @use_args(args.argsGetUsers)
    def get(self, args):
        print("get")
        pass

    @use_args(args.argsPostUsers)
    def post(self, args):
        print("post")
        pass

class OperateUsersId(Resource):

    def get(self, id):
        print(id)
        pass

    def put(self, args, id):
        pass

    def delete(self, args, id):
        pass
