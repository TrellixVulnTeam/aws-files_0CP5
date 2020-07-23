from django.utils import timezone

import pytest
from freezegun import freeze_time
from fb_post.utils.create_comment import create_comment
from fb_post.models import Comment
from fb_post.exceptions import InvalidUserException, InvalidPostException
from fb_post.exceptions import InvalidCommentContent


@pytest.mark.django_db
@freeze_time("2020-04-18")
class TestCreateComments:

    def test_create_comment_with_valid_details_return_comment_id(
            self, user, post):

        # Arrange
        user_id = 2
        post_id = 1
        comment_content = "superb"

        # Act
        comment_id = create_comment(
            user_id,
            post_id,
            comment_content
        )

        # Assert
        comment = Comment.objects.get(
            id=comment_id
        )

        assert comment.content == comment_content
        assert comment.commented_by_id == user_id
        assert comment.post_id == post_id
        assert comment.commented_at == timezone.now()

    def test_create_comment_with_invalid_user_id_raise_error(
            self, post, user):

        # Arrange
        user_id = 0
        post_id = 2
        comment_content = "nice"

        # Act
        with pytest.raises(InvalidUserException):
            create_comment(
                user_id,
                post_id,
                comment_content
            )

        # Assert


    def test_create_comment_with_invalid_post_id_raise_error(
            self, post, user):

        # Arrange
        user_id = 1
        post_id = 0
        comment_content = "nice"

        # Act
        with pytest.raises(InvalidPostException):
            create_comment(
                user_id,
                post_id,
                comment_content
            )

        # Assert

    def test_create_comment_with_invalid_comment_content_raise_error(
            self, post, user):

        # Arrange
        user_id = 1
        post_id = 2
        comment_content = ""

        # Act
        with pytest.raises(InvalidCommentContent):
            create_comment(
                user_id,
                post_id,
                comment_content
            )

        # Assert
