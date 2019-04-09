def value2setter(Input2,Input2value):

    uinput=-1
    vinput=-1
    hinput=-1
    sinput=-1
    xinput=-1

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
    return[vinput,uinput,hinput,sinput,xinput]
