# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:21:22 2024

@author: daniv
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, get_window, find_peaks, cwt, morlet
from scipy.fftpack import fft
from scipy.stats import ttest_rel
from scipy.signal import cwt, morlet, ricker
import pywt

# Cargar datos
datos = np.loadtxt('maria.txt', delimiter=',')
tiempo = datos[:, 0]*30
ecg = datos[:, 1]

# Graficar la señal EMG original
plt.figure(figsize=(10, 6))
plt.plot(tiempo, ecg, label='Señal ECG', color='#ee5ca5')
plt.title('Señal EMG')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud [mV]')
plt.legend()
plt.grid()
plt.show()


fs = 500 
lowcut = 0.5 
highcut = 40 

def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs  
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

# Aplicar el filtro a la señal
def aplicar_filtro(data, lowcut, highcut, fs, order=4):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

ecg_normalizada = ecg / np.max(np.abs(ecg))
ecg_filtrada = aplicar_filtro(ecg_normalizada, lowcut, highcut, fs)

plt.figure(figsize=(10, 6))
plt.plot(tiempo, ecg_filtrada, label='ECG Filtrada', color='#cd60f5')
plt.title('Señal ECG Filtrada')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [mV]')
plt.legend()
plt.grid()
plt.show()
 #picos
picos_R, _ = find_peaks(ecg_filtrada, height=0.3, distance=fs*0.1)
print(f'Número de picos R detectados: {len(picos_R)}')
  
plt.figure(figsize=(10, 6))
plt.plot(tiempo, ecg_filtrada, label='ECG Filtrada', color='#4ef2eb')
plt.plot(tiempo[picos_R], ecg_filtrada[picos_R], '*', label='Picos R', color='#4e8cf2')
plt.title('Detección de Picos R')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [mV]')
plt.legend()
plt.grid()
plt.show()

intervalos_RR = np.diff(tiempo[picos_R])# Diferencias de tiempo entre picos R
print("Intervalos R-R (en segundos):", intervalos_RR)

plt.figure(figsize=(10, 6))
plt.plot(intervalos_RR, linestyle='-', color='#1f77b4')
plt.title('Intervalos R-R')
plt.xlabel('Número de intervalo')
plt.ylabel('Tiempo [ms]')
plt.grid()
plt.show()

# Análisis de HRV en el dominio del tiempo
media_RR = np.mean(intervalos_RR)
desviacion_RR = np.std(intervalos_RR)

print(f"Media de los intervalos R-R: {media_RR:.4f} s")
print(f"Desviación estándar de los intervalos R-R: {desviacion_RR:.4f} s")


fs = 1.0 / np.mean(intervalos_RR)
frecuencias = np.linspace(0.04, 0.15, 100)  # Rango LF y HF Hz

escalas = pywt.scale2frequency('cmor', 1) / (frecuencias * fs)

coeficientes, _ = pywt.cwt(intervalos_RR, escalas, 'cmor')

plt.figure(figsize=(12, 8))
plt.imshow(np.abs(coeficientes), extent=[0, len(intervalos_RR), frecuencias[-1], frecuencias[0]],
           cmap='jet', aspect='auto')
plt.colorbar(label='Magnitud')
plt.title('Espectrograma de HRV usando Wavelet Continua (Morlet)')
plt.xlabel('Número de intervalo')
plt.ylabel('Frecuencia (Hz)')
plt.gca().invert_yaxis()  
plt.show()

