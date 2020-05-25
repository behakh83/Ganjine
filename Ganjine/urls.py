from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views
from rest_framework.authtoken import views as rest_view

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'collections', views.CollectionViewSet)
router.register(r'question', views.QuestionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/test/', views.test_connection),
    path('api/v1/collections-count/', views.collection_count),
    path('api/v1/about-us/', views.about_us),
    path('api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/api-token-auth/', rest_view.obtain_auth_token)
]