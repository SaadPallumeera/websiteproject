from django.urls import path
from . import views 

#URLConf
urlpatterns = [
    path('titration/',views.say_hello),
    path("simple_function/",views.simple_function),
    path("titration/graph/",views.main_view),
    path("",views.home_view),
    path("molMass/",views.molMass_view),
    path("molMass/answer/",views.molMass_answer) 
]