from fb_post_clean_arch.exceptions.custom_exceptions import InvalidCommentId
from fb_post_clean_arch.interactors.presenters.presenter_interface import \
    PresenterInterface
from fb_post_clean_arch.interactors.storages.storage_interface import \
    StorageInterface


class CreateReplyToCommentInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_reply_to_comment(self, comment_id: int,
                       reply_text: str,
                       user_id: int,
                       presenter: PresenterInterface):
        try:
            self.storage.validate_comment_id(comment_id=comment_id)
        except InvalidCommentId:
            presenter.raise_exception_for_invalid_comment()
            return

        comment_id = self.storage.create_reply_to_comment(
            comment_id=comment_id,
            reply_text=reply_text,
            user_id=user_id)

        return presenter.get_create_reply_to_comment_response(
            comment_id=comment_id)
