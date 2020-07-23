from .models import *
#Actor,Director,Movie,Cast,Rating
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from django.db.models import *

# Task-1
def populate_database(actors_list,movies_list,directors_list,movie_rating_list):
    
    for item in actors_list:
        actor=Actor.objects.create(
                actor_id=item['actor_id'],
                name=item['name'],
                gender=item['gender']
                )
    for item in directors_list:
        director=Director.objects.create(name=item)
                    
    for item in movies_list:
        movie=Movie.objects.create(
                movie_id=item['movie_id'],
                name=item['name'],
                box_office_collection_in_crores=item['box_office_collection_in_crores'],
                release_date=item['release_date'],
                director=Director.objects.get(name=item['director_name'])
                )
        
        for cast_item in item['actors']:    
            actors=Cast.objects.create(
                actor=Actor.objects.get(actor_id=cast_item['actor_id']),
                movie=Movie.objects.get(movie_id=item['movie_id']),
                role=cast_item['role'],
                is_debut_movie=cast_item['is_debut_movie']
                )
        
    for item in movie_rating_list:
        rating=Rating.objects.create(
                movie=Movie.objects.get(movie_id=item['movie_id']),
                rating_one_count=item['rating_one_count'],
                rating_two_count=item['rating_two_count'],
                rating_three_count=item['rating_three_count'],
                rating_four_count=item['rating_four_count'],
                rating_five_count=item['rating_five_count']
            )
    

# Task-2
def remove_all_actors_from_given_movie(movie_object):
    return movie_obj.actors.clear()

# Task-3
def get_all_rating_objects_for_given_movies(movie_objs):
    result=Rating.objects.filter(movie__in=movie_objs)
    return result

# Task-4
def get_movies_by_given_movie_names(movie_names):
    movie_list=[]
    
    for movie in Movie.objects.filter(name__in=movie_names):
        cast_list=[]
        for cast in Cast.objects.filter(movie=movie):
            cast_dict={
                'actor':{
                    'name': cast.actor.name,
                    'actor_id': cast.actor.actor_id
                        },
                'role': cast.role,
                'is_debut_movie': cast.is_debut_movie
                    }
            
            cast_list.append(cast_dict)
        movie_dict={
        'movie_id': movie.movie_id,
        'name': movie.name,
        'cast': cast_list,
        'box_office_collection_in_crores': movie.box_office_collection_in_crores,
        'release_date': str(movie.release_date),
        'director_name': movie.director.name,
        'average_rating': get_average_rating_of_movie(movie),
        'total_number_of_ratings': get_total_rating_of_movie(movie)
        }
        
        movie_list.append(movie_dict)
    return movie_list

# Task-5
def get_all_actor_objects_acted_in_given_movies(movie_objs):
    result=Actor.objects.filter(movie__in=movie_objs).distinct()
    return result

# Task-6
def get_female_cast_details_from_movies_having_more_than_five_female_cast():
    pass

# Task-7
def get_actor_movies_released_in_year_greater_than_or_equal_to_2000():
    pass

# Task-8
def reset_ratings_for_movies_in_given_year(year):
    Rating.objects.filter(
    Q(movie__release_date__year=year)
        ).update(
            rating_one_count=0,
            rating_two_count=0,
            rating_three_count=0,
            rating_four_count=0,
            rating_five_count=0
            )
    














































"""    
    for item in actors_list:
        actor=Actor.objects.create(
                actor_id=item['actor_id'],
                name=item['name'],
                gender=item['gender']
                )
        #actor.save()
    for item in directors_list:
        director=Director(name=item)
        director.save()
                    
    for item in movies_list:
        movie=Movie.objects.create(
                movie_id=item['movie_id'],
                name=item['name'],
                box_office_collection_in_crores=item['box_office_collection_in_crores'],
                release_date=item['release_date'],
                director=Director.objects.get(name=item['director_name'])
                )
        
        for cast_item in item['actors']:    
            actors=Cast.objects.create(
                actor=Actor.objects.get(actor_id=cast_item['actor_id']),
                movie=Movie.objects.get(movie_id=item['movie_id']),
                role=cast_item['role'],
                is_debut_movie=cast_item['is_debut_movie']
                )
                    
        #movie.save()
            
    
        
    for item in movie_rating_list:
        rating=Rating.objects.create(
                movie=Movie.objects.get(movie_id=item['movie_id']),
                rating_one_count=item['rating_one_count'],
                rating_two_count=item['rating_two_count'],
                rating_three_count=item['rating_three_count'],
                rating_four_count=item['rating_four_count'],
                rating_five_count=item['rating_five_count']
            )
        #rating.save() 
        
"""
