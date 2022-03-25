import sqlite3

class MyDatabase:
    def __init__(self) -> None:
        self._db_connection = sqlite3.connect("social_personal_imdb.db", check_same_thread=False)
        self._cursor = self._db_connection.cursor()

        create_media_table = "CREATE TABLE IF NOT EXISTS media ( \
            id_media text PRIMARY KEY, \
            title text, \
            poster_url text, \
            rate text, \
            synopsis text, \
            main_cast text \
        )"

        self._cursor.execute(create_media_table)
        self._db_connection.commit()

    def create_media(self, media):
        create_media_SQL = "INSERT INTO media VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(media.id_media, media.title, media.poster_url, media.rate, media.synopsis, media.main_cast)

        self._cursor.execute(create_media_SQL)
        self._db_connection.commit()

    def list_medias(self):
        list_medias_SQL = "SELECT * from media;"
        return self._cursor.execute(list_medias_SQL).fetchall()

    def delete_media(self, media):
        delete_media_SQL = "DELETE FROM media WHERE id_media='{}'".format(media.id_media)
        self._cursor.execute(delete_media_SQL)
        self._db_connection.commit()

    def find_media(self, id_media):
        select_media_SQL = "SELECT * FROM media WHERE id_media='{}'".format(id_media)
        return self._cursor.execute(select_media_SQL).fetchone()

    def edit_media(self, media):
        edit_media_SQL = "UPDATE media SET content='{}' WHERE id_media='{}'".format(media.content, media.id_media)
        self._cursor.execute(edit_media_SQL)
        self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()
        