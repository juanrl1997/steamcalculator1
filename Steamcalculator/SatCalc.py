############ Saturation Calculation ###########



import numpy as np
import pandas as pd



def SatCalcP(Input1value,Input2value,Input2):

    Pinput=-1
    Tinput=-1
    uinput=-1
    vinput=-1
    hinput=-1
    sinput=-1
    xinput=-1

    dfsat=pd.read_csv('/Users/juanrodriguezlacasa/Documents/Imperial/ME4/FYP/Steam/Data.csv')
    dfP=pd.read_csv('/Users/juanrodriguezlacasa/Documents/Imperial/ME4/FYP/Steam/dataunsaturated.csv')
    csat=dfsat.columns.values.tolist()

    if Input2=='volume':
        vinput=float(Input2value)
    elif Input2=='Enthalpy':
        hinput=float(Input2value)
    elif Input2=='Entropy':
        sinput=float(Input2value)
    elif Input2=='Internalenergy':
        uinput=float(Input2value)
    elif Input2=='Dryness':
        xinput=float(Input2value)


    Pinput=float(Input1value)

    #Find closest value
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
        vL=DATA_VALUES[2]
        vH=DATA_VALUES[3]
        x=(vinput-vL)/(vH-vL)
        u=x*DATA_VALUES[4]+(1-x)*DATA_VALUES[5]
        h=x*DATA_VALUES[6]+(1-x)*DATA_VALUES[8]
        s=x*DATA_VALUES[9]+(1-x)*DATA_VALUES[10]
        T=DATA_VALUES[1]
        P=DATA_VALUES[0]
        v=vinput
    if uinput!=-1:
        uL=DATA_VALUES[4]
        uH=DATA_VALUES[5]
        x=(uinput-uL)/(uH-uL)
        v=x*DATA_VALUES[2]+(1-x)*DATA_VALUES[3]
        h=x*DATA_VALUES[6]+(1-x)*DATA_VALUES[8]
        s=x*DATA_VALUES[9]+(1-x)*DATA_VALUES[10]
        T=DATA_VALUES[1]
        P=DATA_VALUES[0]
        u=uinput
    if hinput!=-1:
        hL=DATA_VALUES[6]
        hH=DATA_VALUES[8]
        x=(hinput-hL)/(hH-hL)
        v=x*DATA_VALUES[2]+(1-x)*DATA_VALUES[3]
        u=x*DATA_VALUES[4]+(1-x)*DATA_VALUES[5]
        s=x*DATA_VALUES[9]+(1-x)*DATA_VALUES[10]
        T=DATA_VALUES[1]
        P=DATA_VALUES[0]
        h=hinput
    if sinput!=-1:
        sL=DATA_VALUES[9]
        sH=DATA_VALUES[10]
        x=(sinput-sL)/(sH-sL)
        v=x*DATA_VALUES[2]+(1-x)*DATA_VALUES[3]
        u=x*DATA_VALUES[4]+(1-x)*DATA_VALUES[5]
        h=x*DATA_VALUES[6]+(1-x)*DATA_VALUES[8]
        T=DATA_VALUES[1]
        P=DATA_VALUES[0]
        s=sinput
    if xinput !=-1:
        v=xinput*DATA_VALUES[2]+(1-xinput)*DATA_VALUES[3]
        u=xinput*DATA_VALUES[4]+(1-xinput)*DATA_VALUES[5]
        h=xinput*DATA_VALUES[6]+(1-xinput)*DATA_VALUES[8]
        s=xinput*DATA_VALUES[9]+(1-xinput)*DATA_VALUES[10]
        T=DATA_VALUES[1]
        P=DATA_VALUES[0]

    return[P,T,v,u,h,s,x]



def SatCalcT(Input1value,Input2value,Input2):

    Pinput=-1
    Tinput=-1
    uinput=-1
    vinput=-1
    hinput=-1
    sinput=-1
    xinput=-1

    dfsat=pd.read_csv('/Users/juanrodriguezlacasa/Documents/Imperial/ME4/FYP/Steam/Data.csv')
    dfP=pd.read_csv('/Users/juanrodriguezlacasa/Documents/Imperial/ME4/FYP/Steam/dataunsaturated.csv')
    csat=dfsat.columns.values.tolist()

    if Input2=='volume':
        vinput=int(Input2value)
    elif Input2=='Enthalpy':
        hinput=int(Input2value)
    elif Input2=='Entropy':
        sinput=int(Input2value)
    elif Input2=='Internalenergy':
        uinput=int(Input2value)
    elif Input2=='Dryness':
        xinput=int(Input2value)

    Tinput=int(Input1value)

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
        vL=DATA_VALUES[2]
        vH=DATA_VALUES[3]
        x=(vinput-vL)/(vH-vL)
        u=x*DATA_VALUES[4]+(1-x)*DATA_VALUES[5]
        h=x*DATA_VALUES[6]+(1-x)*DATA_VALUES[8]
        s=x*DATA_VALUES[9]+(1-x)*DATA_VALUES[10]
        T=DATA_VALUES[1]
        P=DATA_VALUES[0]
        v=vinput
    if uinput!=-1:
        uL=DATA_VALUES[4]
        uH=DATA_VALUES[5]
        x=(uinput-uL)/(uH-uL)
        v=x*DATA_VALUES[2]+(1-x)*DATA_VALUES[3]
        h=x*DATA_VALUES[6]+(1-x)*DATA_VALUES[8]
        s=x*DATA_VALUES[9]+(1-x)*DATA_VALUES[10]
        T=DATA_VALUES[1]
        P=DATA_VALUES[0]
        u=uinput
    if hinput!=-1:
        hL=DATA_VALUES[6]
        hH=DATA_VALUES[8]
        x=(hinput-hL)/(hH-hL)
        v=x*DATA_VALUES[2]+(1-x)*DATA_VALUES[3]
        u=x*DATA_VALUES[4]+(1-x)*DATA_VALUES[5]
        s=x*DATA_VALUES[9]+(1-x)*DATA_VALUES[10]
        T=DATA_VALUES[1]
        P=DATA_VALUES[0]
        h=hinput
    if sinput!=-1:
        sL=DATA_VALUES[9]
        sH=DATA_VALUES[10]
        x=(sinput-sL)/(sH-sL)
        v=x*DATA_VALUES[2]+(1-x)*DATA_VALUES[3]
        u=x*DATA_VALUES[4]+(1-x)*DATA_VALUES[5]
        h=x*DATA_VALUES[6]+(1-x)*DATA_VALUES[8]
        T=DATA_VALUES[1]
        P=DATA_VALUES[0]
        s=sinput
    if xinput !=-1:
        v=xinput*DATA_VALUES[2]+(1-xinput)*DATA_VALUES[3]
        u=xinput*DATA_VALUES[4]+(1-xinput)*DATA_VALUES[5]
        h=xinput*DATA_VALUES[6]+(1-xinput)*DATA_VALUES[8]
        s=xinput*DATA_VALUES[9]+(1-xinput)*DATA_VALUES[10]
        T=DATA_VALUES[1]
        P=DATA_VALUES[0]
        x=xinput

        return[P,T,v,u,h,s,x]
