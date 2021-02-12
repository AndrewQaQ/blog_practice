"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
app_name = 'article'
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^article-list/', views.article_list, name='article_list'),
    url(r'^article-detail/(?P<id>[0-9]+)/', views.article_detail, name='article_detail'),
    url(r'^article-create/', views.article_create, name='article_create'),
    url(r'^article-safe-delete/(?P<id>[0-9]+)/', views.article_safe_delete, name='article_safe_delete'),
    url(r'^article-update/(?P<id>[0-9]+)/', views.article_update, name='article_update'),
]