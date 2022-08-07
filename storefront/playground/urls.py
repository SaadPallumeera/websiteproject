from django.urls import path
from . import views 

#URLConf
urlpatterns = [
    path('titration/',views.say_hello),
    path('titrations/',views.say_hello,
    path("simple_function/",views.simple_function),
    path("titrations/graph/",views.main_view),
    path("",views.home_view),
    path("molMass/",views.molMass_view),
    path("molMass/answer/",views.molMass_answer), 
    path("GtoM/",views.GtoM_view),
    path("GtoM/answer/",views.GtoM_answer),
    path("MtoG/",views.MtoG_view),
    path("MtoG/answer/",views.MtoG_answer),
    path("HH/",views.HH_view),
    path("HH/answer/",views.HH_answer),
    path("electrolysis/",views.electrolysis_view),
    path("electrolysis/answer/",views.electrolysis_answer),
    path('Ecell/',views.Ecell_view),
    path("Ecell/answer/",views.Ecell_answer),
    path("Gas/",views.Gas_view),
    path("Gas/answer/",views.Gas_answer),
    path("Pmass/",views.percentMass_view),
    path("Pmass/answer/",views.percentMass_answer),
    path("Geq/",views.Geq_view),
    path("Geq/answer/",views.Geq_ans),
    path("RR/",views.RR_view),
    path("RR/answer/",views.RR_answer),
    path("IRL/",views.IRL_view),
    path("IRL/answer/",views.IRL_answer)
]
