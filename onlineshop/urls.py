from django.urls import path
from .import views
urlpatterns = [
    path('users/login/',views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', views.index, name='index'),
     path('users/profile/', views.getUserProfile, name='user-profile'),
    path('products/', views.getProduct, name='Getproducts'),
    path('products/<str:pk>/', views.singleproduct, name='products'),
]