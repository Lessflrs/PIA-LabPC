#LESSLIE MONTSERRAT MEDELLIN FLORES 1960113
#1960113
import nmap

scanner = nmap.PortScanner()
scanner.scan('192.168...', '1024', '-v -sV')
print(scanner.command_line())
print(scanner.all_host())
print(scanner['192.168...'].state())
print(scanner['192.168...'].all_protocols())
print(scanner['192.168...']['tcp'].keys())
print(scanner['192.168...'].has_tcp(21))
print(scanner['192.168...'].has_tcp(22))
print(scanner['192.168...']['tcp'][22])
print(scanner['192.168...']['tcp'][22]['product'])
