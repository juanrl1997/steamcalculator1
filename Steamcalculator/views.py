import sys
from django.http import HttpResponse
from django.shortcuts import render

sys.path.insert(0,'/Users/juanrodriguezlacasa/Documents/Imperial/ME4/FYP/Project/February/Steamcalculator-project/Steamcalculator')

from compute import Tempsat
from compute import Presssat
from SatCalc import SatCalcT
from SatCalc import SatCalcP
from unSatCalc import unSatCalcP
from unSatCalc import unSatCalcT

import numpy as np
import pandas as pd

def home(request):
    return render(request,'home.html')
    print('hello')

def count(request):
    state='BLABLA'


    values=[0,0,0,0,0,0,0,0,0]


# Input 1: Pressure or Temperature
    Input1=str(request.GET['Input1'])

# Input 2: volume, enthalpy, entropy...
    Input2=str(request.GET['Input2'])

    Input1value = request.GET['Input1value']
    Input2value = request.GET['Input2value']
    print(Input1value)
    print(Input2value)


    #state=Presssat(Input1value,Input2value,Input2)
    #values=SatCalcT(Input1value,Input2value,Input2)

    if Input1=='Temperature':
        state=Tempsat(Input1value,Input2value,Input2)
        if state=='saturated':
            values=SatCalcT(Input1value,Input2value,Input2)
        elif state=='unsaturated':
            values=unSatCalcT(Input1value,Input2value,Input2)

    elif Input1=='Pressure':
        state=Presssat(Input1value,Input2value,Input2)
        print(state)
        if state=='saturated':
            values=SatCalcP(Input1value,Input2value,Input2)
        elif state=='unsaturated':
            values=unSatCalcP(Input1value,Input2value,Input2)



    return render(request,'count.html',{'state':state,'Temperature':values[1],'Pressure':values[0],
    'volume':values[2],'Internalenergy':values[3],'Enthalpy':values[4], 'Entropy':values[5],
    'Dryness':values[6],'Input1':Input1,'Input2':Input2})
