from django.utils import timezone

import pytest
from freezegun import freeze_time
from fb_post.utils.reply_to_comment import reply_to_comment
from fb_post.models import Comment
from fb_post.exceptions import InvalidUserException, InvalidReplyContent
from fb_post.exceptions import InvalidCommentException


@pytest.mark.django_db
@freeze_time("2020-04-19")
class TestReplyToComment:

    def test_reply_to_comment_with_valid_details_return_comment_id(
            self, user, post, comment):

        # Arrange
        user_id = 2
        comment_id = 3
        reply_comment_content = "thanks"
        post_id = 2

        # Act
        comment_id2 = reply_to_comment(
            user_id,
            comment_id,
            reply_comment_content
        )

        # Assert
        comment = Comment.objects.get(
            id=comment_id2
        )

        assert comment.commented_by_id == user_id
        assert comment.content == reply_comment_content
        assert comment.parent_comment_id == comment_id
        assert comment.post_id == post_id
        assert comment.commented_at == timezone.now()


    def test_reply_to_reply_comment_with_valid_details_return_comment_id(
            self, user, post, comment, replycomment):

        # Arrange
        user_id = 2
        comments = Comment.objects.get(
            id=4, parent_comment_id=1
        )
        comment_id = comments.id
        reply_comment_content = "hahaa"
        post_id = 1

        # Act
        comment_id2 = reply_to_comment(
            user_id,
            comment_id,
            reply_comment_content
        )

        # Assert
        comment = Comment.objects.get(
            id=comment_id2
        )

        assert comment.commented_by_id == user_id
        assert comment.content == reply_comment_content
        assert comment.parent_comment_id == comments.parent_comment_id
        assert comment.post_id == post_id
        assert comment.commented_at == timezone.now()


    def test_reply_to_comment_with_invalid_user_id_raise_error(
            self, user, post, comment):

        # Arrange
        user_id = 0
        comment_id = 1
        reply_comment_content = "thanks"

        # Act
        with pytest.raises(InvalidUserException):
            reply_to_comment(
                user_id,
                comment_id,
                reply_comment_content
            )

        # Assert

    def test_create_reply_to_comment_with_invalid_comment_id_raise_error(
            self, user, post, comment):

        # Arrange
        user_id = 1
        comment_id = 0
        reply_comment_content = "thanks"

        # Act
        with pytest.raises(InvalidCommentException):
            reply_to_comment(
                user_id,
                comment_id,
                reply_comment_content
            )

        # Assert

    def test_reply_to_comment_with_invalid_reply_comment_content_raise_error(
            self, user, post, comment):

        # Arrange
        user_id = 1
        comment_id = 1
        reply_comment_content = ""

        # Act
        with pytest.raises(InvalidReplyContent):
            reply_to_comment(
                user_id,
                comment_id,
                reply_comment_content
            )

        # Assert
