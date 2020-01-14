
from django.urls import path
from .import views
from django.views.generic import TemplateView
# from .views import 

urlpatterns = [
    path('ssc/', TemplateView.as_view(template_name="dashboard/ssc.html")),
#     path('save_ssc/', )
 ]