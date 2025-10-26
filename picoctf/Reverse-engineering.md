# 1. ARMassembly 1
- For what argument does this program print `win` with variables 79, 7 and 3? File: [chall_1.S](../assets/chall_1.S) 
- Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## Solution:
- Open the given link, which downloads a .S file. On searching, it is revealed to be an Assembly source file.
- The first line specifies the assembly architecture: ARM v8 A. So, I have context for the rest of the program.
- Now, I used resources to decode the program.

```
- A stack is created, along with registers w0 and w1.
- Subtracted 32 from stack, so stack size is set to 32. So, there are sp to sp+32 positions available.
- The register w0 is placed at stack+12 position.
- The move function mov is used to put 79 into register w0.
- Then, moved w0 to stack+16 position.
- Uses the same steps to put 7 and 3 into sp+20 and sp+24 respectively.
- Uses ldr to load 7 in register w0 and 79 into w1 by calling on their stack positions.
- lsl shifts w1 to the left, which always multiplies any decimal by 2.
- However, since its done 7 times (from w0=7), we get 79x(2^7).
- Again, stores the value at sp+28. Loads it back into w1.
- Signed division divides the numbers and then removes any decimal. So, the sp+28 value gets divided by 3 at sp+24. This is restored in sp+28, and re loaded into w1.
- Takes sp+12 value and subtracts it from w1, storing into w0.
- Stored at sp+28 and re loaded into w0.
```

- Doing all the mathematical operations, we get the correct specified number to be 3370.

```
72*2*2*2*2*2*2*2=10112
10112//3=3370
```

- Converting to hexadecimal gives D2A. 
- Correctly converting it into lowercase 32 bit hex gives 00000d2a.

## Flag:

```
picoCTF{00000d2a}
```

## Concepts learnt:
- Basic Assembly syntax.
- Assembly keywords and functions.
- Storage and retrieval of variables in assembly.

## Notes:
- Alternate tangent 1: Installed NASM and tried to convert the source file into an object file for execution. Failed, because NASM is only for x86 and the source file being for a mobile ARM architecture. 

## Resources:
- .S file explanation (https://stackoverflow.com/questions/10285410/what-are-s-files)
- Some info about keywords (https://mariokartwii.com/armv8/)
- Sections (https://www.tutorialspoint.com/assembly_programming/assembly_memory_segments.htm)
- About w0, w1, etc (https://developer.arm.com/documentation/101550/0000/Programmers--model/Armv8-R-AArch64-architecture-concepts/Armv8-R-AArch64-registers)
- About sp (https://stackoverflow.com/questions/8236959/what-are-sp-stack-and-lr-in-arm)
- More context for the stacks management (https://www.reddit.com/r/asm/comments/14cbwnx/why_subtract_from_the_stack/)
- str (https://azeria-labs.com/memory-instructions-load-and-store-part-4/)
- ldr (https://stackoverflow.com/questions/73495618/how-to-use-str-and-ldr-in-assembly)
- lsl, sdiv and mov (https://www.cs.princeton.edu/courses/archive/fall19/cos217/reading/ArmInstructionSetOverview.pdf)
- Decimal to hexadecimal convert (https://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html)
