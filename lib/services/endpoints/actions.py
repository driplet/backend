from flask import request
from flask_restful import Resource

from lib.accounts import authentication as auth

import en_us
import utils

import json


from zeroless import (Server)
pub = Server(port=35893).pub()


class start(Resource):
    @classmethod
    def post(self, client_id, service_id):
        request_token = request.headers.get('authorization')
        auth_status = auth.verify(client_id, request_token)
        if auth_status != 200:
            return auth_status

        service = utils.get_service(client_id, service_id)
        if service.count() == 0:
            return en_us.NOT_FOUND

        command = {
            "serviceid": service_id,
            "content": utils.encoder(service)[0]['start_command']
        }
        command = json.dumps(command)
        pub(command.encode('utf-8'))
        return "", 204


class stop(Resource):
    @classmethod
    def post(self, client_id, service_id):
        request_token = request.headers.get('authorization')
        auth_status = auth.verify(client_id, request_token)
        if auth_status != 200:
            return auth_status

        service = utils.get_service(client_id, service_id)
        if service.count() == 0:
            return en_us.NOT_FOUND

        command = {
            "serviceid": service_id,
            "content": utils.encoder(service)[0]['stop_command']
        }
        command = json.dumps(command)
        pub(command.encode('utf-8'))
        return "", 204


class restart(Resource):
    @classmethod
    def post(self, client_id, service_id):
        request_token = request.headers.get('authorization')
        auth_status = auth.verify(client_id, request_token)
        if auth_status != 200:
            return auth_status

        service = utils.get_service(client_id, service_id)
        if service.count() == 0:
            return en_us.NOT_FOUND

        command = {
            "serviceid": service_id,
            "content": utils.encoder(service)[0]['restart_command']
        }
        command = json.dumps(command)
        pub(command.encode('utf-8'))
        return "", 204
