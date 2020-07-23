import pytest
from fb_post.utils.get_posts_reacted_by_user import get_posts_reacted_by_user
from fb_post.exceptions import InvalidUserException


@pytest.mark.django_db
class TestReactedPosts:

    def test_get_posts_with_reacted_by_given_user_id_and_return_post_ids(
            self, user, post, reactpost):

        # Arrange
        user_id = 3
        reacted_posts = [1, 2, 3]

        # Act
        posts = get_posts_reacted_by_user(user_id)

        # Assert
        assert posts == reacted_posts

    def test_get_posts_with_reacted_by_invalid_user_id_raise_error(
            self, user, post):

        # Arrange
        user_id = 0

        # Act
        with pytest.raises(InvalidUserException):
            get_posts_reacted_by_user(user_id)
