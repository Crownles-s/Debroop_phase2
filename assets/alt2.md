- To decode n, we MUST use the oracle as we must use multiple attempts to determine n.
- Using C1 and C2, we will have m1^e mod n and m2^e mod n. N can be found using gcd(C1-M1^e, C2-M2^e).
- Researching furthur, I found that both C and python could perform these operations. I chose python because of better builtins. First, import math for all functions.
```py
import math
```
- Then, define variables and everything I know. I need to  do this because I must iterate with at least 2 or 3 different m1 and C1.
```py
m1 = 
m2 = 
C1 = 
C2 = 
e = 65537
```
- Then, I learned to make returning python funtions and found how to find GCD.
```py
def get_n(m1, m2, C1, C2, e):
 m_pow1 = pow(m1, e)
 m_pow2 = pow(m2, e)
 d1 = m_pow1 - C1
 d2 = m_pow2 - C2
return math.gcd(d1, d2)
```
- Now, invoke the function to get GCD.
```py
n = get_n(m1, m2, C1, C2, e)
print("n:", n)
```
- Now, use the oracle to get 2 values of C for 2 m's. And then input and run the script.
- Using m1 and m2 as 10 and 20 outputs n as 2. This appears to be a factor, as n must be greater than 10 AND 20.
- Using more complex values for full n.
- Complex values gave n=1. So, I saw that hex was used before encoding and decoded to try changing the m values to hex before gcd. Did not work.
- When searching why, its because OpenSSL has padding.
