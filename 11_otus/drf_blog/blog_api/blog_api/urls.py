from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from posts import views as posts_views


router = DefaultRouter()
router.register(r'posts', posts_views.PostViewSet)
router.register(r'tags', posts_views.TagViewSet)

urlpatterns = [
	url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]