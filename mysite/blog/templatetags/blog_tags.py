from django import template
from django.utils.safestring import mark_safe
from blog.models import Post
import markdown


register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog\post\latest_posts.html')
def show_latest_posts(count=3):
    latest_posts = Post.published.all()[:count]
    return {'latest_posts': latest_posts}


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
