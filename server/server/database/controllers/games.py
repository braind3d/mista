from server.database.database import Database


class Games:
    def __init__(self, id, name, description, reviews, release_data, developer, publisher, genre, minimum_requirements, recommended_requirements, price):
        self.id = id
        self.name = name
        self.description = description
        self.reviews = reviews
        self.release_data = release_data
        self.developer = developer
        self.publisher = publisher
        self.genre = genre
        self.minimum_requirements = minimum_requirements
        self.recommended_requirements = recommended_requirements
        self.price = price

    def save(self):
        with Database() as db:
            db.execute(
                '''
                INSERT INTO post
                VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    self.title,
                    self.id,
                    self.name,
                    self.description,
                    self.reviews,
                    self.release_data,
                    self.developer,
                    self.publisher,
                    self.genre,
                    self.minimum_requirements,
                    self.recommended_requirements,
                    self.price))
            return self

    @staticmethod
    def all(page_number, page_size, search_query=None):
        with Database() as db:
            if not search_query:
                rows = db.execute('SELECT * FROM games LIMIT {} OFFSET {}'.format(
                        page_size,
                        page_size*(page_number - 1))).fetchall()
                return [Games(*row) for row in rows]

            rows = db.execute('SELECT * FROM games WHERE instr(name, "{}") > 0 LIMIT {} OFFSET {}'.format(
                    search_query,
                    page_size,
                    page_size*(page_number - 1))).fetchall()

            return [Games(*row) for row in rows]

    @staticmethod
    def get(id):
        with Database() as db:
            rows = db.execute('SELECT * FROM games WHERE id = {}'.format(id)).fetchall()
            return [Games(*row) for row in rows][0]
