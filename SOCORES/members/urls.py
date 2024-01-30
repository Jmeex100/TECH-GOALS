from django.urls import path
from .import views

urlpatterns = [
    path('', views.Login_page , name="members")
]



#https://apiv3.apifootball.com/?action=get_events&league_id=149&from=2024-01-11&to=2024-01-11&APIkey=8556a506a91c36c8d01cb75da97f1eb4c5ffaa899c31d39d4a5c2a2e13800faf