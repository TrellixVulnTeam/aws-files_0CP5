import pytest
from fb_post.utils.delete_post import delete_post
from fb_post.models import Post
from fb_post.exceptions import InvalidUserException, InvalidPostException
from fb_post.exceptions import UserCannotDeletePostException

@pytest.mark.django_db
class TestDeletePost:

    def test_delete_post_with_valid_user_id_and_post_id(
            self, user, post):

        # Arrange
        user_id = 1
        post_id = 1

        # Act
        delete_post(user_id, post_id)

        # Assert
        with pytest.raises(Post.DoesNotExist):
            Post.objects.get(id=post_id)

    def test_delete_post_with_invalid_user_id_raise_error(
            self, user, post):

        # Arrange
        user_id = 0
        post_id = 1

        # Act
        with pytest.raises(InvalidUserException):
            delete_post(user_id, post_id)

        # Assert

    def test_delete_post_with_invalid_post_id_raise_error(
            self, user, post):

        # Arrange
        user_id = 1
        post_id = 0

        # Act
        with pytest.raises(InvalidPostException):
            delete_post(user_id, post_id)

        # Assert

    def test_delete_post_with_user_id_not_matches_post_id(
            self, user, post):

        # Arrange
        user_id = 1
        post_id = 2

        # Act
        with pytest.raises(UserCannotDeletePostException):
            delete_post(user_id, post_id)

        # Assert
