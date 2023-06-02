import socket
import time
import threading
from queue import Queue
socket.setdefaulttimeout(0.25) # sets the default time out for new sockets
# a print_lock is what is used to prevent "double" modification of shared variables.
# while one thread is using a variable, others cannot access
lck = threading.Lock()
q = Queue() # stores the port numbers to be scanned
target = input('Enter the host to be scanned: ')
print('Enter scanning mode :- ')
print('1. Scan standerd ports ')
print('2. Scan Reserved ports ') 
print('3. Scan important ports ') 
print('4. Scan user given ports ') 
mode = int(input("Enter mode : "))

def ports (m):
   if m == 1:
      for p in range(1, 1024): 
         q.put(p)
   elif m == 2:
      for p in range(1, 49152):
         q.put(p)
   elif m == 3:
      ports [20, 21, 22, 23, 25, 53, 80, 110, 443]
      for p in ports:
         q.put(p)
   elif m == 4:
      ports = input("Enter your ports (seperate by blank):")
      ports=ports.split()
      ports = list(map(int, ports))
      for p in ports:
         q.put(p)
ports(mode)

thr = int(input('Number of threads to use : '))
t_IP= socket.gethostbyname (target)
print ('Starting scan on host:', t_IP)
def portscan (port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket for IPv4 (address family) and TCP type of socket 
   try:
      con = s.connect((t_IP, port))
      with lck:
         print (port, 'is open')
         con.close()
   except:
      pass
def threader():
   while not q.empty():
      p = q.get() 
      portscan (p)
      q.task_done() #to let q.join() know all the tasks are done what and all were put in the queue
startTime = time.time()
for x in range (thr):
   t = threading.Thread (target = threader) # target is the function to be executed by the thread 
   t.daemon = True # kill all threads when main dies
   t.start() # start the thread
q.join() # Blocks until all items in the queue have been gotten and processed.
print('Time taken:', time.time() - startTime)