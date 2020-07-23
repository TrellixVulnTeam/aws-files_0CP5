import pytest
from fb_post.utils.get_post import get_post
from fb_post.exceptions import InvalidPostException

def check_post_reaction(posts_reactions, post_details_reactions):
    assert posts_reactions['count'] == post_details_reactions['count']
    assert posts_reactions['type'].sort() == post_details_reactions['type'].sort()


def check_post_details(posts, post_details):

    assert posts['posted_by'] == post_details['posted_by']
    assert posts['comments'] == post_details['comments']
    assert posts['comments_count'] == post_details['comments_count']


@pytest.mark.django_db
class TestPostDetails:

    def test_get_details_of_post_with_valid_post_id(
            self, user, post, comment, replycomment, reactpost, reactcomment):

        # Arrange
        post_id = 1
        post_details = {'post_id': 1,
                        'posted_by': {
                            'name': 'Prathap',
                            'user_id': 1,
                            'profile_pic': ''
                        },
                        'posted_at': '2020-04-18 00:00:00.000000',
                        'post_content': 'Good morning',
                        'reactions': {
                            'count': 3,
                            'type': ['WOW', 'THUMBS-DOWN', 'LOVE']
                        },
                        'comments': [{
                            'comment_id': 1,
                            'commenter': {
                                'user_id': 2,
                                'name': 'Sagaram',
                                'profile_pic': ''
                            },
                            'commented_at': '2020-04-18 00:00:00.000000',
                            'comment_content': 'nice',
                            'reactions': {
                                'count': 1,
                                'type': ['THUMBS-UP']
                            },
                            'replies_count': 1,
                            'replies': [{
                                'comment_id': 4,
                                'commenter': {
                                    'user_id': 1,
                                    'name': 'Prathap',
                                    'profile_pic': ''
                                    },
                                'commented_at': '2020-04-18 00:00:00.000000',
                                'comment_content': 'thanks',
                                'reactions': {
                                    'count': 1,
                                    'type': ['LIT']
                                }
                            }]
                        },
                                     {'comment_id': 2,
                                      'commenter': {
                                          'user_id': 3,
                                          'name': 'Rajesh',
                                          'profile_pic': ''
                                      },
                                      'commented_at': '2020-04-18 00:00:00.000000',
                                      'comment_content': 'ohh',
                                      'reactions': {
                                          'count': 0,
                                          'type': []
                                      },
                                      'replies_count': 1,
                                      'replies': [{
                                          'comment_id': 5,
                                          'commenter': {
                                              'user_id': 1,
                                              'name': 'Prathap',
                                              'profile_pic': ''
                                          },
                                          'commented_at': '2020-04-18 00:00:00.000000',
                                          'comment_content': 'haa',
                                          'reactions': {
                                              'count': 0,
                                              'type': []
                                          }
                                      }]
                                      }],
                        'comments_count': 2
                        }


        # Act
        posts = get_post(post_id)

        # Assert
        check_post_details(posts, post_details)
        check_post_reaction(posts['reactions'], post_details['reactions'])
        #check_comment_details()
        #check_comment_replies_details()


    def test_get_details_of_post_with_invalid_post_id_raise_error(self):

        # Arrange
        post_id = 1

        # Act
        with pytest.raises(InvalidPostException):
            get_post(post_id)
