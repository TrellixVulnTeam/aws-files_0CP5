import pytest
from freezegun import freeze_time
import datetime
import unittest
from fb_post.models import User, Post, Comment, Reaction
from fb_post.constants import ReactionEnum


@pytest.fixture
def user():
    
    User.objects.bulk_create([
        User( name = 'Prathap' ),
        User( name = 'Sagaram' ),
        User( name = 'Rajesh' ),
        User( name = 'Naveen' ),
    ])

@pytest.fixture
@freeze_time("2020-04-18")
def post(user):
    
    Post.objects.bulk_create([
        Post(
            content = 'Good morning', 
            posted_by_id = 1
        ),
        Post(
            content = 'hello', 
            posted_by_id = 2
        ),
        Post(
            content = 'say hai', 
            posted_by_id = 4
        )
    ])
    
    
@pytest.fixture
@freeze_time("2020-04-18")
def comment(user, post):
    
    Comment.objects.bulk_create([
        Comment(
            content = 'nice', 
            commented_by_id = 2, 
            post_id = 1
        ),    
        Comment(
            content = 'ohh', 
            commented_by_id = 3, 
            post_id = 1
        ),
        Comment(
            content = 'ahaa', 
            commented_by_id = 1, 
            post_id = 2
        ),
    ])
    

@pytest.fixture
@freeze_time("2020-04-18")
def replycomment(user, post, comment):
    
    Comment.objects.bulk_create([
        Comment(
            content = 'thanks', 
            commented_by_id = 1, 
            post_id = 1, 
            parent_comment_id = 1
        ),    
        Comment(
            content = 'haa', 
            commented_by_id = 1, 
            post_id = 1, 
            parent_comment_id = 2
        ),
    ])
    

@pytest.fixture
def reactpost(user, post):
    
    Reaction.objects.bulk_create([
        Reaction(
            post_id = 1, 
            reaction = ReactionEnum.WOW.value, 
            reacted_by_id = 3
        ),
        Reaction(
            post_id = 2, 
            reaction = ReactionEnum.LOVE.value, 
            reacted_by_id = 1
        ),
        Reaction(
            post_id = 1, 
            reaction = ReactionEnum.THUMBSDOWN.value, 
            reacted_by_id = 2
        ),
        Reaction(
            post_id = 2, 
            reaction = ReactionEnum.SAD.value, 
            reacted_by_id = 3
        ),
        Reaction(
            post_id = 1, 
            reaction = ReactionEnum.LOVE.value, 
            reacted_by_id = 1
        ),
        Reaction(
            post_id = 3, 
            reaction = ReactionEnum.ANGRY.value, 
            reacted_by_id = 3
        ),
    ])
    
    
@pytest.fixture
def reactcomment(user, post, comment, replycomment):
    
    Reaction.objects.bulk_create([
        Reaction(
            comment_id = 1, 
            reaction = ReactionEnum.THUMBSUP.value, 
            reacted_by_id = 1
        ),
        Reaction(
            comment_id = 3, 
            reaction = ReactionEnum.WOW.value, 
            reacted_by_id = 2
        ),
        Reaction(
            comment_id = 4, 
            reaction = ReactionEnum.LIT.value, 
            reacted_by_id = 2
        ),
    ])
