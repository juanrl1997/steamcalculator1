import sys
from django.http import HttpResponse
from django.shortcuts import render

sys.path.insert(0,'/Users/juanrodriguezlacasa/Documents/Imperial/ME4/FYP/Project/February/Steamcalculator-project/Steamcalculator')

from compute import Tempsat
from compute import Presssat
from SatCalc import SatCalcT
from SatCalc import SatCalcP

def home(request):
    return render(request,'home.html')

def count(request):


    Input1=str(request.GET['Input1'])
    Input2=str(request.GET['Input2'])

    Input1value = request.GET['Input1value']
    Input2value=request.GET['Input2value']

    if Input1=='Pressure':
        state=Tempsat(Input1value,Input2value)
        values=SatCalcT(Input1value,Input2value)

    elif Input1=='Temperature':
        state=Presssat(Input1value,Input2value)
        values=SatCalcP(Input1value,Input2value)

    return render(request,'count.html',{'state':state,'Temperature':values[1],'Pressure':values[0],
    'volume':values[2],'Internalenergy':values[3],'Enthalpy':values[4], 'Entropy':values[5],
    'Dryness':values[6],'Input1':Input1,'Input2':Input2})
