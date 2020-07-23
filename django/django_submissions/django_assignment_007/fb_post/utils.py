from . models import *
from . exceptions import *
from datetime import datetime
'''
# Task-2
def create_post(user_id, post_content):
    user = User.objects.filter(id=user_id).exists()
    if not user:
        raise InvalidUserException
    if post_content == "":
        raise InvalidPostContent
    else:
        post=Post.objects.create(
            content=post_content,
            posted_by_id=user_id
            )
        return post.id
  
# Task-3          
def create_comment(user_id, post_id, comment_content):
    user = User.objects.filter(id=user_id).exists()
    post = Post.objects.filter(id=post_id).exists()
    if not user:
        raise InvalidUserException
    if not post:
        raise InvalidPostException
    if comment_content == "":
        raise InvalidCommentContent
    else:
        comment=Comment.objects.create(
            content=comment_content,
            commented_by_id=user_id,
            post_id=post_id
            )
        return comment.id
        
# Task-4
def reply_to_comment(user_id, comment_id, reply_content):
    user = User.objects.filter(id=user_id)
    comments = Comment.objects.filter(id=comment_id)
    len(comments)
    if user.exists() == False:
        raise InvalidUserException
    if comments.exists() == False:
        raise InvalidCommentException
    if reply_content == "":
        raise InvalidReplyContent
    else:
        if(comments[0].parent_comment_id):
            comment=Comment.objects.create(
                content=reply_content,
                commented_by_id=user_id,
                post_id=comments[0].post_id,
                parent_comment_id=comments[0].parent_comment_id
                )
        else:
            comment=Comment.objects.create(
                content=reply_content,
                commented_by_id=user_id,
                post_id=comments[0].post_id,
                parent_comment_id=comment_id
                )
        return comment.id
        
# Task-5
def react_to_post(user_id, post_id, reaction_type):
    user = User.objects.filter(id=user_id)
    post = Post.objects.filter(id=post_id)
    if user.exists() == False:
        raise InvalidUserException
    if post.exists() == False:
        raise InvalidPostException
    if reaction_type not in ['WOW', 'LIT', 'LOVE', 'HAHA', 'THUMBS-UP',
                            'THUMBS-DOWN', 'ANGRY', 'SAD']:
        raise InvalidReactionTypeException
    else:
        try:
            react=Reaction.objects.get(
                reacted_by_id=user_id,
                post_id=post_id
                )
        except:
            Reaction.objects.create(
                reacted_by_id=user_id,
                post_id=post_id,
                reaction=reaction_type
                )
            return
            
        if react.reaction == reaction_type:
            react.delete()
        else:
            react.reaction = reaction_type
            react.reacted_at = datetime.now()
            react.save()
            
# Task-6
def react_to_comment(user_id, comment_id, reaction_type):
    user = User.objects.filter(id=user_id)
    comment = Comment.objects.filter(id=comment_id)
    if user.exists() == False:
        raise InvalidUserException
    if comment.exists() == False:
        raise InvalidCommentException
    if reaction_type not in ['WOW', 'LIT', 'LOVE', 'HAHA', 'THUMBS-UP',
                            'THUMBS-DOWN', 'ANGRY', 'SAD']:
        raise InvalidReactionTypeException
    else:
        try:
            react=Reaction.objects.get(
                reacted_by_id=user_id,
                comment_id=comment_id
                )
        except:
            Reaction.objects.create(
                reacted_by_id=user_id,
                comment_id=comment_id,
                reaction=reaction_type
                )
            return
            
        if react.reaction == reaction_type:
            react.delete()
        else:
            react.reaction = reaction_type
            react.reacted_at = datetime.now()
            react.save()
    
# Task-7
def get_total_reaction_count():
    return Reaction.objects.aggregate(
        count=Count('id')
        )
        
# Task-8
def get_reaction_metrics(post_id):
    post = Post.objects.filter(id=post_id)
    if post.exists() == False:
        raise InvalidPostException
    else:
        matrices = Reaction.objects.values('reaction').filter(post_id=post_id).annotate(
            count=Count('reaction')
            )
        reaction_matrices={}
        for matric in  matrices:
            reaction_matrices[matric['reaction']] = matric['count']
    return reaction_matrices
    
# Task-9
def delete_post(user_id, post_id):
    post=Post.objects.filter(id=post_id,posted_by_id=user_id)
    if len(post) > 0:
        post.delete()
    else:
        #user = User.objects.filter(id=user_id).exists()
        #post = Post.objects.filter(id=post_id).exists()
        if not User.objects.filter(id=user_id).exists():
            raise InvalidUserException
        if not Post.objects.filter(id=post_id).exists():
            raise InvalidPostException
        raise UserCannotDeletePostException
        
# Task-10
def get_posts_with_more_positive_reactions():
    positive_reactions=[
        'THUMBS-UP', 'LIT', 'LOVE', 'HAHA', 'WOW'
        ]
    negative_reactions=[
        'SAD', 'ANGRY', 'THUMBS-DOWN'
        ]
    positive_count=Count('reactions',filter=Q(
        reactions__reaction__in=positive_reactions))
    negative_count=Count('reactions',filter=Q(
        reactions__reaction__in=negative_reactions))
    post=Post.objects.annotate(pcount=positive_count
        ).annotate(ncount=negative_count).filter(
        pcount__gt=F('ncount')
        ).values_list('id', flat=True)
    return list(post)
    
# Task-11
def get_posts_reacted_by_user(user_id):
    user = User.objects.filter(id=user_id)
    if user.exists() == False:
        raise InvalidUserException
    else:
        post=Post.objects.filter(
            reactions__reacted_by_id=user_id
            ).values_list('id', flat=True)
        return list(post)
        
# Task-12
def get_reactions_to_post(post_id):
    post = Post.objects.filter(id=post_id)
    if post.exists() == False:
        raise InvalidPostException
    else:
        reactions=Reaction.objects.filter(
            post_id=post_id
            ).select_related('reacted_by')
        user_list=[]
        for react in reactions:
            user_dict={
                'user_id': react.reacted_by_id,
                'name': react.reacted_by.name,
                'profile_pic': react.reacted_by.profile_pic,
                'reaction': react.reaction
            }
            user_list.append(user_dict)
        return user_list
        
# Task-13
def get_post(post_id,post_value=False):
    
    if post_value == False:
        post = Post.objects.filter(id=post_id)
        
        if post.exists() == False:
            raise InvalidPostException
            
        posts = Post.objects.filter(
                id=post_id).select_related(
                    'posted_by'
                    ).prefetch_related('reactions',
                    Prefetch('comments',
                    queryset=Comment.objects.select_related(
                        'commented_by').prefetch_related('reactions')))
        
    else:
        posts = Post.objects.filter(
            posted_by_id=post_id).select_related(
                'posted_by'
                ).prefetch_related('reactions',
                Prefetch('comments',
                queryset=Comment.objects.select_related(
                    'commented_by').prefetch_related('reactions')))
        """ 
            Post.objects.filter(
            posted_by_id=post_id).select_related(
                'posted_by'
                ).prefetch_related('reactions',
                'comments__commented_by',
                'comments__reactions')
                
        """
    
    post_list=[]
    
    for post in posts:
        comment_list=[]
            
        post_comments = list(post.comments.all())
        for comment in post_comments:
                
            if comment.parent_comment_id == None:
                    
                replies_list=[]
                comments_list=[]
                for comments in post_comments:
                    if comment.id == comments.parent_comment_id:
                        comments_list.append(comments)
                    
                for comment_reply in comments_list:
                        
                    reply_react_list=[]
                    for react in list(comment_reply.reactions.all()):
                        if react.reaction not in reply_react_list:
                            reply_react_list.append(react.reaction)
                        
                    replies_dict={
                            'comment_id': comment_reply.id,
                            'commenter': {
                                'user_id': comment_reply.commented_by_id,
                                'name': comment_reply.commented_by.name,
                                'profile_pic': comment_reply.commented_by.profile_pic
                            },
                            'commented_at': str(datetime.strftime(comment_reply.commented_at,'%Y-%m-%d %H:%M:%S.%f')),
                            'comment_content': comment_reply.content,
                            'reactions': {
                            'count': len(reply_react_list),
                            'type': reply_react_list
                            },
                    }
                    replies_list.append(replies_dict)
                        
                comment_react_list=[]
                for react in list(comment.reactions.all()):
                    if react.reaction not in comment_react_list:
                        comment_react_list.append(react.reaction)
                        
                comment_dict={
                        'comment_id': comment.id,
                        'commenter': {
                          'user_id': comment.commented_by_id,
                          'name': comment.commented_by.name,
                          'profile_pic': comment.commented_by.profile_pic
                        },
                        'commented_at': str(datetime.strftime(comment.commented_at,'%Y-%m-%d %H:%M:%S.%f')),
                        'comment_content': comment.content,
                        'reactions': {
                          'count': len(comment_react_list),
                          'type': comment_react_list
                        },
                        'replies_count': len(replies_list),
                        'replies': replies_list,
                }
                comment_list.append(comment_dict)
        post_react_list=[]
        for react in list(post.reactions.all()):
            if react.reaction not in post_react_list:
                post_react_list.append(react.reaction)
            
        post_dict={
                'post_id': post.id,
                'posted_by': {
                    'name': post.posted_by.name,
                    'user_id': post.posted_by_id,
                    'profile_pic': post.posted_by.profile_pic
                },
                'posted_at': str(datetime.strftime(post.posted_at,'%Y-%m-%d %H:%M:%S.%f')),
                'post_content': post.content,
                'reactions': {
                  'count': post.reactions.count(),
                  'type': post_react_list,
                },
                'comments': comment_list,
                'comments_count': len(comment_list),
        }
        post_list.append(post_dict)
    if post_value == True:
        return post_list
    else:
        return post_list[0]
        
# Task-14
def get_user_posts(user_id):
    user = User.objects.filter(id=user_id)
    if user.exists() == False:
        raise InvalidUserException
    else:
        user_posts=get_post(user_id,post_value=True)
        return user_posts

# Task-15
def get_replies_for_comment(comment_id):
    comment = Comment.objects.filter(id=comment_id)
    if comment.exists() == False:
        raise InvalidCommentException
    else:
        comments=Comment.objects.select_related(
            'commented_by').filter(
            parent_comment_id=comment_id
            )
            
        comment_list=[]
        for comment in comments:
            comment_dict={
                'comment_id': comment.id,
                'commenter': {
                  'user_id': comment.commented_by_id,
                  'name': comment.commented_by.name,
                  'profile_pic': comment.commented_by.profile_pic
                },
                'commented_at': str(datetime.strftime(comment.commented_at,'%Y-%m-%d %H:%M:%S.%f')),
                'comment_content': comment.content,
            }
            comment_list.append(comment_dict)
        return comment_list
'''
        
# Assignment-7
# Task-1

# completed

# Task-2
def create_group(user_id, name, member_ids):
    user_ids  = list(User.objects.values_list('id',flat=True))
    if user_id not in user_ids:
        raise InvalidUserException
    if not name:
        raise InvalidGroupNameException
    else:
        member_ids = list(set(member_ids))
        
        for id in member_ids:
            if id not in user_ids:
                raise InvalidMemberException
                
        if user_id in member_ids:
            member_ids.remove(user_id)
        
        group = Group.objects.create(name=name)
        group.members.add(user_id, through_defaults={'is_admin':True})
                
        group.members.add(*member_ids)
        
        return group.id
        

# Task-3
def add_member_to_group(user_id, new_member_id, group_id):
    user_ids  = list(User.objects.values_list('id',flat=True))
    
    if user_id not in user_ids:
        raise InvalidUserException
        
    if new_member_id not in user_ids:
        raise InvalidMemberException
        
    groups = Group.objects.filter(
        id=group_id).prefetch_related('membership_set')
        
    
    if not groups:
        raise InvalidGroupException
    else:
        for group in groups:        
            group_member_ids =[]
            for member in group.members.all():
                group_member_ids.append(member.id)
                
            if user_id not in group_member_ids:
                raise UserNotInGroupException
            
            group_admins=[]
            for admin in group.membership_set.filter(is_admin=True):
                group_admins.append(admin.member_id)
                
            if user_id not in group_admins:
                raise UserIsNotAdminException
                
            if new_member_id not in group_member_ids:
                group.members.add(new_member_id)
            
    
# Task-4
def remove_member_from_group(user_id, member_id, group_id):
    user_ids  = list(User.objects.values_list('id',flat=True))
    
    if user_id not in user_ids:
        raise InvalidUserException
        
    if member_id not in user_ids:
        raise InvalidMemberException
        
    groups = Group.objects.filter(
        id=group_id).prefetch_related('membership_set')
        
    if not groups:
        raise InvalidGroupException
    else:
        for group in groups:        
            
            group_member_ids =[]
            for member in group.members.all():
                group_member_ids.append(member.id)
                
            if user_id not in group_member_ids:
                raise UserNotInGroupException
            if member_id not in group_member_ids:
                raise MemberNotInGroupException
            
            
            if not group.membership_set.get(member_id=user_id).is_admin:
                raise UserIsNotAdminException
            else:
                group.members.remove(member_id)
                #group.membership_set.remove(Membership.objects.get(member_id=member_id))
        

# Task-5
def make_member_as_admin(user_id, member_id, group_id):
    user_ids  = list(User.objects.values_list('id',flat=True))
    
    if user_id not in user_ids:
        raise InvalidUserException
        
    if member_id not in user_ids:
        raise InvalidMemberException
        
    groups = Group.objects.filter(
        id=group_id).prefetch_related('membership_set')
        
    if not groups:
        raise InvalidGroupException
    else:
        for group in groups:        
            
            group_member_ids =[]
            for member in group.members.all():
                group_member_ids.append(member.id)
                
            if user_id not in group_member_ids:
                raise UserNotInGroupException
                
            if member_id not in group_member_ids:
                raise MemberNotInGroupException
            
            if not group.membership_set.get(member_id=user_id).is_admin:
                raise UserIsNotAdminException
            else:
                if  not group.membership_set.get(member_id=member_id).is_admin:
                    Membership.objects.filter(
                        group_id = group_id, member_id = member_id).update(
                        is_admin=True
                    )
                    
# Task-6
def create_post(user_id, post_content, group_id=None):
    user = User.objects.filter(id=user_id).exists()
    if not user:
        raise InvalidUserException
    if not post_content:
        raise InvalidPostContent
    
    if group_id:
        group = Group.objects.filter(id=group_id)
        if not group:
            raise InvalidGroupException
        else:    
            group_member_ids =[]
            for member in group[0].members.all():
                group_member_ids.append(member.id)
                    
            if user_id not in group_member_ids:
                raise UserNotInGroupException
            
    post=Post.objects.create(
            content=post_content,
            posted_by_id=user_id,
            group_id = group_id
            )
    return post.id
        
            
# Task-7
def get_group_feed(user_id, group_id, offset, limit):
    user = User.objects.filter(id=user_id)
    if not user:
        raise InvalidUserException
    
    group = Group.objects.filter(id=group_id)
    if not group:
        raise InvalidGroupException
    
    group_ids=[]
    for member in group[0].members.all():
        group_ids.append(member.id)
    
    if user_id not in group_ids:
        raise UserNotInGroupException
        
    if offset < 0:
        raise InvalidOffSetValueException
    if limit <= 0:
        raise InvalidLimitSetValueException
    
    posts = list(Post.objects.filter(
            posted_by_id=user_id, group_id=group_id).select_related(
                'posted_by'
                ).prefetch_related('reactions',
                Prefetch('comments',
                queryset=Comment.objects.select_related(
                    'commented_by').prefetch_related('reactions'))))[offset:limit+offset]
                    
    post_list=[]
    
    for post in posts:
        comment_list=[]
            
        post_comments = list(post.comments.all())
        for comment in post_comments:
                
            if comment.parent_comment_id == None:
                    
                replies_list=[]
                comments_list=[]
                for comments in post_comments:
                    if comment.id == comments.parent_comment_id:
                        comments_list.append(comments)
                    
                for comment_reply in comments_list:
                        
                    reply_react_list=[]
                    for react in list(comment_reply.reactions.all()):
                        if react.reaction not in reply_react_list:
                            reply_react_list.append(react.reaction)
                        
                    replies_dict={
                            'comment_id': comment_reply.id,
                            'commenter': {
                                'user_id': comment_reply.commented_by_id,
                                'name': comment_reply.commented_by.name,
                                'profile_pic': comment_reply.commented_by.profile_pic
                            },
                            'commented_at': str(datetime.strftime(comment_reply.commented_at,'%Y-%m-%d %H:%M:%S.%f')),
                            'comment_content': comment_reply.content,
                            'reactions': {
                            'count': len(reply_react_list),
                            'type': reply_react_list
                            },
                    }
                    replies_list.append(replies_dict)
                        
                comment_react_list=[]
                for react in list(comment.reactions.all()):
                    if react.reaction not in comment_react_list:
                        comment_react_list.append(react.reaction)
                        
                comment_dict={
                        'comment_id': comment.id,
                        'commenter': {
                          'user_id': comment.commented_by_id,
                          'name': comment.commented_by.name,
                          'profile_pic': comment.commented_by.profile_pic
                        },
                        'commented_at': str(datetime.strftime(comment.commented_at,'%Y-%m-%d %H:%M:%S.%f')),
                        'comment_content': comment.content,
                        'reactions': {
                          'count': len(comment_react_list),
                          'type': comment_react_list
                        },
                        'replies_count': len(replies_list),
                        'replies': replies_list,
                }
                comment_list.append(comment_dict)
        post_react_list=[]
        for react in list(post.reactions.all()):
            if react.reaction not in post_react_list:
                post_react_list.append(react.reaction)
            
        post_dict={
                'post_id': post.id,
                'posted_by': {
                    'name': post.posted_by.name,
                    'user_id': post.posted_by_id,
                    'profile_pic': post.posted_by.profile_pic
                },
                'posted_at': str(datetime.strftime(post.posted_at,'%Y-%m-%d %H:%M:%S.%f')),
                'post_content': post.content,
                'reactions': {
                  'count': post.reactions.count(),
                  'type': post_react_list,
                },
                'comments': comment_list,
                'comments_count': len(comment_list),
        }
        post_list.append(post_dict)
    
    return post_list

# Task-8
def get_posts_with_more_comments_than_reactions():

    post=Post.objects.annotate(
        comment_count=Count('comments')).annotate(
            reaction_count=Count('reactions')).filter(
                comment_count__gt=F('reaction_count')
                ).values_list('id',flat=True)
                
    return list(post)
    
# Task-9
def get_user_posts(user_id):
    pass

# Task-10
def get_silent_group_members(group_id):
    group = Group.objects.filter(id=group_id)
    if not group:
        raise InvalidGroupException
    else:
        group_member_ids =[]
        for member in group[0].members.all():
            group_member_ids.append(member.id)
        
        active_users=[]
        for member in Post.objects.filter(group_id=group_id):
            active_users.append(member.posted_by_id)
            
        active_user_ids=list(set(active_users))
        
        silent_group_members=[]
        for member in group_member_ids:
            if member not in active_user_ids:
                silent_group_members.append(member)
                
        return silent_group_members