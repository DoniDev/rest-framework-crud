from django.urls import path
from .views import BookAPIView, BookRetrieveView, BookCreateAPIView, BookUpdateAPIView, BookDestroyView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', BookAPIView.as_view()),
    path('book/<int:id>/', BookRetrieveView.as_view()),
    path('book/create/', BookCreateAPIView.as_view()),
    path('book/<int:id>/retrieve', BookUpdateAPIView.as_view()),
    path('book/<int:id>/destroy', BookDestroyView.as_view()),
    path('book/<int:id>/all/', BookRetrieveUpdateDestroyAPIView.as_view()),
]

