#!/usr/bin/env python
# coding: utf-8

# ## Comms Example
# 
# Author: Gary Decosmo

import math as ma
import numpy as np

def AD_numBinCodes(N_bits):
    sol = 2**N_bits
    print(f"For {N_bits} bits, The number of discrete levels represented is {sol} binary codes")
    return sol

def AD_numVoltIncrements(bin_codes):
    sol = bin_codes - 1
    print(f"For {bin_codes} bin codes, the number of voltage increments used to divide total voltage range is {sol}")
    return sol
    
def AD_resolution(v_range,v_increments):
    
    if ((v_range[0] < 0) and (v_range[1] > 0)):
        vt = sum([abs(i) for i in v_range])
    if ((v_range[0] > 0) and (v_range[1] > 0)):
        a = max(v_range)
        b = min(v_range)
        vt = a-b
    if ((v_range[0] > 0) and (v_range[1] < 0)):
        raise ValueError("Please enter voltage range in the form of [minVoltage,maxVoltage]")
    if (v_range[0] == v_range[1]):
        raise ValueError("No voltage present, enter a valid range in the form of [minVoltage,maxVoltage]")
    res = vt/v_increments
    print(f"For voltage range of {vt} V and number of voltage increments is {v_increments}, Resolution is {res*1000:0.3f} mV")
    return res

# AM signal modulation index
def modIndex(vmax,vmin):
    m = (vmax-vmin)/(vmax+vmin)
    return m
    print(f"Modulation (Dec): {m:0.2f}")

def PowerT(Pc,m):
    pt = Pc*(1+((m**2)/2))
    return pt
    print(f"Total Power: {pt:0.2f} W")

def PsideBand(pt,pc):
    ps2 = pt-pc
    ps1 = ps2/2
    return ps1
    print(f"Once Sideband: {ps1:0.2f} W")
    
def freqDev(fd,fm):
    mf = fd/fm
    return mf
    print(f"Mf = {mf:0.2f}")
def BW(flow,fhigh):
    if (fhigh < flow):
        df = flow - fhigh
        print(f"BW = {df:0.2f} Hz")
    else:  
        df = fhigh - flow
        print(f"BW = {df:0.2f} Hz")
    return df

def SNR(SNRdB):
    snr = 10**(SNRdB/10)
    print(f"SNR = {snr:0.2f}")
    return snr

def SNRdB(SNR):
    snrdb = 10*ma.log10(SNR)
    print(f"SNRdB = {snrdb:0.2f} dB")
    
def DataR(SNR,BW):
    r = BW*ma.log2(1+SNR)
    print(f"Data Rate = {r:0.2f}")
    return r

v_range = [26,16]
bc = AD_numBinCodes(14)
vinc = AD_numVoltIncrements(bc)
vtrange = AD_resolution(v_range,vinc)

# Given
SNRdB = 45 #dB
fh = 3200 #Hz
fl = 300 #Hz
fth = 1200 #Hz
ftl = 300 #Hz
frh = 3200 #Hz
frl = 1500 #Hz

# bandwidths: total, transmitted, received
bw_t = BW(3200,300)
bwt = BW(1200,300)
bwr = BW(3200,1500)

# converting dB into S/N
snr = SNR(45)

# data rate for overall, transmitted, and received
DR_t = DataR(snr,bw_t)
DRt = DataR(snr,bwt)
DRr = DataR(snr,bwr)