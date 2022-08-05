from rest_framework.routers import DefaultRouter

from book.views import BookViewSet
from book_copy.views import BookCopyViewset
from users.views import UserLibraryViewset

router = DefaultRouter()
router.register(
    "book",
    BookViewSet,
)
router.register("user", UserLibraryViewset)
router.register("book_copy", BookCopyViewset)


urlpatterns = router.urls
