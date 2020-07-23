from fb_post.constants import DATE_TIME_FORMAT


def get_response_time(datetime_obj):

    date_time = datetime_obj.strftime(DATE_TIME_FORMAT)

    return date_time


def get_user_details_dict(user_obj):

    user_details = {
        'user_id': user_obj.id,
        'name': user_obj.name,
        'profile_pic': user_obj.profile_pic
    }

    return user_details


def get_reactions_dict(reaction_objs):

    reactions_list = (
        reaction_obj.reaction
        for reaction_obj in reaction_objs
    )

    reactions = sorted(list(reactions_list))
    reactions_dict = {
        'count': len(reaction_objs),
        'type': reactions
    }

    return reactions_dict


def get_comment_dict_form(comment):

    comment_reactions_dict = get_reactions_dict(list(comment.reactions.all()))

    comment_dict = {
        'comment_id': comment.id,
        'commenter': get_user_details_dict(comment.commented_by),
        'commented_at': get_response_time(comment.commented_at),
        'comment_content': comment.content,
        'reactions': comment_reactions_dict
    }

    return comment_dict


def get_comment_replies(parent_comment, post_comments):

    comment_replies_list = [
        comment
        for comment in post_comments
        if parent_comment.id == comment.parent_comment_id
    ]

    comment_replies = [
        get_comment_dict_form(comment_reply)
        for comment_reply in comment_replies_list
    ]

    return comment_replies


def get_post_comment_dict_form(comment, post_comments):

    comment_replies_list = get_comment_replies(comment, post_comments)

    comment_dict = get_comment_dict_form(comment)
    comment_dict['replies_count'] = len(comment_replies_list)
    comment_dict['replies'] = comment_replies_list

    return comment_dict


def get_post_comments(post):

    post_comments = list(post.comments.all())

    post_comments_list = [
        get_post_comment_dict_form(comment, post_comments)
        for comment in post_comments
        if comment.parent_comment_id is None
    ]

    return post_comments_list


def get_post_dictionary(post):

    post_comments_list = get_post_comments(post)
    post_reactions_dict = get_reactions_dict(list(post.reactions.all()))

    post_details_dict = {
        'post_id': post.id,
        'posted_by': get_user_details_dict(post.posted_by),
        'posted_at': get_response_time(post.posted_at),
        'post_content': post.content,
        'reactions': post_reactions_dict,
        'comments': post_comments_list,
        'comments_count': len(post_comments_list),
    }

    return post_details_dict
