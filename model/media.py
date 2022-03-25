import time
from json import dumps, loads
from services.database import MyDatabase

class MediaModel:
    database_service: MyDatabase = None

    def __init__(self, title, rate, synopsis, poster_url, main_cast, id_media=None) -> None:
        if id_media:
            self.id_media = id_media
        else:    
            self.id_media = round(time.time() * 1000)

        self.title = title
        self.rate = rate
        self.synopsis = synopsis
        self.poster_url = poster_url
        self.main_cast = main_cast

    @classmethod
    def find_media(cls, id_media):
        found_media = None
        result = cls.database_service.find_media(id_media)
        if result:
            found_media = MediaModel(result[1], result[2], result[3], result[4], result[5], result[0])
        return found_media

    @classmethod
    def add_media(cls, media):
        cls.database_service.create_media(media)

    @classmethod
    def list_films(cls):
        return cls._films_list


    @classmethod
    def remove_media(cls, media):
        cls._database_service.delete_media(media)

    @classmethod
    def list_to_dict(cls, arguments_request=[]):
        arguments_accepted = ["title", "actor"]
        exist_argument_valid = any(item in arguments_request for item in arguments_accepted)

        if len(arguments_request) == 0:
            return loads(dumps(cls._medias_list, default=MediaModel.to_dict))

        elif exist_argument_valid:
            found_media = dict()
            for media in cls._medias_list:

                if ("title" in arguments_request) and (arguments_request["title"] in media.title):
                    found_media[media.id_media] = media

            return loads(dumps(found_media, default=MediaModel.to_dict))

        else:
            return {"erro": "incorrect parameter"}, 400

    def to_dict(self):
        return {
            "id_media": self.id_media,
            "title": self.title,
            "rate": self.rate,
            "synopsis": self.synopsis,
            "poster_url": self.poster_url,
            "main_cast": loads(dumps(self.main_cast))
        }
