from django.urls import path
from books import views

urlpatterns = [
	path('author/', views.CreateAuthorView.as_view(),), 
	#path('author/<int:id>/', views.RetrieveAuthorsView.as_view(),), 
	#path('book/', views.CreateBookView.as_view(),),
	#path('book/<int:id>/', views.RetrieveBooksView.as_view(),),
]