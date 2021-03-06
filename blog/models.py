from hitcount.models import HitCount, HitCountMixin
from markdown_deux import markdown
from star_ratings.models import Rating

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from django.db.models.signals import pre_save
from django.contrib.contenttypes.fields import GenericRelation


from .utils import get_read_time


# Create your models here.

# Manage posts to forbide to show drafts and a future publush date
class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


def upload_location(instance, filename):
    return '%s/%s' % (instance.slug, filename)


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Category name')
        )

    class Meta(object):
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Tag name')
        )

    class Meta(object):
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.name


class Post(models.Model, HitCountMixin):
    objects = PostManager()

    class Meta(object):
        ordering = ['-datetime_stamp', '-updated']
        verbose_name_plural = _('Posts')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        verbose_name=_('Category')
        )
    tag = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name=_('Tag'))
    title = models.CharField(
        max_length=80,
        verbose_name=_('Title'))
    slug = models.SlugField(
        unique=True,
        verbose_name=_('Slug URL'))
    image = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
        height_field='height_field',
        width_field='width_field',
        verbose_name=_('Image'))
    height_field = models.PositiveIntegerField(
        null=True,
        default=0,
        verbose_name=_('Height of a field'))
    width_field = models.PositiveIntegerField(
        null=True,
        default=0,
        verbose_name=_('Width of a field'))
    content = models.TextField(
        verbose_name=_('Content'))
    draft = models.BooleanField(
        default=True,
        verbose_name=_('Draft'))
    publish = models.DateField(
        auto_now=False,
        auto_now_add=False,
        verbose_name=_('Publish date'))
    read_time = models.PositiveIntegerField(
        blank=True,
        null=True)
    updated = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name=_('Updated date'))
    datetime_stamp = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        verbose_name=_('Datetime of creation'))
    ratings = GenericRelation(Rating, related_query_name='posts')
    hit_count = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_relation')

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse('posts:posts_detail', kwargs={'slug': self.slug})

    def get_markdown(self):
        content = self.content
        return mark_safe(markdown(content))


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    if instance.content:
        html_string = instance.get_markdown()
        read_time_content = get_read_time(html_string)
        instance.read_time = read_time_content


pre_save.connect(pre_save_post_receiver, sender=Post)
