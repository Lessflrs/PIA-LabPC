#LESSLIE MONTSERRAT MEDELLIN  FLORES 
#1960113  

$portstoscan = @(20,21,22,23,25,50,51,53,80,110,119,135,136,137,138,139,143,161,162,389,443,445,636,1025,1443,3389,5985,8080,10000)
$waittime = 100

Write-Host "Direccion ip a escanear: " -NoNewline
$direccion = Read-Host 

foreach ( $p in $portstoscan )
{
    $TCPObject = new-object System.Net.Sockets.TcpClient 
        try{ $resultado = $TCPObject.ConnectAsync($direccion,$p).Wait($waittime)}catch{}
        if ( $resultado -eq "True")
        {
            Write-Host "Puerto abierto: " -NoNewline; Write-Host $p -ForegroundColor Green 
        }
}
Get-Date
