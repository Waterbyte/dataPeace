from flask import jsonify
from flask import make_response


def generate_custom_response(result, code):
    return make_response(jsonify(result), code)
