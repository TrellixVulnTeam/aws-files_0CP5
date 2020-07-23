
from imdb.utils import *

    
actors_list=[
        {
            "actor_id": "actor_18",
            "name": "actor 18",
            "gender": "MALE"
        }
    ]
movies_list= [
        {
            "movie_id": "movie_7",
            "name": "movie 7",
            "actors": [
                {
                    "actor_id": "actor_18",
                    "role": "hero",
                    "is_debut_movie": False
                }
            ],
            "box_office_collection_in_crores": "10.9",
            "release_date": "2013-6-9",
            "director_name": "Director 7"
        }
    ]
directors_list= [
        "Director 7"
    ]
movie_rating_list= [
        {
            "movie_id": "movie_7",
            "rating_one_count": 15,
            "rating_two_count": 20,
            "rating_three_count": 20,
            "rating_four_count": 20,
            "rating_five_count": 10
        }
    ]
    
populate_database(
        actors_list, movies_list, directors_list, movie_rating_list)