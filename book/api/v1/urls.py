from rest_framework.routers import DefaultRouter
from book.views import BookViewSet

router = DefaultRouter()
router.register("book", BookViewSet)


urlpatterns = router.urls
