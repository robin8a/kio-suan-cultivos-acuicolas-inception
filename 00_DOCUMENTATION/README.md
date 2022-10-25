# Referencias
- https://colombiatic.mintic.gov.co/679/articles-124767_recurso_1.pdf
- https://app.cloudcraft.co/
  
# Arquitectura de Hardware/Software
![Componentes](./_images/arquitectura-webapp-cultivos-acuicolas-004.png)

## Captura de datos
### Raspberries Pi: 
- Dos rapberries Pi
- Capacidad de conexión a red movil (3G/4G) y Wifi (Redundacia)
- Doble tarjeta de red; una para Wifi y otra para que funciones como server y hotspot de otros dipositivos
- Interfaz offline servidor para descargar datos localmente en caso que no haya conexión de Internet
- Solución de energía (baterías, supresor de picos, apagado automático)
- Extraer, Tranformar, Cargar  y enviar los datos a través de MQTT IoT de AWS (pub/sub)
- AWS SQS para el encolamiento y gestión de  (*posible)

### Granja de dispositivo (IoT): 
- Conjunto de equipos que se integran a los raspberries Pi para enviar datos
- Ej. camaras, dispositivos de medición, formularios
- Parametros ambientales y calidad del agua (PH, temperatura, oxigenación, etc)

## Base de datos y archivos multimedia
- Funciones Lambda de AWS que se dispara con un Evento de IoT de los raspberries y guarda la información a través de un API (AppSync) en una Base de datos no relacional (DynamoDB) 
- Fuente de datos para entrenar los modelos de aprendizaje (ML)
- Fuente de datos para el frontend de la aplicación Webapp
- Correlación de mensajes de IoT con archivos multimedia (imágenes/video) para ser usados en el entrenamiento y "estado actual" del estanque

## Frontend
### Autenticación y autorización
- Cognito: Gestión de usuario, autenticación y autorización
### API
- Queries, Mutaciones (CRUD), Suscripciones (onCreate, onUpdate, onDelete)
- Graphql
- AWS AppSync

### Almacenamiento
- Amazon (S3 Simple Storage Service) para guardar los archivos


## Entrenamiento de modelos con datos y multimedia (Sagemaker)
- Con los datos de la base de datos entrenar los modelos
- Crear los algoritmos
- Procesar la imágenes
- Interpretar la imágenes
- Identicar imágenes


# Modelo Entidad Relación
![ER](./_images/ER_Diagram.drawio.png)

> En orden de importancia: 

## Device
- Son los dispositivos que están categorizados (Ejemplo: Capturas de video, Mediciones de Equipos, Mediciones Manuales)

## Feature
- Se pueden crear (1 a n) features
- Son las (caracteristicas, medidas, documentos, variables, etc) que se pueden asociar a un dispositivo
- Se les asocian unidades de medida (m, kg, m2, densidad, saturación_oxigeno etc)
- Un usuario puede verificar un feature y su documentación asociada

# Formulas
- Se crean fórmulas para realizar calculos especificos sobre variables 
- Se pueden tener diferentes versiones de la formulas y cálculos de las mismas
- Ecuaciones paso a pasa de resultados previos, y con ellos realizar un nuevo cálculo

# Document
- Asociado un dispositivo
- Categorizado 


# Automatización 
- Automatizar de la granja
- Cuanto pesa mi pez? 
- Comida entregada vs proteina en el pez
- Sustentable y economico
- Camara para detectar el tamanho y salud de pez (computing vision)
- Determinar cuando y cuanto se puede vender la producción
- Reproducir las condiciones ideales para el desarrollo de la acuicultura (IA) 
- Aumento de la productividad al mejorar la eficiencia alimentaria y el manejo de enfermedades en sus primeros estados 
- Favorece el muestreo de los peces al evitar estrés por la intervención permanente dentro de los estanques

> Que algoritmos vamos a implementar para lograr los puntos anteriores: 

# Algoritmos a entrenar:
> A traves del procesamiento de imágenes y entrenamiento de modelos de aprendizaje, se propone implementar:

## Algoritmo crecimiento
- Teniendo en cuenta las mediciones de los instrumentos como: (Temperatura, Oxigeno, Profundidad, Claridad del agua, etc)
- Determinar mortalidad
- Enfermedades
- Crecimiento
- Conversión alimenticia  gramos de comida en gramos de peso del pez (gramos_comida/gramos_pez)

## Algoritmos para determinar si es un pez y corte(crop) la imagen
- Identificar y aislar la imagen de un pez
- ![](./_images/identificacion_peces.png)
- Dejar en cuadro el pez
- ![](./_images/pez_identificado.png)
  
## Algoritmos para filtrado 
- Eliminar las imagenes difusas, o no claras o oscuras
  
## Algoritmos identificación 
- Identificar las partes de pez (aletas, cabeza, otras partes)
- ![](./_images/proprociones_aletas_cabeza.png)
- Determinar con las proporciones y correlación el tamanho del pez

## Algoritmos para determinar si un pez esta enfermo
- Deteccion de parasitos? Determinar el impacto de enfermedades en porcentaje en perdida de produccion, disminuir el trabajo de los granjero de tomas manuales
- Identificar manchas
- Identificar parásitos
- Con la deteccion de enfermades o parasitos. Mejores estrategias de prevencion de enfermedades; que porcentaje es %?

## Algoritmos identificación de comportamiento
- Nivel de flotabilidad

## Algoritmo para determinar el peso
- Como referencia un plano en 3D determinar la proporciones y peso
  
## Algoritmo para identificar individualmente cada pez
- Realizar el conteo con reconocimiento facial de un pez, cada pez tiene la cara unica (manchas), o manchas en el cuerpo
- Seguimiento del origen del pez con Blockchain trazabilidad del criador a la mesa
  
## Algoritmos para contar los pellets de comida y cuantos se van al fondo
- Cuanto es el porcentaje de costo de la comida?
- De lo pellets de alimentacion cuanto se aprovecha

# Fuentes de datos (Entrenar para los algoritmos)
- Mediciones de los dispositvos
- Imágenes procesadas y filtradas
- Videos
- Mediciones de campo

# Algoritmos 
Cual algoritmo escoger para resolver un problema en especifico?
Afinar los algoritmos, para lograr los mejores resultados

## Evitar 
- Identificar y prevenir sobre ajuste
- Lograr resultado consistentes
- Que los modelos sean escalable con datos masivos

# Ingenieria de Datos (ETL)
- Creacion de los repositorios de ML
- Identificar e implementar la solucion de ingestion de datos
- Identificar e implementar la solucion de transformacion de datos

Almacenar => Transformar => Transmitir => Flujos de trabajo

## Almacenar
- S3 Data lakes
- DynamoDB

## Ciclo de vida
- No es necesario definir en esta etapa un ciclo; con el objetivo de disminuir los costos de almacenamiento
- Stardard Availability 99.99%, AZs >=3, Costo por 1000 request GET: $0.0004 POST: $0.005 USD
- S3 tiene un durabilidad de 99.99999999999 == (11 9's)



## Tranformar
- Glue
- Glue ETL

## Transmision
- Kinesis
- Kenesis Video transmision

## Workflows
- Data pipelines
- AWS Batch
- Funciones paso a paso

# Análisis Exploratorio de Datos
- 