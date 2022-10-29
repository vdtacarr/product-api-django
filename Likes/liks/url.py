from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('quotes', views.QuoteViewSet, basename='quotes')
router.register('quoteusers', views.QuoteUserViewSet, basename='quoteusers')
router.register('user', views.UserViewSet, basename="users")
urlpatterns = [
    path('', include(router.urls)),
    path('custom', views.custom)
]