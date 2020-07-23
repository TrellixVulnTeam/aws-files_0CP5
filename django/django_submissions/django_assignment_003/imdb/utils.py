from .models import *
#Actor,Director,Movie,Cast,Rating
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from django.db.models import Q

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

def get_total_rating_of_movie(movie_obj):
    try:
        avg = movie_obj.rating.rating_one_count + movie_obj.rating.rating_two_count + movie_obj.rating.rating_three_count + movie_obj.rating.rating_four_count + movie_obj.rating.rating_five_count
        return avg
    except: return 0
        
#Task-12

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
    
#Task-13    
def get_movies_released_in_summer_in_given_years():
    movie_list=[]
    for movie in Movie.objects.filter(
        Q(release_date__year__gt=2005),
        Q(release_date__year__lt=2010),
        release_date__month__in=[5,6,7]).distinct():
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
    
    
    #return get_movies_by_given_movie_names(movie)
    
#Task-14
def get_movie_names_with_actor_name_ending_with_smith():
    
    movie=Movie.objects.filter(actors__name__iendswith='smith').values_list('name',flat=True).distinct()
    return list(movie)
    
#Task-15
def get_movie_names_with_ratings_in_given_range():
    movie=Movie.objects.filter(
        Q(rating__rating_five_count__gte=1000),
        Q(rating__rating_five_count__lte=3000)).values_list('name',flat=True).distinct()
    return list(movie)
    
#Task-16
def get_movie_names_with_ratings_above_given_minimum():
    movie=Movie.objects.filter(
        Q(release_date__year__gt=2000),
        Q(rating__rating_five_count__gte=500)|
        Q(rating__rating_four_count__gte=1000)|
        Q(rating__rating_three_count__gte=2000)|
        Q(rating__rating_two_count__gte=4000)|
        Q(rating__rating_one_count__gte=8000)
        ).values_list('name',flat=True).distinct()
    return list(movie)
    
#Task-17
def get_movie_directors_in_given_year():
    director=Director.objects.filter(
        Q(movie__release_date__year=2000)
        ).values_list('name',flat=True).distinct()
    return list(director)
    
#Task-18
def get_actor_names_debuted_in_21st_century():
    actor=Actor.objects.filter(
        Q(movie__release_date__year__range=(2001,2100)),
        Q(cast__is_debut_movie=True)
        ).values_list('name',flat=True).distinct()
    return list(actor)
#Task-19
def get_director_names_containing_big_as_well_as_movie_in_may():
    director=Director.objects.filter(movie__name__contains='big').filter(
        movie__release_date__month=5).values_list('name',flat=True).distinct()
    return list(director)
    
#Task-20
def get_director_names_containing_big_and_movie_in_may():
    director=Director.objects.filter(
        Q(movie__name__contains='big'),
        Q(movie__release_date__month=5)
        ).values_list('name',flat=True).distinct()
    return list(director)
    
#Task-21
def reset_ratings_for_movies_in_this_year():
    Rating.objects.filter(
    Q(movie__release_date__year=2000)
        ).update(
            rating_one_count=0,
            rating_two_count=0,
            rating_three_count=0,
            rating_four_count=0,
            rating_five_count=0
            )