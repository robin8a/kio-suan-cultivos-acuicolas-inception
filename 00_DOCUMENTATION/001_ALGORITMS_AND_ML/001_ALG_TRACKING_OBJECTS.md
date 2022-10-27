# Video Frame Object Tracking 
> El objetivo principal es hacer el seguimiento individual de los peces y registrar la posición espacial (x, y, z), para determinar patrones de comportamiento de los peces


# Referencias
- Documentación a implementar: https://docs.aws.amazon.com/sagemaker/latest/dg/sms-video-object-tracking.html
![Marcación y seguimiento](../_images/_object_tracking/ot_predict_next.gif)

# Dataset

## Peces en el estanque 
- Por cada pez se va a guardar la posición X, Y, Z durante un periodo t (tiempo), respecto a un punto de referencia K

## Comportamientos
- Debemos contar con las trayectorias x, y, z que hace un pez cuando tiene hambre
- Debemos contar con las trayectorias x, y, z que hace un pez cuando esta en un ciclo reproductivo
- Debemos contar con las trayectorias x, y, z que hace un pez cuando esta enfermo
