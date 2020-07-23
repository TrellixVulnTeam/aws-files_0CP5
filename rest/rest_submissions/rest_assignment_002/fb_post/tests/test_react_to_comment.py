from django.utils import timezone

import pytest
from freezegun import freeze_time
from fb_post.utils.react_to_comment import react_to_comment
from fb_post.models import Reaction
from fb_post.exceptions import InvalidUserException, InvalidCommentException
from fb_post.exceptions import InvalidReactionTypeException
from fb_post.constants import ReactionEnum


@pytest.mark.django_db
@freeze_time("2020-04-19")
class TestReactToComment:

    def test_react_to_comment_with_valid_details_for_the_first_time_create_reaction(
            self, user, post, comment):

        # Arrange
        user_id = 1
        comment_id = 1
        reaction_type = ReactionEnum.THUMBSUP.value

        # Act
        react_to_comment(
            user_id,
            comment_id,
            reaction_type
        )

        # Assert
        react = Reaction.objects.get(
            comment_id=comment_id,
            reacted_by_id=user_id
        )

        assert react.reaction == reaction_type
        assert react.reacted_at == timezone.now()


    def test_react_to_comment_with_valid_details_when_user_reacting_with_post_with_same_reaction_and_delete_reaction(
            self, user, post, comment):

        # Arrange
        user_id = 1
        comment_id = 1
        reaction_type = ReactionEnum.THUMBSUP.value
        react_to_comment(
            user_id,
            comment_id,
            reaction_type
        )

        # Act
        react_to_comment(
            user_id,
            comment_id,
            reaction_type
        )

        # Assert
        with pytest.raises(Reaction.DoesNotExist):
            Reaction.objects.get(
                comment_id=comment_id,
                reacted_by_id=user_id
            )


    @pytest.mark.parametrize(
        'reaction_type_1',
        [(ReactionEnum.ANGRY.value), (ReactionEnum.WOW.value)])
    def test_react_to_comment_with_valid_details_when_user_reacting_with_post_with_different_reaction_and_update_reaction(
            self, user, post, comment, reaction_type_1):

        # Arrange
        user_id = 1
        comment_id = 1
        reaction_type = reaction_type_1

        # Act
        react_to_comment(
            user_id,
            comment_id,
            reaction_type
        )

        # Assert
        react = Reaction.objects.get(
            comment_id=comment_id,
            reacted_by_id=user_id
        )

        assert react.reaction == reaction_type


    def test_react_to_comment_with_invaid_user_id_raise_error(
            self, user, post, comment):

        # Arrange
        user_id = 0
        comment_id = 1
        reaction_type = ReactionEnum.WOW.value

        # Act
        with pytest.raises(InvalidUserException):
            react_to_comment(
                user_id,
                comment_id,
                reaction_type
            )

    def test_react_to_comment_with_invaid_post_id_raise_error(
            self, user, post, comment):

        # Arrange
        user_id = 1
        comment_id = 0
        reaction_type = ReactionEnum.WOW.value

        # Act
        with pytest.raises(InvalidCommentException):
            react_to_comment(
                user_id,
                comment_id,
                reaction_type
            )

    def test_react_to_comment_with_invaid_reaction_type_raise_error(
            self, user, post, comment):

        # Arrange
        user_id = 1
        comment_id = 1
        reaction_type = 'Ohhh'

        # Act
        with pytest.raises(InvalidReactionTypeException):
            react_to_comment(
                user_id,
                comment_id,
                reaction_type
            )
