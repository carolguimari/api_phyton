import time
from json import dumps, loads


class SerieModel:
    _series_list = list()

    def __init__(self, title: str, rate: int, synopsis: str, poster_url: str, main_cast: list) -> None:
        self.id_serie = round(time.time() * 1000)
        self.title = title
        self.synopsis = synopsis
        self.rate = rate
        self.poster_url = poster_url
        self.main_cast = main_cast

    @classmethod
    def add_serie(cls, serie):
        cls._series_list.append(serie)

    @classmethod
    def list_series(cls):
        return cls._series_list

    @classmethod
    def find_serie(cls, id_serie):
        found_serie = None
        for serie in cls._series_list:
            if serie.id_serie == id_serie:
                found_serie = serie
                break
        return found_serie

    @classmethod
    def remove_serie(cls, serie):
        cls._series_list.remove(serie)

    @classmethod
    def list_to_dict(cls, arguments_request=[]):
        arguments_accepted = ["title", "actor"]
        if len(arguments_request) == 0:
            return loads(dumps(cls._series_list, default=SerieModel.to_dict))

        elif any(item in arguments_request for item in arguments_accepted):
            found_serie = dict()
            for serie in cls._series_list:

                if ("title" in arguments_request) and (arguments_request["title"] in serie.title):
                    found_serie[serie.id_serie] = serie

            return loads(dumps(found_serie, default=SerieModel.to_dict))

        else:
            return {"erro": "incorrect parameter"}, 404

    def to_dict(self):
        return {
            "id_serie": self.id_serie,
            "title": self.title,
            "rate": self.rate,
            "synopsis": self.synopsis,
            "poster_url": self.poster_url,
            "main_cast": loads(dumps(self.main_cast))
        }
