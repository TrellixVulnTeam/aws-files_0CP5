from .models import *
#Actor,Director,Movie,Cast,Rating
from django.core.exceptions import ObjectDoesNotExist
from datetime import date

def populate_database(actors_list,movies_list,directors_list,movie_rating_list):
    
    for item in actors_list:
        actor=Actor.objects.create(
                actor_id=item['actor_id'],
                name=item['name']
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
            
            
#task 3           
def get_no_of_distinct_movies_actor_acted(actor_id):
    result=Movie.objects.filter(
                actors__actor_id=actor_id
                ).distinct().count()
    return result
    
#task 4
def get_movies_directed_by_director(director_obj):
    result=director_obj.movie_set.all()
    return result
    
#task 5
def get_average_rating_of_movie(movie_obj):
    try:
        avg=(
            1*movie_obj.rating.rating_one_count
            +2*movie_obj.rating.rating_two_count
            +3*movie_obj.rating.rating_three_count
            +4*movie_obj.rating.rating_four_count
            +5*movie_obj.rating.rating_five_count
            )/(
                movie_obj.rating.rating_one_count
                +movie_obj.rating.rating_two_count
                +movie_obj.rating.rating_three_count
                +movie_obj.rating.rating_four_count
                +movie_obj.rating.rating_five_count
            )
        return avg
    except : return 0

#task 6
def delete_movie_rating(movie_obj):
    result=Rating.objects.filter(movie=movie_obj).delete()
    return result
    
#task 7
def get_all_actor_objects_acted_in_given_movies(movie_objs):
    result=Actor.objects.filter(movie__in=movie_objs).distinct()
    return result
    
#task 8
def update_director_for_given_movie(movie_obj, director_obj):
    movie_obj.director=director_obj
    movie_obj.save()
    
#task 9
def get_distinct_movies_acted_by_actor_whose_name_contains_john():
    result=Movie.objects.filter(actors__name__contains='john').distinct()
    return result
    
#task 10
def remove_all_actors_from_given_movie(movie_obj):
    return movie_obj.actors.clear()

#task 11
def get_all_rating_objects_for_given_movies(movie_objs):
    result=Rating.objects.filter(movie__in=movie_objs)
    return result
    