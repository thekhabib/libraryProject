from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BooksListApiView, BookDetailApiView, \
    BookCreateApiView, BookDeleteApiView, BookUpdateApiView, \
    BookViewSet


router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    # path('books/', BooksListApiView.as_view(), name='books_list'),
    # path('books/<int:pk>/', BookDetailApiView.as_view(), name='book_detail'),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view(), name='book_update'),
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view(), name='book_delete'),
    # path('books/create/', BookCreateApiView.as_view(), name='book_create'),
]

urlpatterns = urlpatterns + router.urls
