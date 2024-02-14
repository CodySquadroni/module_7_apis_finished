from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import WatchListVS, StreamPlatformVS, ReviewList, ReviewDetail

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplateform')
router.register('list', WatchListVS, basename='watchlist')

urlpatterns = [
    path('', include(router.urls)),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-details')
]
