from .models import *
#Actor,Director,Movie,Cast,Rating
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from django.db.models import *
from django.db import *

# Task-1
def populate_database(actors_list,movies_list,directors_list,movie_rating_list):
    
    
    Actor.objects.bulk_create(
            [Actor(
                actor_id=item['actor_id'],
                name=item['name'],
                gender=item['gender'])
                for item in actors_list ])
    
    Director.objects.bulk_create(
        [Director(name=item)
        for item in directors_list ])
                    
    
    for item in movies_list:
        movie_obj=Movie.objects.bulk_create(
        [Movie(
                movie_id=item['movie_id'],
                name=item['name'],
                box_office_collection_in_crores=item['box_office_collection_in_crores'],
                release_date=item['release_date'],
                director=Director.objects.get(name=item['director_name']))
                 ])
        
          
        Cast.objects.bulk_create(
            [Cast(
                    actor_id=cast_item['actor_id'],
                    movie_id=item['movie_id'],
                    role=cast_item['role'],
                    is_debut_movie=cast_item['is_debut_movie'])
                    for cast_item in item['actors'] ])
            
    
    Rating.objects.bulk_create(
        [Rating(
                movie_id=item['movie_id'],
                rating_one_count=item['rating_one_count'],
                rating_two_count=item['rating_two_count'],
                rating_three_count=item['rating_three_count'],
                rating_four_count=item['rating_four_count'],
                rating_five_count=item['rating_five_count'])
                for item in movie_rating_list ])
    

# Task-2
def remove_all_actors_from_given_movie(movie_obj):
    movie_obj.actors.clear()

# Task-3
def get_all_rating_objects_for_given_movies(movie_objs):
    result=Rating.objects.select_related('movie').filter(movie__in=movie_objs)
    return result

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

def get_total_rating_of_movie(movie_obj):
    try:
        avg = movie_obj.rating.rating_one_count + movie_obj.rating.rating_two_count + movie_obj.rating.rating_three_count + movie_obj.rating.rating_four_count + movie_obj.rating.rating_five_count
        return avg
    except: return 0


# Task-4
def get_movies_by_given_movie_names(movie_names):
    movie_list=[]
    movies=Movie.objects.filter(name__in=movie_names).select_related('director','rating').prefetch_related('cast_set__actor')
    for movie in movies:
        cast_list=[]
        for cast in movie.cast_set.all():
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
    movies=Movie.objects.prefetch_related('cast_set__actor').annotate(
        female_count=Count('cast__actor',
        filter=Q(actors__gender='FEMALE'),
        distinct=True)).filter(female_count__gt=5).values_list('name',flat=True)
    
    return get_movies_by_given_movie_names(list(movies))

# Task-7
def get_actor_movies_released_in_year_greater_than_or_equal_to_2000():
    movies=Movie.objects.filter(release_date__year__gte=2000).values_list('name',flat=True)
    
    return get_movies_by_given_movie_names(list(movies))

# Task-8
def reset_ratings_for_movies_in_given_year(year):
    Rating.objects.select_related('movie').filter(
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
