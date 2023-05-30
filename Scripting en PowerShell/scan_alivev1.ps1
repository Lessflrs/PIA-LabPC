#LESSLIE MONTSERRAT MEDELLIN FLORES
#1960113

#Escaneo de equipos activos en la subred 
#
#Determinando gateway 
$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "Tu gateway: $subred"
#
#Determinando rango de subred 
#
$rango = $subred.Substring(0,$subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') + 1).IndexOf('.') + 3 )
echo $rango 
#
## Determinando si $rango termina en "."
## En ocasiones el rango de subred no termna en punto, necesitamos formarlo.
#
$punto = $rango.EndsWith('.')
if ( $punto -like "False" )
{
    $rango = $rango + '.' #agregamos el punto en caso de que no estuviera.
}
#
##Creamos un array con 254 numeros (1 a 254) y se almacena 
##En una variable se llamara $rango_ip
#
$rango_ip = @(1..254)
#
## Generamos bucle foreach para validar host activos en nuestra subred
#
foreach ( $r in $rango_ip )
{
    $actual = $rango + $r #se agrega direccion ip
    $responde = Test-Connection $actual -Quiet -Count 1   # Validamos conexion contra ip en $actual
    if ( $responde -eq "True" ) 
    {
        Write-Output ""
        Write-Host " Host responde: " -NoNewline; Write-Host $actual -ForegroundColor Green
    }
}


Get-Date
