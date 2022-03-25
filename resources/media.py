from json import dumps, loads
from flask import Flask
from flask_restful import Resource, Api, reqparse, request
from model.media import MediaModel


class Media(Resource):
    def get(self, id_media=None):
        if id_media:
            found_media = MediaModel.find_media(id_media)
            if found_media:
                return found_media.to_dict()
            return {"message": "Media not found"}, 404

        elif len(request.args) == 0:
            return MediaModel.list_to_dict()

        else:
            return MediaModel.list_to_dict(arguments_request=request.args)

    def post(self):
        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("title")
        body_arguments.add_argument("poster_url")
        body_arguments.add_argument("rate")
        body_arguments.add_argument("synopsis")
        body_arguments.add_argument("main_cast")

        params = body_arguments.parse_args()
        new_media = MediaModel(
            params["title"],
            params["poster_url"],
            params["rate"],
            params["synopsis"],
            params["main_cast"]
        )

        MediaModel.add_media(new_media)
        return new_media.to_dict()

    def delete(self, id_media):
        found_media = MediaModel.find_media(id_media)
        if found_media:
            MediaModel.remove_media(found_media)
            return found_media.to_dict()
        return {"message": "Media not found"}, 404

    def put(self, id_media):
        found_media = MediaModel.find_media(id_media)
        if found_media:
            body_arguments = reqparse.RequestParser()
            body_arguments.add_argument("title")
            params = body_arguments.parse_args()
            found_media.title = params["title"]
            return found_media.to_dict()
        return {"message": "Media not found"}, 404


    def get_media_by_id(id_media):
        found_media = MediaModel.find_media(id_media)
        if found_media:
            return found_media.to_dict()
        return {"message": "Media not found"}, 404
