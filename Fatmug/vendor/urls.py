
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.Home, name="home" ),
    path('trackvendor/<str:pk>', views.trackVendor, name="track-vendor" ),
    path('addvendor/', views.addVendor, name="add-vendor" ),
    path('allpo/', views.allPo, name="all-po" ),
    path('vendor-performance-evaluation/<str:pk>/', views.vendorPerformace, name="vendor-performance" ),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
