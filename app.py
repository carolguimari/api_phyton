from flask import Flask
from flask_restful import Api
from resources.film import Film
from resources.serie import Serie

app = Flask(__name__)
api = Api(app)

api.add_resource(Film,
                 "/films/<int:id_film>",
                 "/films")

api.add_resource(Serie, "/series/<int:id_serie>",
                 "/series",
                 "/series/author/<string:author>",
                 "/series/titulo/<string:author>")

if __name__ == '__main__':
    app.run(debug=True)
