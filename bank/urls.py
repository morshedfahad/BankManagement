
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('home/', views.staff_home, name='staff_home' ),
    path('register_customer/', views.register_customer, name='register_customer'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('transfer_money/', views.transfer_money, name='transfer_money'),
    path('statement/', views.statement, name='statement' ),
]