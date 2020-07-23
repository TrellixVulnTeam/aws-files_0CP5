from django.test import TestCase
import pytest
# Create your tests here.
from . models import *

from freezegun import freeze_time
import datetime
import unittest
from django.utils import *



@pytest.mark.django_db
def test_reactions_count_and_return_count_of_reactions(
    user, post, comment, replycomment, reactcomment, reactpost):
    
    # Arrange
    reactions = {'count': 9}
    
    # Act
    reactions_count = get_total_reaction_count()

    # Assert
    assert reactions_count == reactions

 
@pytest.mark.django_db
def test_get_reaction_matrices_for_given_post(
    user, post, comment, replycomment, reactpost, reactcomment):
    
    # Arrange
    post_id = 1
    post_reactions = {ReactionEnum.LOVE.value: 1, ReactionEnum.THUMBSDOWN.value: 1, ReactionEnum.WOW.value: 1}
    
    # Act
    reactions = get_reaction_metrics(post_id)
    
    # Assert
    assert reactions == post_reactions
    
    
@pytest.mark.django_db
def test_get_posts_with_more_postive_reactions_and_return_post_ids(
    user, post, reactpost):
   
    # Arrange
    post_list = [1]
    
    # Act
    posts = get_posts_with_more_positive_reactions()
    
    # Assert
    assert posts == post_list
    

@pytest.mark.django_db
def test_get_posts_with_more_negative_reactions_return_empty_list(
    user, post):
    
    # Arrange
    Reaction(
            post_id = 1, 
            reaction = ReactionEnum.THUMBSDOWN.value, 
            reacted_by_id = 4
        )
    Reaction(
            post_id = 1, 
            reaction = ReactionEnum.ANGRY.value, 
            reacted_by_id = 3
        )
    post_list = []
    
    # Act
    posts = get_posts_with_more_positive_reactions()
    
    # Assert
    assert posts == post_list


@pytest.mark.django_db
def test_get_posts_with_positive_reactions_equals_to_negative_reactions_return_empty_list(
    user, post):
    
    # Arrange
    Reaction(
            post_id = 1, 
            reaction = ReactionEnum.THUMBSDOWN.value, 
            reacted_by_id = 4
        )
        
    post_list = []
    
    # Act
    posts = get_posts_with_more_positive_reactions()
    
    # Assert
    assert posts == post_list


@pytest.mark.django_db
class TestUserPosts:
    
    pytest.mark.django_db
    
    def test_get_user_posts_details_with_valid_user_id(
        self, user, post, comment, replycomment, reactpost, reactcomment):
       
        # Arrange
        user_id = 2
        user_post_details = [{'post_id': 2,
                              'posted_by': {
                                  'name': 'Sagaram', 
                                  'user_id': 2, 
                                  'profile_pic': ''
                                },
                              'posted_at': '2020-04-18 00:00:00.000000',
                              'post_content': 'hello',
                              'reactions': {
                                  'count': 2, 
                                  'type': ['LOVE', 'SAD']
                                },
                              'comments': [{
                                'comment_id': 3,
                                'commenter': {
                                    'user_id': 1, 
                                    'name': 'Prathap', 
                                    'profile_pic': ''
                                    },
                                'commented_at': '2020-04-18 00:00:00.000000',
                                'comment_content': 'ahaa',
                                'reactions': {
                                    'count': 1, 
                                    'type': ['WOW']
                                    },
                                'replies_count': 0,
                                'replies': []
                              }],
                              'comments_count': 1
        }]
                              

        # Act
        post_details = get_user_posts(user_id)
        
        # Assert
        check_post_details(post_details[0],  user_post_details[0])
        
        
    def test_get_user_posts_details_with_valid_user_id_and_users_do_not_have_any_posts_return_empty_list(
        self, user, post, comment, replycomment, reactpost, reactcomment):
         
         # Arrange
        user_id = 3
        user_post_details = []
        
        # Act
        post_details = get_user_posts(user_id)
        
        # Assert
        assert post_details == user_post_details
        
    def test_get_user_posts_details_with_invalid_user_id_raise_error(self):
        
        # Arrange
        user_id = 1
        
        # Act
        with pytest.raises(InvalidUserException):
            get_user_posts(user_id)
            
