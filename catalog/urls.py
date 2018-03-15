from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
	path('dancers/', views.DancerListView.as_view(), name='dancers'),
    path('dancer/<int:pk>', views.DancerDetailView.as_view(), name='dancer-detail'),
	path('coaches/', views.CoachListView.as_view(), name='coaches'),
	path('coach/<int:pk>', views.CoachDetailView.as_view(), name='coach-detail'),
]