# 1. miniRSA
Let's decrypt this: [ciphertext](../assets/ciphertext)? Something seems a bit small.

## Solution:
- Open the given link, which downloads a text(?) file. I could not see what file type it was, even in Properties.
- Since all the text was readable, it was not an issue.
- Next, I noticed some things labelled e, N and c.
- Searching up RSA techniques revealed the meanings of these labels.
- The challenge description points to a small e attack. Search for an RSA decoder leads to many websites.
- I chose a website with explicit support for small e attacks. Here, I entered N, c and e.
- The final output after the successful small e attack is the flag.

![RSA Attack website](../assets/Screenshot%202025-10-24%20192306.png?raw=true)

## Flag:

```
picoCTF{n33d_a_lArg3r_e_d0cd6eae}
```

## Concepts learnt:
- RSA encryption and decryption using public and private keys.
- Uses of ciphertext (c), base (e), and modulus (N).
- Methods of RSA attacks and small e attacks.
- Pitfalls of having a small and easily cracked e value, as well as massive advantages of a larger e.
- Other methods of RSA cracking including factoring p andc q when e is sufficiently large. This seems to need a private key and d value.

## Notes:
- Did not go for any alternate tangents. 

## Resources:
- RSA Explanation (https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/)
- Explanation of N, e, c, p and q (https://en.wikipedia.org/wiki/RSA_cryptosystem#:~:text=e%20having%20a%20short%20bit,the%20algorithm%20works%20as%20well.)
- About small e attacks (https://cic.iacr.org/p/1/3/29)
- Ciphertext decode via small e attack (https://www.dcode.fr/rsa-cipher)

# 2. Custom encryption

Can you get sense of this code file and write the function that will decode the given encrypted file content.
Find the encrypted file here [flag_info](../assets/enc_flag) and [code file](../assets/custom_encryption.py) might be good to analyze and get the flag.


## Solution:
- Open the given links, which download a text file and a python script.
- Import the python file into vscode.
- The python script is an encryption sequence that appears to be using a and b to ENCRYPT a sequence.
- Since I have my own a and b, I need to somehow construct a decryption script and use that with the a, b and cipher to get the flag.
- On reading the script, I saw multiple functions. A generator function took 3 variables and performed a simple arithmatic operation, isPrime returns true and false based on prime or not, were the two I understood easily.
- To get the decrypt script I need to reverse all the operations.
- It also uses 2 values p and g for the encryption, 97 and 31 respectively.
- To reverse, we need to reverse each operation.
- First, I tried to interpret all the operations using resources 3, 4 and 5.
- Then, I looked closer at each function and also the test function to see the order of calls and returns, like the main function in C. I assumed that the proper order must be known to effectively reverse the encryption.
- I was not sure what format to enter the cipher in, so I just used the exact format first.
- Next, I found some redundant code, because p and q are prime here.

```py
if not is_prime(p) and not is_prime(g):
print("Enter prime numbers")
return

```
- Again, I did not need the following code because I already had a and b, and did not need them randomised.

```py
a = randint(p-10, p)
b = randint(g-10, g)

```
- After this, the code uses p, q, a and b to generate u and v respectively using simple arithmetic in generator function.
- Then, p, a, b, u and v are used to make a key and a b_key again using generator function.
- The key and b_key appear to be designed to be equal. That value then becomes a shared key.
- Then, a semi cipher is constructed using the dynamic xor func with the flag and shared key as input.
- That is furthur encrypted to a full cipher using the encrypt func and semi cipher and shared key as input.
- Since test func in now deciphered, I looked at the others. isPrime is also understood and has no impact on my program, since I already have primes.
- Generator func is also easy to understand, being just a power and a modulud function. encrypt takes every character (for char in plaintext), uses ord to find the ascii values and multiplies it by 311 and the key, same as the shared_key and b_key.
- For reversing encrypt, we can take the characters, divide them by 311 and the shared_key. Then, use the chr function to reverse the function of ord.
- The actual main function passes a message and "trudeau" to the test function. The test function treats the message as the plaintext flag and the "trudeau" as a text_key. The dynamic_xor function also gets the same input.
- The xor function makes a key_length that calculates the length of text_key, which is always 7 from trudeau.
- Then, the plaintext flag is reversed using [::-1].
- Then, each character of the text_key is chosen in a cycle of key_length=7, using modulus function so the value goes from 0 to 7 and back. This is stored in key_char.
- Then, the char is encrypted using the ord of key_char and char (from the plaintext) and converted back to letters using chr.
- The blank cipher_text defined at the start is used to store each encrypted letter, and the final encrypted ciphertext is returned to test func.
- XOR is self-inversing. Thus using the cipher as input will return the original flag as output. So, thats what we can do to reverse this without extra coding.
- Now to build the decryption code, I will first define every known value and then calculate the shared_key using the same code as the original generator function.

```py
a = 94
b = 29
p = 97
g = 31
cipher = [260307, 491691, 491691, 2487378, 2516301, 0, 1966764, 1879995, 1995687, 1214766, 0, 2400609, 607383, 144615, 1966764, 0, 636306, 2487378, 28923, 1793226, 694152, 780921, 173538, 173538, 491691, 173538, 751998, 1475073, 925536, 1417227, 751998, 202461, 347076, 491691]
text_key = "trudeau"

u = pow(g, a, p)
v = pow(g, b, p)
#shared_key, key and b_key are same. Thus I can use pow(v, a, p) or pow(u, b, p).
shared_key = pow(v, a, p)
```

- Next, I will retrace the path of the test function.
- Thus, first i need to convert the cipher to semi-cipher by reversing the encrypt function. So, calculate the divider, divide the characters by using index i to select each character, divide and lastly convert back to a letter using chr.

```py
divider = shared_key * 311
semi_cipher = ""
for i in cipher:
    char_temp = i // divider
    semi_cipher += chr(char_temp)
```
- Next, reverse the XOR encryption to convert semi cipher back to plaintext. Use the same exact code as in original function, just with renamed variables for better clarity.

```py
rev = ""
for i, char in enumerate(semi_cipher):
    key_char = text_key[i % len(text_key)]
    rev += chr(ord(char) ^ ord(key_char))
```

- Lastly, use [::-1] to reverse the plaintext back to normal.

```py
flag = rev[::-1]
print(flag)
```

Finally, the full [Decryption code](../assets/decryption.py)

## Flag:

```
picoCTF{custom_d2cr0pt6d_751a22dc}
```

## Concepts learnt:
- XOR encryption syntaxes and self reversability.
- Python fundamentals: Operators (arithmetic and logical), loops, function definition and some builtins.
- Python code syntax
- General cryptography script syntaxes as well as reverse enginerring them when possible.

## Notes:
- Alternate tangent 1: Tried to reverse the XOR encryption before knowing that it self reverses.
- Alternate tangent 2: Tried web tools for easy decryption but could not find any.

## Resources:
- Information about cryptography in python (https://www.askpython.com/python/examples/rsa-algorithm-in-python)
- Ord function (https://www.w3schools.com/python/ref\_func\_ord.asp)
- Python arithmetic (https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp)
- Logical operators (https://www.geeksforgeeks.org/python/python-logical-operators/)
- Curled braces explanation (https://www.geeksforgeeks.org/python/parentheses-square-brackets-and-curly-braces-in-python/)
- Len Function (https://www.w3schools.com/python/ref_func_len.asp)
- Undoing ord function with chr (https://stackoverflow.com/questions/29818519/what-is-the-opposite-of-pythons-ord-function)
- Meaning of [::-1] (https://stackoverflow.com/questions/31633635/what-is-the-meaning-of-inta-1-in-python)
- // function (https://www.freecodecamp.org/news/what-does-double-slash-mean-in-python/)
- About XOR encryption (https://stackoverflow.com/questions/14279866/what-is-the-inverse-function-to-xor)
- Python For loops (https://www.w3schools.com/python/python_for_loops.asp)

# 3. rsa-oracle
Can you abuse the oracle?
An attacker was able to intercept communications between a bank and a fintech company. They managed to get the message [(ciphertext)](../assets/secret.enc) and the [password](../assets/password.enc) that was used to encrypt the message.

- Hint 1: Crytography Threat models: chosen plaintext attack.
- Hint 2: OpenSSL can be used to decrypt the message. e.g openssl enc -aes-256-cbc -d ...
- Hint 3: The key to getting the flag is by sending a custom message to the server by taking advantage of the RSA encryption algorithm.
- Hint 4: Minimum requirements for a useful cryptosystem is CPA security.

## Solution:
- Open the given links to download 2 enc files. Lookin up enc files shows that they are generic encoded files.
- Opening the passwords file shows a number, while the secrets file is unreadable.
- On running the netcat with random values, we see the encryption code to be `m ^ e mod n` and decryption to be `c ^ d mod n`.
- We see another line `encoded length must be less than keysize`.
- Looking up keysize, we see that m must be less than n.
- Now, to decode we need n.
- Using the hints, we see CPA or chosen plaintext attacks.
- Looked up padding methods and decryption methods.
- Results showed some techniques. The most common one, Bleichenbacher Attack, needed us to know n.
- I understood that brute forcing an n calculation will be impossible. So, I looked closer at modular arithmetic, and especially at the multiplicative property of RSA `decrypt (c1 * c2 mod n) = decrypt (c1) * decrypt (c2) mod n`
- I need to encrypt a chosen plaintext value, multiply with the password, decrypt the multiplication, and divide by the plaintext.
- Using this method, I got a decimal output with unreadable ascii characters. So, convert to hex and then to ascii, I got the password `92d53`.
- Now, I installed openSSL and ran the decryption code with the key.
```
C:\Users\DEBROOP>openssl enc -aes-256-cbc -d -in "C:\Users\DEBROOP\Downloads\secret.enc" -k 92d53
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
picoCTF{su((3ss_(r@ck1ng_r3@_92d53250}
```

## Flag:

```
picoCTF{su((3ss_(r@ck1ng_r3@_92d53250}
```

## Concepts learnt:
- Padded RSA encryption.
- Non-padded RSA GCD attack.
- Chosen-Plaintext Attacks.
- Python netcat fundamentals.
- RSA security strength.
- Abusing encryption oracles.
- Multiplicative properties of RSA using modular arithmetic.

## Notes:
- [Alternate tangent 1](../assets/alt1.md): 'Overflow' the netcat using a python [script](../assets/socket.py). Could not really understand where to go next.
- [Alternate tangent 2](../assets/alt2.md): Used normal [GCD](../assets/gcd_fail.py) factoring without considering padding.
- Alternate tangent 3: Tried different formats for the decrypted password.

## Resources:
- .enc information (https://www.reviversoft.com/en/file-extensions/enc)
- Modular arithmetic (https://en.wikipedia.org/wiki/Modular_arithmetic)
- Key size (https://en.wikipedia.org/wiki/Key_size)
- RSA oracle usage (https://en.wikipedia.org/wiki/RSA_cryptosystem#:~:text=by%20sending%20her%20random%20or%20maliciously%20crafted%20ciphertexts)
- n retrieval (https://cryptohack.gitbook.io/cryptobook/untitled/recovering-the-modulus)
- GCD in python (https://www.ccbp.in/blog/articles/gcd-of-two-numbers-in-python)
- Func definition with input and return (https://www.geeksforgeeks.org/python/python-functions/)
- Padding (https://medium.com/asecuritysite-when-bob-met-alice/so-how-does-padding-work-in-rsa-6b34a123ca1f)
- Attack method (https://medium.com/@c0D3M/bleichenbacher-attack-explained-bc630f88ff25)
- OpenSSL commands (https://www.youtube.com/watch?v=WweWxoPN5qI)
- Connect to netcat using python (https://gist.github.com/leonjza/adc69cadc3d8a5d4c068) and (https://stackoverflow.com/questions/1908878/netcat-implementation-in-python)
- Variables (https://www.w3schools.com/python/python_variables.asp)
