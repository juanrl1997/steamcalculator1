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

import numpy as np
import pandas as pd



import io
import matplotlib.pyplot as plt
import numpy as np


from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np



def home(request):
    Pvplot()


    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'home.html',{'graphic':graphic})


def count(request):



    values=[0,0,0,0,0,0,0,0,0]


# Input 1: Pressure or Temperature
    Input1=str(request.GET['Input1'])

# Input 2: volume, enthalpy, entropy...
    Input2=str(request.GET['Input2'])

    Input1value = request.GET['Input1value']
    Input2value = request.GET['Input2value']
    print(Input1)
    print(Input2)

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
