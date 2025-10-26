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

# 2. vault-door-3
This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java.](../assets/VaultDoor3.java)

## Solution:
- Open the given link, which downloads a .java, a JAVA source file. Opens without issues in vscode.
- Now, I tried to understand the code. The comments clealy mention a password. The code itself looks very similar to C.

```java
class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }
```
- From this, we can see the format of the password to be picoCTF{}, so the password is part of the flag.
- This snippet invokes the checkPassword below this. True returns "Access granted", false returns "Access denied"
- So, I turn to the second half of the code.

```java
public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f");
    }
```

- The start immediately mentions that the password length must be equal to 32. The snippet returns false if it's not 32.
- An int i is defined, to be used in for loop indexing. Followed by 4 for loops.
- The first for loop takes password characters indexed 0 to 7, and places them at index 0 to 7 of a new string.
- The second for loop works on index 8 to 15, placing the characters into index 15 to 8 respectively in order.
- The third for loop takes index 16 to 32 but in steps of 2. So it takes 16, 18, 20, up to 30. Places them at 30, 28 , 26, respectively up to 14.
- The fourth for loop takes index 31 to 17 in reverse order and steps of 2. It places them at the same index in the new string.
- These 4 loops cover all 0 - 31 index characters. Since out put is supposed to be `jU5t_a_sna_3lpm18g947_u_4_m9r54f` we can just reverse the jumbling.
- To reverse the jumbling, we can do it manually or write a code.

```java
char[] password = new char[32];
        for (; i<16; i++) {
             password.charAt(23-i) = buffer[i];
        }
        for (; i<32; i+=2) {
             password.charAt(46-i) = buffer[i];
        }
        for (i=0; i<8; i++) {
             password.charAt(i) = buffer[i];
        }
        for (i=31; i>=17; i-=2) {
             password.charAt(i) = buffer[i];
        }
```

## Flag:

```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f}
```

## Concepts learnt:
- For loops in java.
- If and else in java.

## Notes:
- No alternate tangents.

## Resources:
- None.

# 2. GDB baby step 1
Can you figure out what is in the eax register at the end of the main function? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Disassemble [this.](../assets/debugger0_a)

## Solution:
- Used hex editor to identify the file type after downloading. It is a linux executable and linkable file (ELF).
- Import it to WSL and tried running the ELF. There is no output at all.
```
cp /mnt/c/Users/DEBROOP/Downloads/debugger0_a ~/
chmod a+x debugger0_a
debugger0_a
```
- Then, I searched how to get the contents of the file to look for the main function as asked.
- Sources suggested using objdump or readelf. Using objdump -d because description asks to disassemble/
```
objdump -d debugger0_a
```
- This command gave a full [list](../assets/debugger0_a-objdump.txt) of the functions. Then, I found the main function.
```
0000000000001129 <main>:
    1129:       f3 0f 1e fa             endbr64
    112d:       55                      push   %rbp
    112e:       48 89 e5                mov    %rsp,%rbp
    1131:       89 7d fc                mov    %edi,-0x4(%rbp)
    1134:       48 89 75 f0             mov    %rsi,-0x10(%rbp)
    1138:       b8 42 63 08 00          mov    $0x86342,%eax
    113d:       5d                      pop    %rbp
    113e:       c3                      ret
    113f:       90                      nop
```
- Found a hexadecimal number followed by %eax. Converted it to decimal and used it as flag.

## Flag:

```
picoCTF{549698}
```

## Concepts learnt:
- ELF files and uses.
- How to run ELF files.
- How to disassemble ELF files.
- Uses of objdump.

## Notes:
- Alternate tangent 1: Tried to run the ELF file.

## Resources:
- ELF file content viewing (https://stackoverflow.com/questions/1685483/how-can-i-examine-contents-of-a-data-section-of-an-elf-file-on-linux)
- objdump manpage (https://man7.org/linux/man-pages/man1/objdump.1.html)
