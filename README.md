### VARIABILIDAD DE LA FRECUENCIA CARDIACA USANDO LA TRANSFORMADA WAVELET

Este laboratorio tiene como objetivo analizar la variabilidad de la frecuencia cardíaca (HRV) empleando la transformada wavelet, una herramienta que permite identificar cambios en las frecuencias características y evaluar la dinámica temporal de la señal cardíaca. Para alcanzar este objetivo, es necesario poseer conocimientos previos sobre la metodología de funcionamiento del sistema cardiaco y el procesamiento de esta señal, los cuales serán detallados a continuación.

La señal electrocardiográfica es una representación gráfica de la actividad eléctrica del corazón obtenida mediante un electrocardiograma (ECG). Esta señal muestra las variaciones en el potencial eléctrico a lo largo del ciclo cardíaco, proporcionando información valiosa sobre la función y el estado del corazón. El análisis de la señal es esencial para la detección de arritmias, la evaluación de enfermedades cardíacas y el monitoreo de la salud cardiovascular.

- **Complejo QRS e Intervalo RR:** El complejo QRS es la porción de la señal que representa la despolarización de los ventrículos, un momento clave del ciclo cardíaco. La duración y amplitud de este complejo pueden ofrecer pistas sobre el estado de los ventrículos y posibles anomalías en la conducción eléctrica.
El intervalo RR, por su parte, mide el tiempo entre dos complejos QRS consecutivos y permite calcular la frecuencia cardíaca. A través del análisis de la variabilidad de este intervalo (HRV o variabilidad de la frecuencia cardíaca), se puede evaluar la influencia del sistema nervioso autónomo en el corazón y detectar irregularidades en el ritmo cardíaco. 
En conjunto, el estudio detallado de la señal electrocardiográfica y de parámetros específicos como el complejo QRS y el intervalo RR es esencial para la comprensión de la dinámica cardíaca y el diagnóstico de diversas condiciones cardiovasculares.


![image](https://github.com/user-attachments/assets/61dd6468-dc31-43dd-ae63-e8990e5efd24)


- **El sistema nervioso autónomo (SNA)** es una parte fundamental del sistema nervioso encargada de regular las funciones involuntarias del cuerpo, como la frecuencia cardíaca, la digestión y la respiración. Este sistema se divide en dos componentes principales: el sistema nervioso simpático y el sistema nervioso parasimpático, que actúan de forma complementaria y, en muchas ocasiones, opuesta.
  
- **Sistema Nervioso Simpático:** Prepara al cuerpo para enfrentar situaciones de estrés o emergencia, activando la respuesta de "lucha o huida". En este proceso, aumenta la frecuencia cardíaca, dilata las pupilas y libera glucosa en el torrente sanguíneo, proporcionando así una fuente de energía adicional.
  
- **Sistema Nervioso Parasimpático:**  Promueve la relajación y la conservación de energía, facilitando actividades como la digestión y el descanso. Disminuye la frecuencia cardíaca y estimula procesos que ayudan a conservar los recursos energéticos del organismo.
Ambos sistemas trabajan de manera conjunta para mantener la homeostasis, o el equilibrio interno del cuerpo. Por ejemplo, mientras que el sistema simpático activa respuestas rápidas frente al estrés, el sistema parasimpático ayuda a restaurar el estado de calma tras la amenaza. Esta interacción es esencial para regular funciones vitales y adaptarse a los cambios en el entorno.

**TRANSFORMADA WAVELET** 
La transformada wavelet es un método que descompone una señal en componentes de diversas escalas y posiciones. A diferencia de la transformada de Fourier, que representa señales mediante funciones sinusoidales (senoides), la transformada wavelet utiliza funciones llamadas wavelets, que son ondas pequeñas y asimétricas. Esta característica permite capturar tanto la información de frecuencia como la de tiempo, lo que resulta especialmente útil para señales que presentan cambios rápidos.

- **Usos de la Transformada Wavelet:**  La transformada wavelet tiene diversas aplicaciones en el análisis de señales biológicas, destacando su uso en el análisis de señales electrocardiográficas (ECG) para detectar arritmias y otras anomalías cardíacas. Se han desarrollado algoritmos que utilizan wavelets para identificar características específicas en registros de ECG, logrando así una alta precisión en el diagnóstico. Además, en el procesamiento de señales de electroencefalografía (EEG), facilita la eliminación de ruido y artefactos, mejorando la visualización y análisis de las ondas cerebrales. La transformada wavelet también se combina con técnicas como las máquinas de soporte vectorial para clasificar diferentes tipos de arritmias cardíacas a partir de las características extraídas. Asimismo, se utiliza en la compresión de datos en imágenes médicas y señales biológicas, permitiendo mantener la información esencial mientras se reduce el tamaño del archivo.

- **Tipos de Wavelets Utilizadas en Señales Biológicas:** Existen varias familias de wavelets utilizadas en el análisis de señales biológicas. Las ondículas Haar son las más simples y las primeras en ser empleadas, consistentes en funciones de escalada. Las ondículas Daubechies , denominadas dbN (donde N es el orden), son reconocidas por su capacidad para proporcionar una buena aproximación y compresión de datos. Las ondículas Symlets son variantes simétricas de las Daubechies, diseñadas para mejorar la simetría en la representación de las señales. Por otro lado, los coiflets ofrecen propiedades similares a las Daubechies, pero presentan un mayor número de ceros en sus momentos. Finalmente, el sombrero mexicano (Mexican Hat Wavelet) es especialmente útil para detectar bordes y transiciones en las señales.
  
Para este análisis en particular, se utilizará la ondícula Morlet, una función empleada en el análisis de señales a través de la transformada wavelet. Esta ondícula combina características de la transformada de Fourier con la capacidad de proporcionar información tanto temporal como frecuencial.

Para comprender el plan de acción que se implementará durante la práctica de laboratorio, se ha elaborado un diagrama de flujo. Este diagrama proporciona una representación visual clara de las etapas y procedimientos que se seguirán, facilitando la organización y la ejecución del trabajo. Al incluir cada paso del proceso, desde la preparación inicial hasta la recopilación y análisis de datos, el diagrama ayuda a garantizar que todos los participantes estén alineados y que se sigan los protocolos establecidos de manera eficiente. 

![image](https://github.com/user-attachments/assets/029aa2ff-cffe-4eb0-9027-f758c0f7be67)


**1.	Adquisición de la señal ECG :**

Para comenzar, es esencial colocar los electrodos de superficie sobre la piel del usuario, asegurando una buena adherencia mediante gel conductor para optimizar la captación de señales. Estos electrodos están conectados al AD8232, un circuito integrado diseñado específicamente para la adquisición y procesamiento de señales biopotenciales, como las generadas en un electrocardiograma (ECG). Este circuito puede extraer, amplificar y filtrar señales de baja amplitud en entornos con ruido. El AD8232, responsable del procesamiento de las señales, se conecta en serie a una placa STM. Mediante programación, se desarrolló una interfaz gráfica que permite visualizar en tiempo real la actividad eléctrica del corazón y almacenar los datos adquiridos. En total, se registraron 30000 datos en un intervalo de 5 minutos, durante el cual el usuario permaneció en estado de reposo para minimizar el ruido experimental.


  ![image](https://github.com/user-attachments/assets/9868ca03-7ba7-40e3-985e-1772cee02403)


Los electrodos se colocan estratégicamente en el pecho del usuario para captar la señal de manera óptima. El electrodo rojo (R) se ubicó debajo de la clavícula derecha, el electrodo amarillo (L) debajo de la clavícula izquierda, y el electrodo verde, que actúa como tierra (F), se situó en la zona de las costillas.


![image](https://github.com/user-attachments/assets/81357e9b-66e8-449f-84a6-c17de961f84d)


La frecuencia de muestreo en electrocardiografía es el número de muestras tomadas por segundo de la señal eléctrica del corazón. Este parámetro es fundamental para asegurar que la actividad cardíaca se registre con precisión y detalle suficiente para realizar un análisis de diagnóstico efectivo. Para un análisis básico de ECG, se recomienda una frecuencia de muestreo mínima de 500 muestras por segundo (MPS), lo cual es adecuado para capturar las características principales del trazado electrocardiográfico, como las ondas P, QRS y T.

Una frecuencia de muestreo adecuada permite que los detalles críticos de la señal cardíaca, especialmente en las áreas de cambio rápido, como el complejo QRS, se registren sin pérdida de información, minimizando errores en el procesamiento y análisis de la señal.


![image](https://github.com/user-attachments/assets/5c1f5211-2154-44c6-9c16-9fade93fbda3)


> **Ejes de la Gráfica:**
> > **-El eje horizontal (Tiempo [s]):** Representa el tiempo transcurrido durante el registro del ECG.

> > **-El eje vertical (Amplitud [mV]):** Representa la amplitud de las señales eléctricas del corazón.

**2.	Pre-procesamiento de la señal :**
Para el proceso de filtrado, se cambió de un filtro pasa bajo a un filtro pasa banda, considerando las diferencias en su funcionamiento:

- **Filtro pasa bajo:** Este tipo de filtro permite el paso de señales cuyas frecuencias están por debajo de una frecuencia de corte determinada, atenuando las frecuencias superiores. Su función de transferencia muestra una disminución de la ganancia a medida que las frecuencias superan el valor de corte.

- **Filtro pasa banda:** A diferencia del filtro pasa bajo, el filtro pasa banda permite el paso de un rango específico de frecuencias, conocido como la banda de paso, mientras atenúa las frecuencias que se encuentran por debajo y por encima de este rango. En este contexto, la creación de un filtro pasa banda se logra al conectar en serie un filtro pasa alto y un filtro pasa bajo, lo cual permite seleccionar únicamente un rango específico de frecuencias (la banda de paso) y atenúa las frecuencias que quedan fuera de este rango.

![image](https://github.com/user-attachments/assets/ed5f3891-c56d-482f-868e-6e26ceb5ff1b)

![image](https://github.com/user-attachments/assets/3234ffb0-ff01-402a-8a23-56a9389c6c34)


Con base en lo anterior, se diseñó un filtro pasa bajo con una frecuencia de corte de 0.5 Hz y una atenuación a 60 Hz. luego, se definió la amplitud en dB y se evaluó el orden del filtro, obteniendo un filtro de cuarto orden. Posteriormente, se calculó el polinomio característico del filtro Butterworth. Para cumplir con los requisitos de frecuencia, el filtro pasa bajo diseñado se transformó en un filtro pasa banda con frecuencias de corte ajustadas a 500 Hz, sustituyendo los valores correspondientes en la ecuación característica para obtener el filtro final.

Después del proceso de filtrado, la señal fue normalizada para mantener sus valores dentro de un rango estándar de -1 a 1, asegurando que la amplitud permanezca controlada y óptima para el procesamiento posterior.

![image](https://github.com/user-attachments/assets/75f399dd-3aba-455b-b054-52c9ba62ebb2)


> **Diseño del filtro:**
> > **•	Frecuencia de corte baja (fL):** 0.5 Hz

> > **•	Frecuencia de corte alta (fH):** 40 Hz

> > **•	Frecuencia de muestreo (fs):** 500 Hz

> > **•	Atenuación fuera de la banda:** 60 Hz

> > **•	Orden del filtro:** Butterworth orden 4


![image](https://github.com/user-attachments/assets/98f18aab-5524-462e-99d7-538cdbe7ffa8)


Se identificaron los picos R estos son componentes clave en la señal de un electrocardiograma (ECG), ya que representan la despolarización de los ventrículos del corazón. Se calcularon los intervalos RR, un parámetro fundamental en electrocardiografía que se refiere al tiempo transcurrido entre dos ondas R consecutivas. Este intervalo se mide desde el inicio de una onda R hasta el inicio de la siguiente. El intervalo RR representa la latencia entre despolarizaciones sucesivas de los ventrículos, lo que corresponde a un ciclo cardíaco completo. Su análisis es fundamental para evaluar la frecuencia cardíaca y la regularidad del ritmo. Para facilitar la visualización y comprensión de los picos R, se extrajo una porción de la señal, lo que permite identificar de manera más clara las características de las ondas y su relación con el ciclo cardíaco.


![image](https://github.com/user-attachments/assets/6190628b-8b5a-4000-878d-b517da25aabf)

![image](https://github.com/user-attachments/assets/60f0d71e-6f5f-4dd8-8638-d91c34a5a2b3)


**3.	Análisis de la HRV en el dominio del tiempo**

**Media de los intervalos RR:** Este parámetro es fundamental en electrocardiografía, ya que se utiliza para evaluar tanto la frecuencia cardíaca como la variabilidad de la frecuencia cardíaca (HRV). La media de los intervalos RR se calcula promediando todos los intervalos registrados durante un período específico, sumando los intervalos y dividiendo el total por la cantidad de mediciones. En nuestra señal, la media de los intervalos RR fue de 0,6519 segundos **(651,9 ms)**.

Este valor de 0,6519 segundos indica el tiempo promedio que transcurre entre dos latidos consecutivos del corazón, lo cual es esencial para comprender la frecuencia cardíaca promedio. Una media más baja sugiere una frecuencia cardíaca más alta, mientras que una media más alta indica una frecuencia cardíaca más baja, lo que proporciona información valiosa sobre el estado general del sistema cardiovascular.

- **Frecuencia Cardíaca Promedio:** Se puede calcular utilizando la fórmula


![image](https://github.com/user-attachments/assets/4c0cd58b-7204-4651-8503-5a2bde7d30e8)

- **Sustituyendo los medios:**
  

![image](https://github.com/user-attachments/assets/1b4445d6-5784-4678-ad06-f2eb1741ca6e)


Este valor sugiere una frecuencia cardíaca moderadamente elevada, que podría estar influenciada por factores como el estrés, la actividad física o el estado emocional del individuo.

**Desviación estándar de los intervalos RR:** Este valor corresponde a la desviación estándar de todos los intervalos RR medidos durante el mismo período. Al ser independiente de la frecuencia cardíaca, este indicador es útil para evaluar la variabilidad general del ritmo cardíaco. La desviación estándar ofrece información valiosa sobre las fluctuaciones en los tiempos entre latidos sucesivos del corazón, lo que facilita una comprensión más profunda de la estabilidad y el funcionamiento del sistema cardiovascular. En nuestra señal, la desviación estándar de los intervalos RR fue de 0,2689 segundos **(268,9 ms)**.

Este valor de 0,2689 segundos indica la variabilidad en los intervalos RR. Un valor relativamente alto de desviación estándar sugiere una mayor variabilidad en los intervalos RR, lo que puede reflejar una respuesta activa del sistema nervioso autónomo, en particular del sistema parasimpático, que regula la frecuencia cardíaca. En general, una desviación estándar baja se asocia con un ritmo cardíaco más constante y menos influenciado por factores externos. Por el contrario, una alta variabilidad puede ser indicativa de un mejor estado de salud cardiovascular y de una mayor capacidad del organismo para adaptarse a cambios fisiológicos.
En total, se identifican 458 complejos R a lo largo de toda la señal. A continuación, se presentan los primeros valores de los intervalos RR, en segundos, los cuales representan la diferencia temporal entre las ocurrencias sucesivas de la onda R en el electrocardiograma (ECG). 

> **Intervalos R-R (en segundos):**
> > [0.540018  - 0.53001767 0.540018 -  0.53001767  - 0.540018 -  0.52001733  -  
 0.52001733 - 0.53001767  -  0.53001767  -  0.52001733 - 0.53001767  -  0.52001733  -  
 0.510017 -  0.52001733  -  0.510017  -  0.990033  -  0.960032  -  0.97003233  -  
 0.930031  -  0.95003167   -  0.50001667  -   0.55001833  -  0.540018  -  0.55001833  -  
 0.56001867  -  0.570019  -  0.570019 -  0.58001933 -  0.570019  -  1.110037  -  
 0.540018  -  0.50001667  -  1.00003333   -  0.98003267  -  1.45004833 - 0.97003233  -  
 0.55001833  -  1.21004033  -  0.64002133   -  0.68002267   -  0.70002333  -   0.67002233  -  
 0.61002033   -  0.58001933  -  0.56001867   -  0.570019   -   0.56001867   -   0.56001867  -  
 0.56001867   -   0.55001833   -   0.56001867   -   0.56001867   -   0.56001867   -   0.540018  -  
 0.53001767   -   0.52001733   -   0.510017    -   1.03003433   -   0.53001767   -   0.540018  -  
 0.540018   -  0.540018   -   0.56001867   -   0.55001833  -    0.56001867   -   0.56001867  -  
 1.07003567   -   0.52001733 0.510017   -   0.50001667   -   0.510017   -   1.00003333  -  
 0.510017   -  0.50001667   -   0.50001667   -   1.42004733   -   0.92003067 1.410047  -  
 0.50001667   -   0.50001667   -   0.50001667   -   0.510017    -   0.510017   -   0.510017  -  
 0.510017   -  1.04003467   -   0.50001667   -   0.50001667   -   0.510017   -   0.52001733  -  
 0.52001733 0.510017   -   0.540018    -    0.510017   -   0.52001733   -  0.510017 ]

**4.	Aplicación de transformada Wavelet**


![image](https://github.com/user-attachments/assets/d3232779-1dec-4bbf-8a71-b4ee0b8ef8c5)


> **Ejes de la Gráfica:**
> > **-El eje horizontal:** Representa el tiempo transcurrido durante el registro de los intervalos RR. Esto permite observar cómo varían los patrones de frecuencia a lo largo del tiempo.

> > **-El eje vertical:** muestra las diferentes escalas o frecuencias. Las frecuencias más bajas corresponden a variaciones más lentas en el ritmo cardíaco, mientras que las frecuencias más altas reflejan cambios más rápidos.

Se empleó la transformada wavelet continua (CWT) con la wavelet de Morlet esta es una herramienta eficaz para analizar la variación de la potencia espectral de una señal a través del tiempo y en diferentes bandas de frecuencia. En el espectrograma mostrado, se aplicó el CWT sobre datos de variabilidad de la frecuencia cardíaca (HRV) para identificar cambios en las frecuencias bajas y altas a lo largo del tiempo. La wavelet de Morlet, una de las funciones base más utilizadas en la CWT, consiste en una onda sinusoidal modulada por una envolvente gaussiana. Esta configuración permite capturar tanto la información temporal como frecuencial de la señal, logrando un equilibrio óptimo entre precisión temporal y de frecuencia. Esto la hace especialmente adecuada para el análisis de señales no estacionarias, como la HRV, en las que tanto las frecuencias como sus potencias varían con el tiempo.

 En el espectrograma, la intensidad de color o luminosidad refleja la energía o potencia de las distintas frecuencias en cada instante de tiempo. Las áreas más brillantes o con colores más intensos indican una mayor energía en una frecuencia específica en ese momento. Los colores también representan la magnitud o potencia de la señal: los tonos cálidos (rojo, amarillo) corresponden a una alta potencia, mientras que los tonos fríos (azul) indican una baja potencia.

**Banda de Baja Frecuencia (0,04 - 0,15 Hz):** Esta banda está vinculada a la actividad tanto simpática como parasimpática del sistema nervioso. A lo largo del tiempo, se pueden observar cambios en la potencia de esta banda. Si en el espectrograma aparecen áreas con colores más cálidos en la banda de baja frecuencia (LF), esto sugiere un aumento en la actividad de estas frecuencias, lo cual podría asociarse con una respuesta de estrés o con la activación del sistema nervioso simpático.

**Banda de Alta Frecuencia (0,15- 0,4):** Esta banda generalmente refleja la actividad parasimpática, la cual está principalmente regulada por la respiración. Cualquier cambio notable en la potencia de esta banda podría indicar variaciones en la respuesta parasimpática, como procesos de relajación o ajustes en el patrón respiratorio.

**Análisis Crítico de Cambios en la Potencia Espectral:** La CWT facilito la observación de cómo varían estas frecuencias en potencia a lo largo del tiempo. Por ejemplo, si en un segmento específico se observa un aumento en la potencia de la banda de baja frecuencia, esto podría interpretarse como un incremento en la actividad simpática, lo que podría estar asociado a situaciones de estrés o esfuerzo físico. En cambio, una disminución en la potencia de estas frecuencias podría indicar un estado de relajación o recuperación.

### INSTRUCCIONES 
Este código está diseñado para ser utilizado en la plataforma Spyder. Para ejecutarlo correctamente, sigue estos pasos:

**1.	Instalación de librerías:** Asegúrate de instalar las librerías necesarias en la consola usando los siguientes comandos:

>	 pip install PyWavelets

> pip install numpy

>	 pip install matplotlib
