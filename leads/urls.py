from django.urls import path,include
from . import views

app_name="leads"

urlpatterns = [
    path('',  views.lead_list),
    path('<pk>/',  views.lead_detail),
]


