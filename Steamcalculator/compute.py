############### Check is saturated or unsaturated ####################


import numpy as np
import pandas as pd

Pinput=-1
uinput=-1
hinput=-1
sinput=-1
xinput=-1


dfsat=pd.read_csv('/Users/juanrodriguezlacasa/Documents/Imperial/ME4/FYP/Steam/Data.csv')
dfP=pd.read_csv('/Users/juanrodriguezlacasa/Documents/Imperial/ME4/FYP/Steam/dataunsaturated.csv')
csat=dfsat.columns.values.tolist()

def Presssat(Input1value,Input2value):

    subP = dfsat['P'] - Pinput
    subPls=subP.values.tolist()
    m = min(i for i in subP if i >= 0)
    #Row of Pressure is set to the one just above
    rowOfPressure=subPls.index(m)
    PressureHigh=dfsat.loc[rowOfPressure,'P']
    PressureLow=dfsat.loc[rowOfPressure-1,'P']
    ratio=(Pinput-PressureLow)/(PressureHigh-PressureLow)
    #Interpolation of rows
    j=0
    DATA_VALUES=[0,0,0,0,0,0,0,0,0,0,0]
    for i in csat:
        DATA_VALUES[j]=(1-ratio)*dfsat.loc[rowOfPressure-1,i]+ratio*dfsat.loc[rowOfPressure,i]
        j=j+1
    if vinput!=-1:
        if vinput>=DATA_VALUES[2] and vinput<=DATA_VALUES[3]:
            state='saturated'
        else:
            state='unsaturated'
    elif uinput!=-1:
        if uinput>=DATA_VALUES[4] and uinput<=DATA_VALUES[5]:
            state='saturated'
        else:
            state='unsaturated'
    elif hinput!=-1:
        if hinput>=DATA_VALUES[6] and hinput<=DATA_VALUES[8]:
            state='saturated'
        else:
            state='unsaturated'
    elif sinput!=-1:
        if sinput>=DATA_VALUES[9] and sinput<=DATA_VALUES[10]:
            state='saturated'
        else:
            state='unsaturated'
    elif xinput!=-1:
        state='saturated'
    else:
        state='unsaturated'

    return(state)

def Tempsat(Input1value,Input2value):

    Tinput=int(Input1value)
    vinput=int(Input2value)


    Tsat=[0.01, 7, 32.9, 45.8, 60.1, 81.3, 99.6, 100, 120.2, 143.6, 158.8, 170.4, 179.9, 212.4, 233.9,
          250.4, 263.9, 275.6, 285.8, 295, 303.3, 311, 324.7, 336.7, 347.4, 357, 365.7, 373.7]
    dfsat=pd.read_csv('/Users/juanrodriguezlacasa/Documents/Imperial/ME4/FYP/Steam/Data.csv')
    dfP=pd.read_csv('/Users/juanrodriguezlacasa/Documents/Imperial/ME4/FYP/Steam/dataunsaturated.csv')
    csat=dfsat.columns.values.tolist()

    if Tinput>=0.01 and Tinput<=373.95:
        #Find closest value
        subT = dfsat['T'] - Tinput
        subTls=subT.values.tolist()
        m = min(i for i in subT if i >= 0)
        #Row of Temperature is set to the one just above
        rowOfTemperature=subTls.index(m)
        TemperatureHigh=dfsat.loc[rowOfTemperature,'T']
        TemperatureLow=dfsat.loc[rowOfTemperature-1,'T']
        ratio=(Tinput-TemperatureLow)/(TemperatureHigh-TemperatureLow)
        #Interpolation of rows
        j=0
        DATA_VALUES=[0,0,0,0,0,0,0,0,0,0,0]
        for i in csat:
            DATA_VALUES[j]=(1-ratio)*dfsat.loc[rowOfTemperature-1,i]+ratio*dfsat.loc[rowOfTemperature,i]
            j=j+1
        if vinput!=-1:
            if vinput>=DATA_VALUES[2] and vinput<=DATA_VALUES[3]:
                state='saturated'
            else:
                state='unsaturated'
        elif uinput!=-1:
            if uinput>=DATA_VALUES[4] and uinput<=DATA_VALUES[5]:
                state='saturated'
            else:
                state='unsaturated'
        elif hinput!=-1:
            if hinput>=DATA_VALUES[6] and hinput<=DATA_VALUES[8]:
                state='saturated'
            else:
                state='unsaturated'
        elif sinput!=-1:
            if sinput>=DATA_VALUES[9] and sinput<=DATA_VALUES[10]:
                state='saturated'
            else:
                state='unsaturated'
        elif xinput!=-1:
            state='saturated'
        else:
            state='unsaturated'
        return (state)
