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

    @staticmethod
    def all(page_number, page_size, search_query=None):
        with Database() as db:
            if not search_query:
                rows = db.execute('''select distinct games.game_id, games.name, games.description, games.all_reviews, games.release_date,developers.developer_name, publishers.publisher_name, genres.genre_name, games.minimum_requirements, games.recommended_requirements, games.original_price 
                    FROM games
                    LEFT JOIN game_developers
                    ON games.game_id = game_developers.game_id 
                    LEFT JOIN developers
                    ON game_developers.developer_id = developers.developer_id
                    LEFT JOIN game_publishers
                    ON games.game_id = game_publishers.game_id
                    LEFT JOIN publishers 
                    ON game_publishers.publisher_id = publishers.publisher_id
                    LEFT JOIN game_genres
                    ON games.game_id = game_genres.game_id
                    LEFT JOIN genres
                    ON game_genres.genre_id = genres.genre_id
                    GROUP BY games.game_id
                    LIMIT {} OFFSET {}'''
                    .format(
                    page_size,
                    page_size*(page_number - 1))).fetchall()
                return [Games(*row) for row in rows]

            rows = db.execute('''select distinct games.game_id, games.name, games.description, games.all_reviews, games.release_date,developers.developer_name, publishers.publisher_name, genres.genre_name, games.minimum_requirements, games.recommended_requirements, games.original_price 
                FROM games
                LEFT JOIN game_developers
                ON games.game_id = game_developers.game_id 
                LEFT JOIN developers
                ON game_developers.developer_id = developers.developer_id
                LEFT JOIN game_publishers
                ON games.game_id = game_publishers.game_id
                LEFT JOIN publishers 
                ON game_publishers.publisher_id = publishers.publisher_id
                LEFT JOIN game_genres
                ON games.game_id = game_genres.game_id
                LEFT JOIN genres
                ON game_genres.genre_id = genres.genre_id
                WHERE instr(name, "{}") > 0
                GROUP BY games.game_id
                LIMIT {} OFFSET {}
                '''
                .format(
                search_query,
                page_size,
                page_size*(page_number - 1))).fetchall()

            return [Games(*row) for row in rows]

    @staticmethod
    def get(id):
        with Database() as db:
            rows = db.execute(
                '''SELECT games.game_id, games.name, games.description, games.all_reviews, games.release_date,developers.developer_name, publishers.publisher_name, genres.genre_name, games.minimum_requirements, games.recommended_requirements, games.original_price 
                    FROM games
                    LEFT JOIN game_developers
                    ON games.game_id = game_developers.game_id 
                    LEFT JOIN developers
                    ON game_developers.developer_id = developers.developer_id
                    LEFT JOIN game_publishers
                    ON games.game_id = game_publishers.game_id
                    LEFT JOIN publishers 
                    ON game_publishers.publisher_id = publishers.publisher_id
                    LEFT JOIN game_genres
                    ON games.game_id = game_genres.game_id
                    LEFT JOIN genres
                    ON game_genres.genre_id = genres.genre_id
                    WHERE games.game_id = {}
                    GROUP BY games.game_id'''
            .format(id)).fetchall()
            return [Games(*row) for row in rows][0]
