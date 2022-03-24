from json import dumps, loads
from flask import Flask
from flask_restful import Resource, Api, reqparse, request
from model.film import FilmModel


class Film(Resource):
    def get(self, id_film=None):
        if id_film:
            found_film = FilmModel.find_film(id_film)
            if found_film:
                return found_film.to_dict()
            return {"message": "Film not found"}, 404

        elif len(request.args) == 0:
            return FilmModel.list_to_dict()

        else:
            return FilmModel.list_to_dict(arguments_request=request.args)

    def post(self):
        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("title")
        body_arguments.add_argument("poster_url")
        body_arguments.add_argument("rate")
        body_arguments.add_argument("synopsis")
        body_arguments.add_argument("main_cast", action='append')

        params = body_arguments.parse_args()
        new_film = FilmModel(
            params["title"],
            params["poster_url"],
            params["rate"],
            params["synopsis"],
            params["main_cast"]
        )

        FilmModel.add_film(new_film)
        return new_film.to_dict()

    def delete(self, id_film):
        found_film = FilmModel.find_film(id_film)
        if found_film:
            FilmModel.remove_film(found_film)
            return found_film.to_dict()
        return {"message": "Film not found"}, 404

    def put(self, id_film):
        found_film = FilmModel.find_film(id_film)
        if found_film:
            body_arguments = reqparse.RequestParser()
            body_arguments.add_argument("title")
            params = body_arguments.parse_args()
            found_film.title = params["title"]
            return found_film.to_dict()
        return {"message": "Film not found"}, 404

    def get_all_films():
        return

    def get_film_by_id(id_film):
        found_film = FilmModel.find_film(id_film)
        if found_film:
            return found_film.to_dict()
        return {"message": "Film not found"}, 404
