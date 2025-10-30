import socket
def snd(h, p, main):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((h, p))

for m in main:
    s.sendall((m + '\n').encode())
    r = s.recv(4096)
    print("Reply:", r.decode())

h = "titan.picoctf.net"
p = 63366

op = input("Enter operation (E or D): ")
n = int(input("Number: "))
main = []

for i in range(n):
    x = input(f"String {i+1}: ")
    main.append(f"{op} {x}")

snd(h, p, main)