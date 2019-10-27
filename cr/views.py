from django.shortcuts import render
import socket
# Create your views here.
def emergency(requesy):
    host_name=socket.gethostname()
    get_ip= socket.gethostbyname(host_name)

