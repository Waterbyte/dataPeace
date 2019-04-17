from flask_restful import Resource
from webargs.flaskparser import use_args

from backendAPI import args, utils, auth


class OperateUsers(Resource):

    @use_args(args.argsGetUsers)
    def get(self, args):
        val = auth.getUsersWithParams(args)
        return utils.generate_custom_response(val, 200)

    @use_args(args.argsPostUsers)
    def post(self, args):
        if auth.createUsers(args):
            return utils.generate_custom_response({}, 201)
        else:
            return utils.generate_custom_response({}, 422)


class OperateUsersId(Resource):

    def get(self, id):
        val = auth.getUser(int(id))
        return utils.generate_custom_response(val, 200)

    @use_args(args.argsUpdateUser)
    def put(self, args, id):
        if auth.modifyUser(args, (int(id))):
            return utils.generate_custom_response({}, 200)
        else:
            return utils.generate_custom_response({}, 422)

    def delete(self, id):
        if auth.deleteUser(int(id)):
            return utils.generate_custom_response({}, 200)
        else:
            return utils.generate_custom_response({}, 422)
