## Objetivo
- En esta actividad tiene como objetivo mostrar scripts en PowerShell para obtener cierta información de nuestra red. 

### Reseña del contenido 

- Hacemos uso de scripts en powershell, los cuales nos ayudan a realizar escaneos de puertos activos y escaneo de puertos a un equipo en específico.


  **scan_alivev1.ps1**: Este se centra en el escaneo de equipos activos en la subred, donde a través de la ejecución se obtiene la subred y se validan los activos en     esa subred. Y donde también se verifica la conexión con cada dirección IP.


  **scan_alivev2.ps1**: Este script obtiene la puerta de enlace y el rango de subred para así después buscar los puertos abiertos y así verifica la conexión.


  **scan_portv1.ps1**: Por último, este script permite escanear y validar la disponibilidad de hosts en una subred, y detectar puertos abiertos en una dirección ip. 
