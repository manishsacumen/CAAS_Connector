from django.urls import path
from  .save_views import SaveJiraView
from .import views


urlpatterns = [
    path('save_jira/', SaveJiraView.as_view()),
    path('jira_register/', views.jira_register, name='jira-register') ,
]