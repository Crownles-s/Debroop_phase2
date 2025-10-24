# 1. miniRSA
Let's decrypt this: ciphertext? Something seems a bit small.

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
- Alternate tangent 1: 

## Resources:
- RSA Explanation (https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/)
- Explanation of N, e, c, p and q (https://en.wikipedia.org/wiki/RSA_cryptosystem#:~:text=e%20having%20a%20short%20bit,the%20algorithm%20works%20as%20well.)
- About small e attacks (https://cic.iacr.org/p/1/3/29)
- Ciphertext decode via small e attack (https://www.dcode.fr/rsa-cipher)
