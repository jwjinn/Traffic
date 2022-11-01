from django.urls import path
from . import views

from plotting.dash_apps import app1, app2, app3, TimeToWork, RoadSpecific, RoadOverall, RoadByYear, subway0, subway1, subway2, subway3





urlpatterns = [
    path('', views.index, name = 'index'),

    #Dashboard: 간단하게 표현할때, 사용 가장 간편하고 흥미위주로
    path('dashboard/', views.dashboard, name = 'dashboard'),

    path('seoulIndex/', views.seoulIndex, name = 'seoulIndex'),

    path('roadTraffic/', views.roadTraffic, name='roadTraffic'),

    path('bus/', views.bus, name='bus'),

    path('subway/', views.subway, name='subway'),

]