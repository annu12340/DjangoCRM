from django.urls import path,include
from . import views

app_name="leads"

urlpatterns = [
    path('',  views.lead_list),
    path('create/',  views.lead_create),
    path('<int:pk>/',  views.lead_detail),

]


