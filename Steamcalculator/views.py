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

from allplot import allplot

from check import checkinput2T
from check import checkinput2P
from check import Input1range

import numpy as np
import pandas as pd


def home(request):

    return render(request, 'home.html')


def count(request):

    values=[0,0,0,0,0,0,0,0,0]

# Input 1: Pressure or Temperature
    Input1=str(request.GET['Input1'])
# Input 2: volume, enthalpy, entropy...
    Input2=str(request.GET['Input2'])
    error=False
    Input1value=request.GET['Input1value']
    Input2value=request.GET['Input2value']
    try:
        Input1value = float(Input1value)
    except ValueError:
        error=True
    #except ValueError:
    #    error==True
    try:
        Input2value = float(Input2value)
    except ValueError:
        error=True

    print(error)

    if error==False:
        if  Input2value < 0:
            error=True
    if error==False:
        error=Input1range(Input1,Input1value)
    if error==False and Input1=='Temperature':
        error=checkinput2T(Input1value,Input2,Input2value)
    if error==False and Input1=='Pressure':
        error=checkinput2P(Input1value,Input2,Input2value)


    if error==False:

        if Input1=='Temperature':
            state=Tempsat(Input1value,Input2value,Input2)
            if state=='saturated':
                values=SatCalcT(Input1value,Input2value,Input2)
            elif state=='unsaturated':
                values=unSatCalcT(Input1value,Input2value,Input2)

        elif Input1=='Pressure' :
            state=Presssat(Input1value,Input2value,Input2)
            if state=='saturated':
                values=SatCalcP(Input1value,Input2value,Input2)
            elif state=='unsaturated':
                values=unSatCalcP(Input1value,Input2value,Input2)

        Pvalue=values[0]
        Tvalue=values[1]
        vvalue=values[2]
        hvalue=values[4]
        svalue=values[5]

        [graphic,graphic2, graphic3, graphic4]= allplot(Pvalue,Tvalue,vvalue,hvalue,svalue)



    if error==True:
        return render(request,'error.html')
    if error==False:
        return render(request,'count.html',{
        'state':state,
        'Temperature':format(values[1],'.5g'),
        'Pressure':format(values[0],'.5g'),
        'volume':format(values[2],'.5g'),
        'Internalenergy':format(values[3],'.5g'),
        'Enthalpy': format(values[4],'.5g'),
        'Entropy':format(values[5],'.5g'),
        'Dryness':format(values[6],'.5g'),
        'Input1':Input1,
        'Input2':Input2,
        'graphic':graphic,
        'graphic2':graphic2,
        'graphic3':graphic3,
        'graphic4':graphic4,
        'error':error

        })
