from django.utils import timezone

import pytest
from freezegun import freeze_time
from fb_post.utils.create_post import create_post
from fb_post.models import Post
from fb_post.exceptions import InvalidUserException, InvalidPostContent


@pytest.mark.django_db
@freeze_time("2020-04-17")
class TestCreatePosts:

    def test_create_post_with_valid_details_return_post_id(
            self, user):

        # Arrange
        user_id = 1
        post_content = "hello"

        # Act
        post_id = create_post(
            user_id,
            post_content
        )

        # Assert
        post = Post.objects.get(id=post_id)

        assert post.posted_by_id == user_id
        assert post.content == post_content
        assert post.posted_at == timezone.now()

    def test_create_post_with_invalid_user_id_raise_error(self):

        # Arrange
        user_id = 1
        post_content = "hello"

        # Act
        with pytest.raises(InvalidUserException):
            create_post(
                user_id,
                post_content
            )

        # Assert

    def test_create_post_with_invalid_post_content_raise_error(
            self, user):

        # Arrange
        user_id = 1
        post_content = ""

        # Act
        with pytest.raises(InvalidPostContent):
            create_post(
                user_id,
                post_content
            )

        # Assert
