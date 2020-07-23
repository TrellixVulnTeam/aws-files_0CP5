import pytest
from fb_post.utils.get_replies_for_comment import get_replies_for_comment
from fb_post.exceptions import InvalidCommentException


@pytest.mark.django_db
class TestRepliesForComment:

    def test_get_replies_for_comment_and_return_list_of_replies(
            self, user, post, comment, replycomment):

        # Arrange
        comment_id = 2
        list_of_replies = [{'comment_id': 5,
                            'commenter': {
                                'user_id': 1,
                                'name': 'Prathap',
                                'profile_pic': ''
                                },
                            'commented_at': '2020-04-18 00:00:00.000000',
                            'comment_content': 'haa'
                            }]

        # Act
        replies = get_replies_for_comment(comment_id)

        # Assert
        assert replies == list_of_replies


    def test_get_replies_for_comment_with_invalid_comment_id_raise_error(
            self, user, post, comment, replycomment):

        # Arrange
        comment_id = 0

        # Act
        with pytest.raises(InvalidCommentException):
            get_replies_for_comment(comment_id)
