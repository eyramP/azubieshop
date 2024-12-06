from rest_framework.urls import path
from . import views

urlpatterns = [
    path('admin/register/', view=views.RegisterAdminUserView.as_view(), name='register_admin_account'),
    path('admin/login/', view=views.AdminLoginView.as_view(), name='admin_login'),
    path('register/', view=views.RegisterUserView.as_view(), name='register_admin_account'),
    path('login/', view=views.UserLoginView.as_view(), name='user_login'),
]
