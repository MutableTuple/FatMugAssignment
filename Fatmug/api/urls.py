from django.urls import path
from . import views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )



urlpatterns = [
    path("", views.getRoutes),
    path("vendors/", views.getVendors),
    path("vendor/<str:pk>/", views.getVendor),
    path("create-vendor/", views.createVendor),
    path("edit-vendor/<str:pk>/", views.editVendor),
    path("delete-vendor/<str:pk>/", views.deleteVendor),
    # po
    path("allpo/", views.getPO),
    path("singlepo/<str:pk>/", views.getSinglePO),
    path("edit-po/<str:pk>/", views.editPO),
    path("create-po/", views.createPO),
    path("delete-po/<str:pk>", views.deletePO),
    # performance metrics
    path("performance-metrics/<str:pk>", views.getPerformanceMetrics),
    
    
    # path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

