import logging

from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Post


# Post signals
@receiver(post_save, sender=Post)
def log_post_updated_created_event(sender, **kwargs):
    """ Writes info about a newly created or updated post into info log file """
    logger = logging.getLogger(__name__)

    post = kwargs['instance']
    if kwargs['created']:
        logger.info(
            'Post created: {} {} (ID: {}) by {}'.format(post.title, post.updated, post.id, post.user))
    else:
        logger.info('Post updated: {} {} (ID: {}) by {}'.format(post.title, post.updated, post.id, post.user))


@receiver(post_delete, sender=Post)
def log_post_delete_event(sender, **kwargs):
    """ Writes info about deleted post into info log file """
    logger = logging.getLogger(__name__)

    post = kwargs['instance']
    logger.info('Post deleted: {} {} (ID: {}) by {}'.format(post.title, post.updated, post.id, post.user))


# User signals
@receiver(post_save, sender=User)
def log_user_create_update_event(sender, **kwargs):
    """ Writes info about created or updated user into info log file """
    logger = logging.getLogger(__name__)

    user = kwargs['instance']
    if kwargs['created']:
        logger.info('User created: {} {}(ID: {})'.format(user.username, user.email, user.id))
    else:
        logger.info('User updated: {} {}(ID: {})'.format(user.username, user.email, user.id))


@receiver(post_delete, sender=User)
def log_user_delete_event(sender, **kwargs):
    """ Writes info about deleted user into info log file """
    logger = logging.getLogger(__name__)

    user = kwargs['instance']
    logger.info('User deleted: {} {}(ID: {})'.format(user.username, user.email, user.id))
