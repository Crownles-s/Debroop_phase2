- First, I can try to overload the system. By sending large input and see where it fails. I made a python code to input strings of specified length as input and send it.
- First, I connected to the netcat. Since host and port chnages when instance is closed, I kept them as variables.
```py
import socket
def snd(h, p, main):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((h, p))
```
- Taking ms as my injection to the netcat, looping using m, sending 2 different things with \n so I can send E/D and the string. encode, decode and s.recv values.
```py
for m in main:
    s.sendall((m + '\n').encode())
    r = s.recv(4096)
    print("Reply:", r.decode())
```
- Defining host and port. Fill in port manually later according to instance.
```py
h = "titan.picoctf.net"
p =
```
- Now, to put my inputs. E or D, and then the number of things to input. Make a string to store the entire value of the big inject string.
```py
op = input("Enter operation (E or D): ")
n = int(input("Number: "))
main = []
```
- Loop till n to get the long string.
```py
for i in range(n):
    x = input(f"String {i+1}: ")
    main.append(f"{op} {x}")
```
- Send the now defined values.
```py
snd(h, p, main)
```
