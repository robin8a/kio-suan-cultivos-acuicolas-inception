# Referencias
- https://colombiatic.mintic.gov.co/679/articles-124767_recurso_1.pdf
- https://app.cloudcraft.co/
  
# Arquitectura de Software
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

## Base de datos
- Funciones Lambda de AWS que se dispara con un Evento de IoT de los raspberries y guarda la información a través de un API (AppSync) en una Base de datos no relacional (DynamoDB) 
  


# Modelo Entidad Relación
![ER](./_images/ER_Diagram.drawio.png)
