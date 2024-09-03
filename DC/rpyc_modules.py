import rpyc
import sys

c = rpyc.classic.connect("localhost")

while True: 
   client_message = input("Enter your message : ")
   c.execute(f"client_message = '{client_message}'")

   if client_message == "stop":
      break;
   c.execute("""print(f"Client Message: {client_message}")
server_message = input("Enter your message : ")
print(f"Server Message: {server_message}")""")

   with rpyc.classic.redirected_stdio(c):
      c.execute("""print(f"Client Message: {client_message}")
print(f"Server Message: {server_message}")""")
   
