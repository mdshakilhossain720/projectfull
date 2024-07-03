from django.urls import path
from Shop import views
from django.conf import settings
from django.conf.urls.static import static
from .forms import loginForm
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.ProductView.as_view(),name='ProductView'),
    path('product-detail/<int:pk>/', views. ProductDetails.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('lehenga/', views.lehenga, name='lehenga'),
    path('lehenga/<slug:data>/', views.lehenga, name='lehengaitems'),
    path('login/', views.login, name='login'),
    path('accoutn/login/',auth_views.LoginView().as_view(template_name='Shop/login.html',authentication_form=LoginForm),name='login'),
    path('registration/',views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)