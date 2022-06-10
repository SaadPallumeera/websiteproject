from django.shortcuts import render
from django.http import HttpResponse
import requests
import matplotlib.pyplot as plt
from .utils import get_plot, titrationS, Chemistry

l1 = []


# Create your views here.
def button(request):
    return(render(request,'hello.html'))

def say_hello(request):
    data = requests.get("https://regres.in/api/users")
    print(data.text)
    data = data.text
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




