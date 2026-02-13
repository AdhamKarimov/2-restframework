from rest_framework import routers

from project.views import ProjectViewSet

router = routers.SimpleRouter()
router.register(r'project_view_set', ProjectViewSet)
urlpatterns = router.urls