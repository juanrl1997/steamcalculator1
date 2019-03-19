import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import pylab
from pylab import *
import PIL
import PIL.Image
import io
from io import *

dfsat=pd.read_csv('/Users/juanrodriguezlacasa/Documents/Imperial/ME4/FYP/Steam/Data.csv')
csat=dfsat.columns.values.tolist()

def  Pvplot(Pvalue,vvalue):

    plt.clf()

    P=dfsat['P'].tolist()
    vg=dfsat['vg'].tolist()
    vf=dfsat['vf'].tolist()
    plt.semilogx(vg,P,'b')
    plt.semilogx(vf,P,'r')
    plt.xlabel('v')
    plt.ylabel('P')
    Pcrit=220.64
    vcrit=0.003106
    plt.plot(vcrit,Pcrit,'x')
    plt.plot(vvalue,Pvalue,'x')

def Phplot(Pvalue,hvalue):
    plt.clf()
    P=dfsat['P'].tolist()
    hg=dfsat['hg'].tolist()
    hf=dfsat['hf'].tolist()
    plt.semilogy(hg,P,'b')
    plt.semilogy(hf,P,'r')
    plt.xlabel('h')
    plt.ylabel('P')
    Pcrit=220.64
    hcrit=2087.5
    plt.plot(hcrit,Pcrit,'x')
    plt.plot(hvalue,Pvalue,'x')

def Tsplot(Tvalue,svalue):
    plt.clf()
    T=dfsat['T'].tolist()
    sg=dfsat['sg'].tolist()
    sf=dfsat['sf'].tolist()
    plt.plot(sg,T,'b')
    plt.plot(sf,T,'r')
    plt.xlabel('s')
    plt.ylabel('T')
    Tcrit=373.65
    scrit=4.412
    plt.plot(scrit,Tcrit,'x')
    plt.plot(svalue,Tvalue,'x')

def Hsplot(hvalue,svalue):
    plt.clf()
    hf=dfsat['hf'].tolist()
    hg=dfsat['hg'].tolist()
    sg=dfsat['sg'].tolist()
    sf=dfsat['sf'].tolist()
    plt.plot(sg,hg,'b')
    plt.plot(sf,hf,'r')
    plt.xlabel('s')
    plt.ylabel('h')
    scrit=4.412
    hcrit=2087.5
    plt.plot(scrit,hcrit,'x')
    plt.plot(svalue,hvalue,'x')
