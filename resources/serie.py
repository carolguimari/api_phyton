from json import dumps, loads
from flask_restful import Resource, Api, reqparse, request
from model.serie import SerieModel


class Serie(Resource):
    def get(self, id_serie=None):
        if id_serie:
            found_serie = SerieModel.find_serie(id_serie)
            if found_serie:
                return found_serie.to_dict()
            return {"message": "Serie not found"}, 404

        elif len(request.args) == 0:
            return SerieModel.list_to_dict()

        else:
            return SerieModel.list_to_dict(arguments_request=request.args)

    def post(self):
        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("title")
        body_arguments.add_argument("poster_url")
        body_arguments.add_argument("rate")
        body_arguments.add_argument("synopsis")
        body_arguments.add_argument("main_cast", action='append')

        params = body_arguments.parse_args()
        new_serie = SerieModel(
            params["title"],
            params["poster_url"],
            params["rate"],
            params["synopsis"],
            params["main_cast"]
        )
        SerieModel.add_serie(new_serie)
        return new_serie.to_dict()

    def delete(self, id_serie):
        found_serie = SerieModel.find_serie(id_serie)
        if found_serie:
            SerieModel.remove_serie(found_serie)
            return found_serie.to_dict()
        return {"message": "Serie not found"}, 404

    def put(self, id_serie):
        found_serie = SerieModel.find_serie(id_serie)
        if found_serie:
            body_arguments = reqparse.RequestParser()
            body_arguments.add_argument("title")
            params = body_arguments.parse_args()
            found_serie.title = params["title"]
            return found_serie.to_dict()
        return {"message": "Serie not found"}, 404

    def get_all_series():
        return

    def get_serie_by_id(id_serie):
        found_serie = SerieModel.find_serie(id_serie)
        if found_serie:
            return found_serie.to_dict()
        return {"message": "Serie not found"}, 404
