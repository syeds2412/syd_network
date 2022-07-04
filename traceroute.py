import urllib
import time 
import datetime, threading
from bs4 import BeautifulSoup
import urllib.request
import subprocess
import socket


fp2=open("output.txt",'w')


#This function will be executed after every x minutes


def TraceRoute():



        hostname="google.com"
        fp2.write(hostname+"    :   ")
        print(hostname)

        #subprocess.call(['traceroute',hostname])

        traceroute = subprocess.Popen(["tracert", '-w', '100', hostname],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while (True):
                hop = traceroute.stdout.readline()
#                print(type(hop))
                if not hop: break
                print('-->',str(hop))
                fp2.write(str(hop))


        threading.Timer(60*50, TraceRoute).start() #Ensures periodic execution of TraceRoute( ) x=60*50 seconds

TraceRoute()