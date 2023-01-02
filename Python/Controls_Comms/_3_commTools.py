
import math as ma
import numpy as np

# Helpers

def SNR(n):
    # Signal to Noise Ratio given n Bits
    snr = 6.02*n+1.76
    return snr

def SNR2P(SNR):
    # Converts SNR dB to percentage of signal to noise
    p = (10**(-((SNR)/20)))*100
    return p

def ENOB(SNR):
    # Effective number of bits given Signal to noise ratio
    bits = (SNR-1.76)/6.02
    return bits

def RMS(Amplitude):
    # RMS voltage given amplitude of wave
    rms = Amplitude/ma.sqrt(2)
    return rms

def LSB2SNR(LSB):
    # returns LSB given rms voltage
    snr = 20*ma.log(LSB*ma.sqrt(6))
    return snr

def DNL(Ci,Cavg):
    dnl = (Ci/Cavg)-1
    return dnl