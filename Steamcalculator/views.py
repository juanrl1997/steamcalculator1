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

from plots import Pvplot
from plots import Phplot
from plots import Tsplot
from plots import Hsplot

import numpy as np
import pandas as pd

from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np


def home(request):

    return render(request, 'home.html')


def count(request):



    values=[0,0,0,0,0,0,0,0,0]


# Input 1: Pressure or Temperature
    Input1=str(request.GET['Input1'])

# Input 2: volume, enthalpy, entropy...
    Input2=str(request.GET['Input2'])

    Input1value = request.GET['Input1value']
    Input2value = request.GET['Input2value']

    print(Input2)

    print(Input2value)

    #state=Presssat(Input1value,Input2value,Input2)
    #values=SatCalcT(Input1value,Input2value,Input2)

    if Input1=='Temperature':
        state=Tempsat(Input1value,Input2value,Input2)
        print(state)
        if state=='saturated':
            print('run')

            values=SatCalcT(Input1value,Input2value,Input2)
        elif state=='unsaturated':
            values=unSatCalcT(Input1value,Input2value,Input2)

    elif Input1=='Pressure':
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


# plot 1
    Pvplot(Pvalue,vvalue)


    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
# plot 2
    Phplot(Pvalue,hvalue)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic2 = base64.b64encode(image_png)
    graphic2 = graphic2.decode('utf-8')
# plot 3
    Tsplot(Tvalue,svalue)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic3 = base64.b64encode(image_png)
    graphic3 = graphic3.decode('utf-8')

# plot 4
    Hsplot(hvalue,svalue)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic4 = base64.b64encode(image_png)
    graphic4 = graphic4.decode('utf-8')


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
    'graphic4':graphic4

    })
