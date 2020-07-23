import pytest
from fb_post.utils.get_reactions_to_post import get_reactions_to_post
from fb_post.exceptions import InvalidPostException


@pytest.mark.django_db
class TestGetReactionsToPosts:

    def test_get_reactions_to_post_with_valid_post_id(
            self, user, post, reactpost):

        # Arrange
        post_id = 2
        reactions_list = [{'user_id': 1, 'name': 'Prathap', 'profile_pic': '',
                           'reaction': 'LOVE'},
                          {'user_id': 3, 'name': 'Rajesh', 'profile_pic': '',
                           'reaction': 'SAD'}]

        # Act
        list2 = get_reactions_to_post(post_id)

        # Assert
        assert list2 == reactions_list


    def test_get_reactions_to_post_with_invalid_post_id_raise_error(
            self, user, post, reactpost):

        # Arrange
        post_id = 0

        # Act
        with pytest.raises(InvalidPostException):
            get_reactions_to_post(post_id)
