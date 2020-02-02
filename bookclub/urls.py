from django.urls import path, re_path
from .views import BookDetailView, BookUpdateView, BookListView, BookCreateView, BookDeleteView, SearchListView
from users.views import FavoriteListView

urlpatterns = [
    path('', BookListView.as_view(), name="index"),
    re_path('search', SearchListView.as_view(), name="search"),
    path('book/new/', BookCreateView.as_view(), name="add_book"),
    path('book/<int:pk>/update', BookUpdateView.as_view(), name="book_update"),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name="book_delete"),
    path('book/<int:pk>/', BookDetailView.as_view(), name="book_detail"),
    path('favorites/', FavoriteListView.as_view(), name="favorites")
]