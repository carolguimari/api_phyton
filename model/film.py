import time
from json import dumps, loads


class FilmModel:
    _films_list = list()

    def __init__(self, title: str, rate: int, synopsis: str, poster_url: str, main_cast: list) -> None:
        self.id_film = round(time.time() * 1000)
        self.title = title
        self.rate = rate
        self.synopsis = synopsis
        self.poster_url = poster_url
        self.main_cast = main_cast

    @classmethod
    def add_film(cls, film):
        cls._films_list.append(film)

    @classmethod
    def list_films(cls):
        return cls._films_list

    @classmethod
    def find_film(cls, id_film):
        found_film = None
        for film in cls._films_list:
            if film.id_film == id_film:
                found_film = film
                break
        return found_film

    @classmethod
    def remove_film(cls, film):
        cls._films_list.remove(film)

    @classmethod
    def list_to_dict(cls, arguments_request=[]):
        arguments_accepted = ["title", "actor"]
        if len(arguments_request) == 0:
            return loads(dumps(cls._films_list, default=FilmModel.to_dict))

        elif any(item in arguments_request for item in arguments_accepted):
            found_film = dict()
            for film in cls._films_list:

                if ("title" in arguments_request) and (arguments_request["title"] in film.title):
                    found_film[film.id_film] = film

            return loads(dumps(found_film, default=FilmModel.to_dict))

        else:
            return {"erro": "incorrect parameter"}, 404

    def to_dict(self):
        return {
            "id_film": self.id_film,
            "title": self.title,
            "rate": self.rate,
            "synopsis": self.synopsis,
            "poster_url": self.poster_url,
            "main_cast": loads(dumps(self.main_cast))
        }
