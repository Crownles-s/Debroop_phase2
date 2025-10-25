a = 94
b = 29
p = 97
g = 31
cipher = [260307, 491691, 491691, 2487378, 2516301, 0, 1966764, 1879995, 1995687, 1214766, 0, 2400609, 607383, 144615, 1966764, 0, 636306, 2487378, 28923, 1793226, 694152, 780921, 173538, 173538, 491691, 173538, 751998, 1475073, 925536, 1417227, 751998, 202461, 347076, 491691]
text_key = "trudeau"

u = pow(g, a, p)
v = pow(g, b, p)
#shared_key, key and b_key are same. Thus I can use pow(u, b, p) or pow(v, a, p).
shared_key = pow(v, a, p) 

divider = shared_key * 311
semi_cipher = ""
for i in cipher:
    char_temp = i // divider
    semi_cipher += chr(char_temp)

rev = ""
for i, char in enumerate(semi_cipher):
    key_char = text_key[i % len(text_key)]
    rev += chr(ord(char) ^ ord(key_char))

flag = rev[::-1]
print(flag)
