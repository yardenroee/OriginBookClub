from django.urls import path
from .views import BookDetailView, BookUpdateView, BookListView, BookCreateView

urlpatterns = [
    path('', BookListView.as_view(), name="index"),
    path('book/new/', BookCreateView.as_view(), name="add_book"),
    path('book/update/<int:pk>', BookUpdateView.as_view(), name="book_update"),
    path('book/<int:pk>/', BookDetailView.as_view(), name="book_detail")
]