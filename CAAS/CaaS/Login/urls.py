from django.urls import path
from .import views
from django.views.generic import TemplateView

app_name = 'Login'
urlpatterns = [
    path('', views.user_login, name='CaaS-Login'),
    path('login/', views.user_login, name='CaaS-Login'),
    path('register/', views.user_register, name='CaaS-Register'),
    path('home/', views.home_view, name='CaaS-HomePage'),
    path('ssc/', views.ssc_view, name='CaaS-SSC'),

    path('logout/', views.logout_view, name='CaaS-Logout'),
    # path('ssc/', TemplateView.as_view(template_name="dashboard/ssc.html")),
]