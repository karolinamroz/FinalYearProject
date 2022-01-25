from django.urls import path, include
from races import views

urlpatterns = (
    path('latest-races/', views.LatestRacesList.as_view()),
    path('races/search/', views.search),
    path('races/<slug:category_slug>/<slug:race_slug>/', views.RacesDetail.as_view()),
    path('races/<slug:category_slug>/', views.CategoryDetail.as_view()),

)