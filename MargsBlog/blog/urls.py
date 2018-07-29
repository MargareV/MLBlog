from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . feeds import LatestPostsFeed

urlpatterns = [
   path('', views.post_list, name='post_list'),
   path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
   # path('', views.PostListView.as_view(), name='post_list'),
   re_path(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<post>[\w-]+)/$', views.post_detail, name='post_detail'),
   path('<int:post_id>/share/', views.post_share, name='post_share'),
   path('feed/', LatestPostsFeed(), name="post_feed"),
   path('search/', views.post_search, name="post_search"),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)