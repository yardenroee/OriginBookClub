from django.urls import path
from .views import BookDetailView, BookUpdateView, BookListView, BookCreateView, BookDeleteView

urlpatterns = [
    path('', BookListView.as_view(), name="index"),
    path('book/new/', BookCreateView.as_view(), name="add_book"),
    path('book/<int:pk>/update', BookUpdateView.as_view(), name="book_update"),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name="book_delete"),
    path('book/<int:pk>/', BookDetailView.as_view(), name="book_detail"),
]