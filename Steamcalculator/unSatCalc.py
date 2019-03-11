############### Unsaturated calculation ##################

import numpy as np
import pandas as pd



#start Calculation

def unSatCalcP(Input1value,Input2value,Input2):

    print('unSatCalcP ran')

    Pinput=-1
    Tinput=-1
    uinput=-1
    vinput=-1
    hinput=-1
    sinput=-1
    xinput=-1

    df = pd.read_csv('/Users/juanrodriguezlacasa/Documents/Imperial/ME4/FYP/Steam/dataunsaturated.csv')
    c=df.columns.values.tolist()
    Tsat=[0.01, 7, 32.9, 45.8, 60.1, 81.3, 99.6, 100, 120.2, 143.6, 158.8, 170.4, 179.9, 212.4, 233.9,
      250.4, 263.9, 275.6, 285.8, 295, 303.3, 311, 324.7, 336.7, 347.4, 357, 365.7, 373.7]

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

    #Creating an array of only P values / no duplicates
    P=df['P'].drop_duplicates()

    #Create list of only Ps
    Pls=P.tolist()

    #Find closest row to the P value
    subP=P-Pinput
    subPls=subP.values.tolist()
    m = int(min(i for i in subP if i >= 0))

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

    #### FOR V ####
    if vinput !=-1:
        #lookup vlow
        vlow=DATA_VALUESLOW[:,2]
        subvlow=vlow-vinput
        subvlowls=subvlow.tolist()
        n = min(i for i in subvlow if i >= 0)
        rowOfvlow=subvlowls.index(n)

        LowTemplow=DATA_VALUESLOW[rowOfvlow-1][1]
        LowTemphigh=DATA_VALUESLOW[rowOfvlow][1]

        #lookup vhigh
        vhigh=DATA_VALUESHIGH[:,2]
        subvhigh=vhigh-vinput
        subvhighls=subvhigh.tolist()
        n = min(i for i in subvhigh if i >= 0)
        rowOfvhigh=subvhighls.index(n)

        HighTemplow=DATA_VALUESHIGH[rowOfvhigh-1][1]
        HighTemphigh=DATA_VALUESHIGH[rowOfvhigh][1]

        ### CHECK IF TOO CLOSE TO SATURATION LINE ###
        a='proceed'
        if Tsat[rowOfPressure-1]>LowTemplow and Tsat[rowOfPressure-1]<LowTemphigh:
            print('error')
            a='noproceed'
        if Tsat[rowOfPressure-1]>HighTemplow and Tsat[rowOfPressure-1]<HighTemphigh:
            print('error')
            a='noproceed'

        ### CALCULATE VALUES IF V IS OK ###

        if a=='proceed':
            #Calculate values at precise position of Pressure
            DATA_VALUES=ratioP*DATA_VALUESHIGH+(1-ratioP)*DATA_VALUESLOW
            #lookup v
            v=DATA_VALUES[:,2]
            subv=v-vinput
            subvls=subv.tolist()
            n = min(i for i in subv if i >= 0)
            rowOfv=subvls.index(n)

            #ratio of v
            vHigh=v[rowOfv]
            vLow=v[rowOfv-1]
            ratiov=(vinput-vLow)/(vHigh-vLow)

            #outputs
            P=ratiov*DATA_VALUES[rowOfv,0]+(1-ratiov)*DATA_VALUES[rowOfv-1,0]
            T=ratiov*DATA_VALUES[rowOfv,1]+(1-ratiov)*DATA_VALUES[rowOfv-1,1]
            v=ratiov*DATA_VALUES[rowOfv,2]+(1-ratiov)*DATA_VALUES[rowOfv-1,2]
            u=ratiov*DATA_VALUES[rowOfv,3]+(1-ratiov)*DATA_VALUES[rowOfv-1,3]
            h=ratiov*DATA_VALUES[rowOfv,4]+(1-ratiov)*DATA_VALUES[rowOfv-1,4]
            s=ratiov*DATA_VALUES[rowOfv,5]+(1-ratiov)*DATA_VALUES[rowOfv-1,5]

         ### uinput ###

    if uinput !=-1 :
        #lookup ulow
        ulow=DATA_VALUESLOW[:,3]
        subulow=ulow-uinput
        subulowls=subulow.tolist()
        n = min(i for i in subulow if i >= 0)
        rowOfulow=subulowls.index(n)

        LowTemplow=DATA_VALUESLOW[rowOfulow-1][1]
        LowTemphigh=DATA_VALUESLOW[rowOfulow][1]

        #lookup uhigh
        uhigh=DATA_VALUESHIGH[:,3]
        subuhigh=uhigh-uinput
        subuhighls=subuhigh.tolist()
        n = min(i for i in subuhigh if i >= 0)
        rowOfuhigh=subuhighls.index(n)

        HighTemplow=DATA_VALUESHIGH[rowOfuhigh-1][1]
        HighTemphigh=DATA_VALUESHIGH[rowOfuhigh][1]

        ### CHECK IF TOO CLOSE TO SATURATION LINE ###
        a='proceed'
        if Tsat[rowOfPressure-1]>LowTemplow and Tsat[rowOfPressure-1]<LowTemphigh:
            print('error')
            a='noproceed'
        if Tsat[rowOfPressure-1]>HighTemplow and Tsat[rowOfPressure-1]<HighTemphigh:
            print('error')
            a='noproceed'

        ### CALCULATE VALUES IF U IS OK ###

        if a=='proceed':
            #Calculate values at precise position of Pressure
            DATA_VALUES=ratioP*DATA_VALUESHIGH+(1-ratioP)*DATA_VALUESLOW
            #lookup u
            u=DATA_VALUES[:,3]
            subu=u-uinput
            subuls=subu.tolist()
            n = min(i for i in subu if i >= 0)
            rowOfu=subuls.index(n)

            #ratio of u
            uHigh=u[rowOfu]
            uLow=u[rowOfu-1]
            ratiou=(uinput-uLow)/(uHigh-uLow)

            #outputs
            P=ratiou*DATA_VALUES[rowOfu,0]+(1-ratiou)*DATA_VALUES[rowOfu-1,0]
            T=ratiou*DATA_VALUES[rowOfu,1]+(1-ratiou)*DATA_VALUES[rowOfu-1,1]
            v=ratiou*DATA_VALUES[rowOfu,2]+(1-ratiou)*DATA_VALUES[rowOfu-1,2]
            u=ratiou*DATA_VALUES[rowOfu,3]+(1-ratiou)*DATA_VALUES[rowOfu-1,3]
            h=ratiou*DATA_VALUES[rowOfu,4]+(1-ratiou)*DATA_VALUES[rowOfu-1,4]
            s=ratiou*DATA_VALUES[rowOfu,5]+(1-ratiou)*DATA_VALUES[rowOfu-1,5]

    if hinput !=-1 :
        #lookup hlow
        hlow=DATA_VALUESLOW[:,4]
        subhlow=hlow-hinput
        subhlowls=subhlow.tolist()
        n = min(i for i in subhlow if i >= 0)
        rowOfhlow=subhlowls.index(n)

        LowTemplow=DATA_VALUESLOW[rowOfhlow-1][1]
        LowTemphigh=DATA_VALUESLOW[rowOfhlow][1]

        #lookup hhigh
        hhigh=DATA_VALUESHIGH[:,4]
        subhhigh=hhigh-hinput
        subhhighls=subhhigh.tolist()
        n = min(i for i in subhhigh if i >= 0)
        rowOfhhigh=subhhighls.index(n)

        HighTemplow=DATA_VALUESHIGH[rowOfhhigh-1][1]
        HighTemphigh=DATA_VALUESHIGH[rowOfhhigh][1]

        ### CHECK IF TOO CLOSE TO SATURATION LINE ###
        a='proceed'
        if Tsat[rowOfPressure-1]>LowTemplow and Tsat[rowOfPressure-1]<LowTemphigh:
            print('error')
            a='noproceed'
        if Tsat[rowOfPressure-1]>HighTemplow and Tsat[rowOfPressure-1]<HighTemphigh:
            print('error')
            a='noproceed'

        ### CALCULATE VALUES IF H IS OK ###

        if a=='proceed':
            #Calculate values at precise position of Pressure
            DATA_VALUES=ratioP*DATA_VALUESHIGH+(1-ratioP)*DATA_VALUESLOW
            #lookup h
            h=DATA_VALUES[:,4]
            subh=h-hinput
            subhls=subh.tolist()
            n = min(i for i in subh if i >= 0)
            rowOfh=subhls.index(n)

            #ratio of h
            hHigh=h[rowOfh]
            hLow=h[rowOfh-1]
            ratioh=(hinput-hLow)/(hHigh-hLow)

            #outputs
            P=ratioh*DATA_VALUES[rowOfh,0]+(1-ratioh)*DATA_VALUES[rowOfh-1,0]
            T=ratioh*DATA_VALUES[rowOfh,1]+(1-ratioh)*DATA_VALUES[rowOfh-1,1]
            v=ratioh*DATA_VALUES[rowOfh,2]+(1-ratioh)*DATA_VALUES[rowOfh-1,2]
            u=ratioh*DATA_VALUES[rowOfh,3]+(1-ratioh)*DATA_VALUES[rowOfh-1,3]
            h=ratioh*DATA_VALUES[rowOfh,4]+(1-ratioh)*DATA_VALUES[rowOfh-1,4]
            s=ratioh*DATA_VALUES[rowOfh,5]+(1-ratioh)*DATA_VALUES[rowOfh-1,5]

    #### FOR S ####
    if sinput !=-1 :
        #lookup slow
        slow=DATA_VALUESLOW[:,5]
        subslow=slow-sinput
        subslowls=subslow.tolist()
        n = min(i for i in subslow if i >= 0)
        rowOfslow=subslowls.index(n)

        LowTemplow=DATA_VALUESLOW[rowOfslow-1][1]
        LowTemphigh=DATA_VALUESLOW[rowOfslow][1]

        #lookup shigh
        shigh=DATA_VALUESHIGH[:,5]
        subshigh=shigh-sinput
        subshighls=subshigh.tolist()
        n = min(i for i in subshigh if i >= 0)
        rowOfshigh=subshighls.index(n)

        HighTemplow=DATA_VALUESHIGH[rowOfshigh-1][1]
        HighTemphigh=DATA_VALUESHIGH[rowOfshigh][1]

        ### CHECK IF TOO CLOSE TO SATURATION LINE ###
        a='proceed'
        if Tsat[rowOfPressure-1]>LowTemplow and Tsat[rowOfPressure-1]<LowTemphigh:
            print('error')
            a='noproceed'
        if Tsat[rowOfPressure-1]>HighTemplow and Tsat[rowOfPressure-1]<HighTemphigh:
            print('error')
            a='noproceed'

        ### CALCULATE VALUES IF S IS OK ###

        if a=='proceed':
            #Calculate values at precise position of Pressure
            DATA_VALUES=ratioP*DATA_VALUESHIGH+(1-ratioP)*DATA_VALUESLOW
            #lookup s
            s=DATA_VALUES[:,5]
            subs=s-sinput
            subsls=subs.tolist()
            n = min(i for i in subs if i >= 0)
            rowOfs=subsls.index(n)

            #ratio of s
            sHigh=s[rowOfs]
            sLow=s[rowOfs-1]
            ratios=(sinput-sLow)/(sHigh-sLow)

            #outputs
            P=ratios*DATA_VALUES[rowOfs,0]+(1-ratios)*DATA_VALUES[rowOfs-1,0]
            T=ratios*DATA_VALUES[rowOfs,1]+(1-ratios)*DATA_VALUES[rowOfs-1,1]
            v=ratios*DATA_VALUES[rowOfs,2]+(1-ratios)*DATA_VALUES[rowOfs-1,2]
            u=ratios*DATA_VALUES[rowOfs,3]+(1-ratios)*DATA_VALUES[rowOfs-1,3]
            h=ratios*DATA_VALUES[rowOfs,4]+(1-ratios)*DATA_VALUES[rowOfs-1,4]
            s=ratios*DATA_VALUES[rowOfs,5]+(1-ratios)*DATA_VALUES[rowOfs-1,5]
    x=0
    return[P,T,v,u,h,s,x]

def unSatCalcT(Input1value,Input2value,Input2):

    print('unSatCalcT ran')

    Pinput=-1
    Tinput=-1
    uinput=-1
    vinput=-1
    hinput=-1
    sinput=-1
    xinput=-1

    df = pd.read_csv('/Users/juanrodriguezlacasa/Documents/Imperial/ME4/FYP/Steam/dataunsaturated.csv')
    c=df.columns.values.tolist()
    Tsat=[0.01, 7, 32.9, 45.8, 60.1, 81.3, 99.6, 100, 120.2, 143.6, 158.8, 170.4, 179.9, 212.4, 233.9,
      250.4, 263.9, 275.6, 285.8, 295, 303.3, 311, 324.7, 336.7, 347.4, 357, 365.7, 373.7]

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

    #Sort by values of T instead of P
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
    m = int(min(i for i in subT if i >= 0))

    #row of pressure within the no duplicates pressure array
    rowOfTemperature=subTls.index(m)
    TemperatureHigh=Tls[rowOfTemperature]
    TemperatureLow=Tls[rowOfTemperature-1]
    ratioT=(Tinput-TemperatureLow)/(TemperatureHigh-TemperatureLow)

    zeros=np.zeros((36,6))
    rowH=rowOfTemperature*36
    rowL=(rowOfTemperature-1)*36

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

    ######## MISSING CHECK IF TOO CLOSE TO SATURATION LINE!!!!! #################


    # Missing this calculation for u, v, h and s within their section



    #################################################################################


        if uinput!=-1:
            #Calculate values at precise position of Pressure
            DATA_VALUES=ratioT*DATA_VALUESHIGH+(1-ratioT)*DATA_VALUESLOW
            #lookup u
            u=DATA_VALUES[:,3]
            subu=u-uinput
            subuls=subu.tolist()
            n = min(i for i in subu if i >= 0)
            rowOfu=subuls.index(n)

            #ratio of s
            uHigh=u[rowOfu]
            uLow=u[rowOfu-1]
            ratiou=(uinput-uLow)/(uHigh-uLow)

             #outputs
            P=ratiou*DATA_VALUES[rowOfu,0]+(1-ratiou)*DATA_VALUES[rowOfu-1,0]
            T=ratiou*DATA_VALUES[rowOfu,1]+(1-ratiou)*DATA_VALUES[rowOfu-1,1]
            v=ratiou*DATA_VALUES[rowOfu,2]+(1-ratiou)*DATA_VALUES[rowOfu-1,2]
            u=ratiou*DATA_VALUES[rowOfu,3]+(1-ratiou)*DATA_VALUES[rowOfu-1,3]
            h=ratiou*DATA_VALUES[rowOfu,4]+(1-ratiou)*DATA_VALUES[rowOfu-1,4]
            s=ratiou*DATA_VALUES[rowOfu,5]+(1-ratiou)*DATA_VALUES[rowOfu-1,5]

        if vinput!=-1:
            #Calculate values at precise position of Pressure
            DATA_VALUES=ratioT*DATA_VALUESHIGH+(1-ratioT)*DATA_VALUESLOW
            #lookup v
            v=DATA_VALUES[:,2]
            subv=v-vinput
            subvls=subv.tolist()
            n = min(i for i in subv if i >= 0)
            rowOfv=subvls.index(n)

            #ratio of s
            vHigh=v[rowOfv]
            vLow=v[rowOfv-1]
            ratiov=(vinput-vLow)/(vHigh-vLow)

             #outputs
            P=ratiov*DATA_VALUES[rowOfv,0]+(1-ratiov)*DATA_VALUES[rowOfv-1,0]
            T=ratiov*DATA_VALUES[rowOfv,1]+(1-ratiov)*DATA_VALUES[rowOfv-1,1]
            v=ratiov*DATA_VALUES[rowOfv,2]+(1-ratiov)*DATA_VALUES[rowOfv-1,2]
            u=ratiov*DATA_VALUES[rowOfv,3]+(1-ratiov)*DATA_VALUES[rowOfv-1,3]
            h=ratiov*DATA_VALUES[rowOfv,4]+(1-ratiov)*DATA_VALUES[rowOfv-1,4]
            s=ratiov*DATA_VALUES[rowOfv,5]+(1-ratiov)*DATA_VALUES[rowOfv-1,5]

        if hinput!=-1:

            #Calculate values at precise position of Pressure
            DATA_VALUES=ratioT*DATA_VALUESHIGH+(1-ratioT)*DATA_VALUESLOW
            #lookup h
            h=DATA_VALUES[:,4]
            subh=h-hinput
            subhls=subh.tolist()
            n = min(i for i in subh if i >= 0)
            rowOfh=subhls.index(n)

            #ratio of h
            hHigh=h[rowOfh]
            hLow=h[rowOfh-1]
            ratioh=(hinput-hLow)/(hHigh-hLow)

            #outputs
            P=ratioh*DATA_VALUES[rowOfh,0]+(1-ratioh)*DATA_VALUES[rowOfh-1,0]
            T=ratioh*DATA_VALUES[rowOfh,1]+(1-ratioh)*DATA_VALUES[rowOfh-1,1]
            v=ratioh*DATA_VALUES[rowOfh,2]+(1-ratioh)*DATA_VALUES[rowOfh-1,2]
            u=ratioh*DATA_VALUES[rowOfh,3]+(1-ratioh)*DATA_VALUES[rowOfh-1,3]
            h=ratioh*DATA_VALUES[rowOfh,4]+(1-ratioh)*DATA_VALUES[rowOfh-1,4]
            s=ratioh*DATA_VALUES[rowOfh,5]+(1-ratioh)*DATA_VALUES[rowOfh-1,5]

        if sinput!=-1:
            #Calculate values at precise position of Pressure
            DATA_VALUES=ratioT*DATA_VALUESHIGH+(1-ratioT)*DATA_VALUESLOW
            #lookup s
            s=DATA_VALUES[:,5]
            subs=s-sinput
            subsls=subs.tolist()
            n = min(i for i in subs if i >= 0)
            rowOfs=subsls.index(n)

            #ratio of s
            sHigh=s[rowOfs]
            sLow=s[rowOfs-1]
            ratios=(sinput-sLow)/(sHigh-sLow)

            #outputs
            P=ratios*DATA_VALUES[rowOfs,0]+(1-ratios)*DATA_VALUES[rowOfs-1,0]
            T=ratios*DATA_VALUES[rowOfs,1]+(1-ratios)*DATA_VALUES[rowOfs-1,1]
            v=ratios*DATA_VALUES[rowOfs,2]+(1-ratios)*DATA_VALUES[rowOfs-1,2]
            u=ratios*DATA_VALUES[rowOfs,3]+(1-ratios)*DATA_VALUES[rowOfs-1,3]
            h=ratios*DATA_VALUES[rowOfs,4]+(1-ratios)*DATA_VALUES[rowOfs-1,4]
            s=ratios*DATA_VALUES[rowOfs,5]+(1-ratios)*DATA_VALUES[rowOfs-1,5]

    x=0
    return[P,T,v,u,h,s,x]
