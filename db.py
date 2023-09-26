import sqlite3

from reviews_processing import Review


def create_reviews_table() -> None:
    with sqlite3.connect("database.sqlite3") as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Reviews ("
                       "id INTEGER PRIMARY KEY,"
                       "machine TEXT NOT NULL,"
                       "reviews JSON NOT NULL)")


def insert_reviews(reviews: dict[str, list[Review]]) -> None:
    with sqlite3.connect("database.sqlite3") as connection:
        cursor = connection.cursor()
        for machine_name, machine_reviews in reviews.items():
            cursor.execute(f'INSERT OR IGNORE INTO Reviews (machine, reviews) '
                           f'VALUES ("{machine_name}", "{machine_reviews}")')


if __name__ == "__main__":
    create_reviews_table()
