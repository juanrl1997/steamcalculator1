import numpy as np
import pandas as pd
from valuesetter import value2setter



def Input1range(Input1,Input1value):
    standbyerror=False
    if Input1=='Temperature':
        if Input1value < 0.01 or Input1value > 800:
            standbyerror = True
    if Input1=='Pressure':
        if Input1value < 0.00617 or Input1value > 1000:
            standbyerror = True
    return(standbyerror)


def checkinput2T(Input1value,Input2,Input2value):

    df = pd.read_csv('/Users/juanrodriguezlacasa/Documents/Imperial/ME4/FYP/Steam/dataunsaturated.csv')
    c=df.columns.values.tolist()

    Tinput=float(Input1value)
    [vinput,uinput,hinput,sinput,xinput]=value2setter(Input2,Input2value)


    df=df.sort_values(by=['T','P'])
    df=df.reset_index(drop=True)

    #If input is P and v
    #Creating an array of only P values / no duplicates
    T=df['T'].drop_duplicates()

    #Create list of only Ps
    Tls=T.tolist()

    #Find closest row to the P value
    subT=T-Tinput
    subTls=subT.values.tolist()
    m = float(min(i for i in subT if i >= 0))

    #row of pressure within the no duplicates pressure array
    rowOfTemperature=subTls.index(m)
    TemperatureHigh=Tls[rowOfTemperature]
    TemperatureLow=Tls[rowOfTemperature-1]
    ratioT=(Tinput-TemperatureLow)/(TemperatureHigh-TemperatureLow)

    zeros=np.zeros((36,6))
    rowH=rowOfTemperature*36
    rowL=(rowOfTemperature-1)*36

    print(rowH,rowL)

    #storing values of Highpressure Data
    column=-1
    DATA_VALUESHIGH=np.zeros((36,6))
    for i in c:
        column=column+1
        for j in range(0,36):
            DATA_VALUESHIGH[j,column]=df.loc[rowH+j,i]


    #storing values of Highpressure Data
    column=-1
    DATA_VALUESLOW=np.zeros((36,6))
    for i in c:
        column=column+1
        for j in range(0,36):
            DATA_VALUESLOW[j,column]=df.loc[rowL+j,i]


    if vinput!=-1:
        #Calculate values at precise position of Pressure
        DATA_VALUES=ratioT*DATA_VALUESHIGH+(1-ratioT)*DATA_VALUESLOW
        #lookup v
        v=DATA_VALUES[:,2]
        subv=v-vinput
        subvls=subv.tolist()

        try :
            n = min(i for i in subv if i >= 0)
            rowOfv=subvls.index(n)
            vHigh=v[rowOfv]
            vLow=v[rowOfv-1]
            ratiov=(vinput-vLow)/(vHigh-vLow)
            standbyerror=False


        except ValueError:
            print('raaan')
            standbyerror=True

    if uinput!=-1:
        #Calculate values at precise position of Pressure
        DATA_VALUES=ratioT*DATA_VALUESHIGH+(1-ratioT)*DATA_VALUESLOW
        #lookup v
        u=DATA_VALUES[:,3]
        subu=u-uinput
        subuls=subu.tolist()

        try :
            n = min(i for i in subu if i >= 0)
            rowOfu=subuls.index(n)
            uHigh=u[rowOfu]
            uLow=u[rowOfu-1]
            ratiou=(uinput-uLow)/(uHigh-uLow)
            standbyerror=False

        except ValueError:
            print('raaan')
            standbyerror=True

    if hinput!=-1:
        #Calculate values at precise position of Pressure
        DATA_VALUES=ratioT*DATA_VALUESHIGH+(1-ratioT)*DATA_VALUESLOW
        #lookup v
        h=DATA_VALUES[:,4]
        subh=h-hinput
        subhls=subh.tolist()

        try :
            n = min(i for i in subh if i >= 0)
            rowOfh=subhls.index(n)
            hHigh=h[rowOfh]
            hLow=h[rowOfh-1]
            ratioh=(hinput-hLow)/(hHigh-hLow)
            standbyerror=False


        except ValueError:
            print('raaan')
            standbyerror=True


    if sinput!=-1:
        #Calculate values at precise position of Pressure
        DATA_VALUES=ratioT*DATA_VALUESHIGH+(1-ratioT)*DATA_VALUESLOW
        #lookup v
        s=DATA_VALUES[:,5]
        subs=s-sinput
        subsls=subs.tolist()

        try :
            n = min(i for i in subs if i >= 0)
            rowOfs=subsls.index(n)
            sHigh=s[rowOfs]
            sLow=s[rowOfs-1]
            ratios=(sinput-sLow)/(sHigh-sLow)
            standbyerror=False


        except ValueError:
            print('raaan')
            standbyerror=True

    return(standbyerror)

def checkinput2P(Input1value,Input2,Input2value):
    df = pd.read_csv('/Users/juanrodriguezlacasa/Documents/Imperial/ME4/FYP/Steam/dataunsaturated.csv')
    c=df.columns.values.tolist()
    Pinput=float(Input1value)
    [vinput,uinput,hinput,sinput,xinput]=value2setter(Input2,Input2value)

    df=df.sort_values(by=['P','T'])
    df=df.reset_index(drop=True)
    #If input is P and v
    #Creating an array of only P values / no duplicates
    P=df['P'].drop_duplicates()

    #Create list of only Ps
    Pls=P.tolist()

    #Find closest row to the P value
    subP=P-Pinput
    subPls=subP.values.tolist()
    m = float(min(i for i in subP if i >= 0))

    #row of pressure within the no duplicates pressure array
    rowOfPressure=subPls.index(m)
    PressureHigh=Pls[rowOfPressure]
    PressureLow=Pls[rowOfPressure-1]
    ratioP=(Pinput-PressureLow)/(PressureHigh-PressureLow)

    zeros=np.zeros((36,6))
    rowH=rowOfPressure*36
    rowL=(rowOfPressure-1)*36

    #storing values of Highpressure Data
    column=-1
    DATA_VALUESHIGH=np.zeros((36,6))
    for i in c:
        column=column+1
        for j in range(0,36):
            DATA_VALUESHIGH[j,column]=df.loc[rowH+j,i]


    #storing values of Highpressure Data
    column=-1
    DATA_VALUESLOW=np.zeros((36,6))
    for i in c:
        column=column+1
        for j in range(0,36):
            DATA_VALUESLOW[j,column]=df.loc[rowL+j,i]

    if vinput!=-1:
        print('run')
        #Calculate values at precise position of Pressure
        DATA_VALUES=ratioP*DATA_VALUESHIGH+(1-ratioP)*DATA_VALUESLOW
        #lookup v
        v=DATA_VALUES[:,2]
        subv=v-vinput
        subvls=subv.tolist()
        print(v)
        try :
            n = min(i for i in subv if i >= 0)
            rowOfv=subvls.index(n)
            vHigh=v[rowOfv]
            vLow=v[rowOfv-1]
            ratiov=(vinput-vLow)/(vHigh-vLow)
            standbyerror=False


        except ValueError:
            print('raaan')
            standbyerror=True

    if uinput!=-1:
        #Calculate values at precise position of Pressure
        DATA_VALUES=ratioP*DATA_VALUESHIGH+(1-ratioP)*DATA_VALUESLOW
        #lookup v
        u=DATA_VALUES[:,3]
        subu=u-uinput
        subuls=subu.tolist()

        try :
            n = min(i for i in subu if i >= 0)
            rowOfu=subuls.index(n)
            uHigh=u[rowOfu]
            uLow=u[rowOfu-1]
            ratiou=(uinput-uLow)/(uHigh-uLow)
            standbyerror=False

        except ValueError:
            print('raaan')
            standbyerror=True

    if hinput!=-1:
        #Calculate values at precise position of Pressure
        DATA_VALUES=ratioP*DATA_VALUESHIGH+(1-ratioP)*DATA_VALUESLOW
        #lookup v
        h=DATA_VALUES[:,4]
        subh=h-hinput
        subhls=subh.tolist()

        try :
            n = min(i for i in subh if i >= 0)
            rowOfh=subhls.index(n)
            hHigh=h[rowOfh]
            hLow=h[rowOfh-1]
            ratioh=(hinput-hLow)/(hHigh-hLow)
            standbyerror=False


        except ValueError:
            print('raaan')
            standbyerror=True


    if sinput!=-1:
        #Calculate values at precise position of Pressure
        DATA_VALUES=ratioP*DATA_VALUESHIGH+(1-ratioP)*DATA_VALUESLOW
        #lookup v
        s=DATA_VALUES[:,5]
        subs=s-sinput
        subsls=subs.tolist()

        try :
            n = min(i for i in subs if i >= 0)
            rowOfs=subsls.index(n)
            sHigh=s[rowOfs]
            sLow=s[rowOfs-1]
            ratios=(sinput-sLow)/(sHigh-sLow)
            standbyerror=False


        except ValueError:
            print('raaan')
            standbyerror=True

    return(standbyerror)
