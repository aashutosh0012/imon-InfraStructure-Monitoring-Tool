from django.urls import include, path
from rest_framework import routers
from api.views import ServerViewSet, DatabaseViewSet
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'servers', ServerViewSet)
router.register(r'databases', DatabaseViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

# REST framework's login and logout views for browsable API
urlpatterns += [
    # path('api-auth/', include('rest_framework.urls'))
]
