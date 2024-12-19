from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, CategoryViewSet
from django.conf import settings
from django.conf.urls.static import static
from . import views

router = DefaultRouter()
router.register('transactions', TransactionViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)), 
    path('', views.home, name='home'),  
    path('about/', views.about, name='about'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('add/', views.transaction_add, name='transaction_add'),
]

if settings.DEBUG:  
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
