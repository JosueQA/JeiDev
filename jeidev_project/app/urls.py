from django.urls import path
from .views import AppDownloadView, AppViews, AppPageViews

urlpatterns = [
    path('', AppViews.as_view(), name='app_home'),
    path('<slug:slug>/', AppPageViews.as_view(), name='app'),
    path('download/<int:id>/', AppDownloadView.as_view(), name='app_download'),
] 
        