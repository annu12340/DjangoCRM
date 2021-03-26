from django.urls import path,include
from . import views

app_name="leads"

urlpatterns = [
    path('',views.landing_page),
    path('register/',views.register),
    path('login',views.loginPage),


    path('all/',  views.lead_list),
    path('create/',  views.lead_create),
    path('<int:pk>/',  views.lead_detail),
    path('<int:pk>/update/',  views.lead_update),
    path('<int:pk>/delete/',  views.lead_delete),

]


