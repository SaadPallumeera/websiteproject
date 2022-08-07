from hashlib import shake_128
from multiprocessing.sharedctypes import Value
from django.shortcuts import render
from django.http import HttpResponse
import requests
import matplotlib.pyplot as plt
from .utils import get_plot, titrationS, Chemistry
import math


l1 = []


# Create your views here.
def button(request):
    return(render(request,'hello.html'))

def say_hello(request):
    return render(request,'hello.html',{'data':data})
    
def simple_function(request):
    print("\nThis is a simple function\n")
  #  return(HttpResponse("""<html><script>window.location.replace('/');<script></html>"""))
    inp = request.GET.get('username')
   # inp2 = request.GET.get("password")
   # jake = "hello"
   # inp = 'boy'

    return(HttpResponse(inp))

def main_view(request):

    x = float(request.GET.get('volAcid'))
    y = float(request.GET.get('Macid'))
    z = float(request.GET.get('Mbase'))
    chart = titrationS(float(y),float(x),float(z))
    return render(request,'graph.html',{'chart':chart,'x':x})

def home_view(request):
    return(render(request,'home.html'))

def molMass_view(request):
    return(render(request,'MolMass.html'))

def molMass_answer(request):
    form = str(request.GET.get('formula'))
    x=Chemistry.mm(form)
    return(render(request,'molMassAns.html',{'mass':x,'formula':form}))

def GtoM_view(request):
    return(render(request,'GtoM.html'))

def GtoM_answer(request):
    form = str(request.GET.get('formula'))
    gram = float(request.GET.get('grams'))
    mol = round(gram/Chemistry.mm(form),5)
    return(render(request,'GtoMAns.html',{'formula':form,'gram':gram,'mol':mol }))

def MtoG_view(request):
    return(render(request,'MtoG.html'))

def MtoG_answer(request):
    form = str(request.GET.get('formula'))
    mol = float(request.GET.get('moles'))
    gram = round(mol*Chemistry.mm(form),5)
    return(render(request,'MtoGAns.html',{'formula':form,'gram':gram,'mol':mol}))

def HH_view(request):
    return(render(request,'HH.html'))

def HH_answer(request):
    Pka = float(request.GET.get('Pka'))
    acid = float(request.GET.get('acid'))
    base = float(request.GET.get('base'))
    Ph = Pka + math.log(base/acid,10)
    Ph = round(Ph,2)
    return(render(request,'HH_ans.html',{'Ph':Ph}))

def electrolysis_view(request):
    return(render(request,'electrolysis.html'))

def electrolysis_answer(request):
    moles = float(request.GET.get('moles'))
    time = float(request.GET.get('time'))
    amps = float(request.GET.get('amps'))
    electrons = float(request.GET.get('charge'))
    ans = 0
    answer = ""
    if(moles == 0):
        ans = ((amps * time)/(96485*electrons))
        ans = str(round(ans,4))
        answer = ans + " amount of moles will be produced"
    if (time == 0):
        ans = ((moles *96485 * electrons)/(amps))
        ans = str(round(ans,4))
        answer = "It will take " + ans + " seconds"
    if (amps == 0):
        ans = ((moles *96485 * electrons)/(time))
        ans = str(round(ans,4))
        answer = "It will require " + ans + " amps"
    if (electrons == 0):
        ans = ((moles *96485)/(time*amps))
        ans = str(round(ans,4))
        answer = "The electrons gained/lost per atom is " + ans
    
    return(render(request,'electrolysis_answer.html',{'answer':answer}))

def Ecell_view(request):
    return(render(request,'Ecell.html'))

def Ecell_answer(request):
    s1=float(request.GET.get('s1'))
    s2=float(request.GET.get('s2'))
    q=float(request.GET.get('q'))
    t=float(request.GET.get('t'))
    n =float(request.GET.get('n'))
    ans = s1-s2+((8.314)*(t)/((n)*96485))*(math.log(q))
    return(render(request,'Ecell_answer.html',{'ans':ans}))

def Gas_view(request):
    return(render(request,'Gas.html'))

def Gas_answer(request):
    pressure = float(request.GET.get('p'))
    unit = str(request.GET.get('u'))
    volume = float(request.GET.get('v'))
    temperature = float(request.GET.get('t'))
    n = float(request.GET.get('n'))
    multiply = 1
    un = "atm"
    if (unit == "Millimetre(s) of mercury (mmHg)"):
        multiply = 760
        un = "mmHg"
    if (unit == "Kilopascals (kPa)" ):
        multiply = 101.325
        un = "kPa"
    if (pressure == 0):
        ans = n*.082057*temperature/volume
        ans = round(ans * multiply,4)
        answer = "The pressure is " + str(ans) + " " + un
    if (volume == 0):
        ans = n*.082057*temperature/pressure
        ans = round(ans * multiply,4)
        answer = "The volume is "  + str(ans) + " litres"
    if (n==0):
        ans = pressure * volume /(.082057*temperature)
        ans = round(ans * multiply,4)
        answer = "The number of moles is " + str(ans)
    if (temperature == 0):
        ans = pressure * volume /(.082057*pressure)
        ans = round(ans * multiply,4)
        answer = "The temperature is " + str(ans) + " kelvin"
    return(render(request,'Gas_ans.html',{'answer':answer}))

def percentMass_view(request):
    return(render(request,"percentMass.html"))

def percentMass_answer(request):
    form = request.GET.get('formula')
    answer = Chemistry.percentMass(form)
    return(render(request,"percentMass_ans.html",{'answer':answer}))

def Geq_view(request):
    return(render(request,"Geq.html"))

def Geq_ans(request):
    K = float(request.GET.get("K"))
    G = float(request.GET.get("G"))
    T = float(request.GET.get("T"))
    ans = 0
    answer = ""
    if (K == 0):
        ans = 2.71828**(-1*G/(8.314*T))
        answer = "The equilibrium constant is " + str(ans)
    if (G == 0):
        ans = -(8.314)*T*math.log(K)
        answer = "∆G is " + str(ans) + "kJ/mol"
    if ( T == 0):
        ans = -1*G/(8.314*math.log(K))
        answer = "Temperature is " + str(T) + " kelvin"
    return(render(request,"Geq_ans.html",{'answer':answer}))

def RR_view(request):
    return(render(request,"RR.html"))

def RR_answer(request):
    conc = str(request.GET.get("concentration")).split(" ")
    order = str(request.GET.get("order")).split(" ")
    constant = float(request.GET.get("constant"))
    ans = float(constant)
    x=0
    while (x<len(conc)):
        #ans = float(order[x])
        ans = ans *(float(conc[x])**float(order[x]))
        x+=1
    ans = round(ans,5)
    answer = "The Reaction Rate is " + str(ans) + " molar per second "
    return(render(request,"RR_ans.html",{"answer":answer}))

def IRL_view(request):
    return(render(request,"IRL.html"))

def IRL_answer(request):
    conc = float(request.GET.get("concentration"))
    order = str(request.GET.get("order"))
    constant = float(request.GET.get("constant"))
    time = float(request.GET.get("time"))
    ans = 1
    if (order == "0th order"):
        ans = conc - constant*time
    if (order == "1st order"):
        ans = conc * math.e**(-1*constant*time)
    if (order == "2nd order"):
        ans = 1/(1/conc + constant*time)
    if (ans<0):
        ans = 0
    ans = round(ans,5)
    answer = "The concentration after " + str(time) + " seconds is " + str(ans) + " molar"
    return(render(request,"IRL_ans.html",{"ans":answer}))


def error_500(request):
        data = {}
        return render(request,'error_500.html', data)

