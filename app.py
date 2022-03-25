from flask import Flask
from flask_restful import Api
from resources.media import Media
from services.database import MyDatabase
from model.media import MediaModel

app = Flask(__name__)
api = Api(app)
database = MyDatabase()
MediaModel.database_service = database

api.add_resource(Media,
                 "/medias/<int:id_media>",
                 "/medias")

if __name__ == '__main__':
    app.run(debug=True)
