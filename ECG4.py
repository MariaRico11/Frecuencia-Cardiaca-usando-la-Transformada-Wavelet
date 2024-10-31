# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 21:17:01 2024

@author: daniv
"""

import sys
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QFileDialog, QLineEdit
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import serial.tools.list_ports
import serial
import numpy as np
import struct

import threading

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import datetime

class principal(QMainWindow):
    
    def __init__(self):
        super(principal, self).__init__()
        uic.loadUi("Lab3 EMG.ui", self)
        self.puertos_disponibles()
        self.ser = None
        self.connect.clicked.connect(self.conectar)

        self.guardarButton.clicked.connect(self.guardar_datos)
        self.cargarButton.clicked.connect(self.cargar_y_mostrar_datos)

        self.x = np.linspace(0, 10, 1000)
        self.y = np.linspace(0, 0, 1000)

        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.graficawidget.setLayout(layout)

    def puertos_disponibles(self):
        p = serial.tools.list_ports.comports()
        for port in p:
            self.puertos.addItem(port.device)

    def conectar(self): 
        estado = self.connect.text()
        self.stop_event_ser = threading.Event()
        if estado == "CONECTAR":
            com = self.puertos.currentText()
            try:
                self.ser = serial.Serial(com, 115200)
                self.hilo_ser = threading.Thread(target=self.periodic_thread)
                self.hilo_ser.start()
                print("Puerto serial Conectado")
                self.connect.setText("DESCONECTAR")

            except serial.SerialException as e:
                print("Error en el puerto serial: ", e)
        else:
            self.ser.close()
            self.stop_event_ser.set()
            self.hilo_ser.join()
            print("Puerto serial Desconectado")
            self.connect.setText("CONECTAR")

    def periodic_thread(self):
        if self.ser is not None and self.ser.is_open:
            data = self.ser.read(50)
            if len(data) == 50:
                data = struct.unpack('50B', data)
                for i in range(0, len(data), 2):
                    self.y = np.roll(self.y, -1)
                    self.y[-1] = data[i] * 100 + data[i + 1]

                self.ax.clear()
                self.ax.plot(self.x, self.y)
                self.ax.grid(True)
                self.canvas.draw()
                
        if not self.stop_event_ser.is_set():
            threading.Timer(1e-3, self.periodic_thread).start()

    def guardar_datos(self):
        try:
            now = datetime.datetime.now()
            fecha_hora = now.strftime("%Y-%m-%d %H:%M:%S")
            nombre_persona = self.nombre_persona.text()
            nombre_persona = nombre_persona.replace(":", "").replace(" ", "_")
            nombre_archivo = f"{nombre_persona}.txt"

            with open(nombre_archivo, 'w') as f:
                f.write(f"Fecha y hora: {fecha_hora}\n")
                f.write(f"Nombre del paciente: {nombre_persona}\n")
                f.write("Datos de la medición:\n")
                for i in range(len(self.x)):
                    f.write(f"{self.x[i]}, {self.y[i]}\n")

            print(f"Datos guardados en {nombre_archivo}")

        except Exception as e:
            print("Error al guardar los datos:", e)

    def cargar_datos(self, nombre_archivo):
        try:
            x = []
            y = []

            with open(nombre_archivo, 'r') as f:
                for _ in range(4):
                    next(f)

                for line in f:
                    datos = line.strip().split(",")
                    x.append(float(datos[0]))
                    y.append(float(datos[1]))
            return x, y

        except Exception as e:
            print("Error al cargar los datos:", e)
            return None, None

    def cargar_y_mostrar_datos(self):
        nombre_archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos de texto (*.txt)")
        if nombre_archivo:
            x, y = self.cargar_datos(nombre_archivo)
            if x and y:
                self.x = x
                self.y = y
                self.ax.clear()
                self.ax.plot(self.x, self.y, color = '#ee5ca0')
                self.ax.set_xlabel('Tiempo')
                self.ax.set_ylabel('Valor')
                self.ax.set_title('ECG ')
                self.canvas.draw()
                print("Datos cargados y mostrados desde", nombre_archivo)
            else:
                print("No se pudieron cargar los datos desde", nombre_archivo)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = principal()
    ventana.show()
    sys.exit(app.exec())
