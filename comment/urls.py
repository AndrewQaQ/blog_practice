from django.conf.urls import url
from . import views
app_name = 'comment'

urlpatterns = [
	url(r'^post-comment/(?P<article_id>[0-9]+)', views.post_comment, name='post_comment'),
]