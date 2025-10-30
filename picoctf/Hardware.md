# 1. I like Logic
i like logic and i like files, apparently, they have something in common, what should my next step be.
- Included [file](../assets/challenge.sal)

## Solution:
- The folder includes a .sal file. Searching for it reveals that it is a Salae logic analyser file. This is helped by the fact that the description mentions logic files.
- Opened the file. I saw 1s and 0s in the third channel.
- First, I exported the raw data. I could not find anything useful in that.
- So, I searched up an ascii analyser for it.
- The ascii analyser gave a csv file with sentences. I exported the file and used resource 2 to convert the csv to 1 sentence.
- I opened the sentence in Word, and used find and replace to replace 0-9, fullstop and commas with blank, replaces COMMA with , and both \r and \n with spaces.
- This gave a legible paragraph with a flag format in it.  

Extracted and cleaned sentence in a [TXT file](../assets/logic.txt)

## Flag:

```
FCSC{b1dee4eeadf6c4e60aeb142b0b486344e64b12b40d1046de95c89ba5e23a9925}
```

## Concepts learnt:
- Logic files and types.
- Data storage using binary logic pulses.

## Notes:
- Alternate tangent 1: Export raw data and binary.
- Critical error: Accidentally removed numbers before copying flags.

## Resources:
- Salae analyser guide (https://support.saleae.com/user-guide/using-logic/saving-loading-and-exporting-data)
- CSV to delimited (https://delim.co/#)

# 2. IQ Test
let your input x = 30478191278.

wrap your answer with nite{ } for the flag.

As an example, entering x = 34359738368 gives (y0, ..., y11), so the flag would be nite{010000000011}.

## Solution:
- Download the files and try solve the logic gates.
- Since they take only 0's and 1's and I needed 36 x values, convert to 36 bit. Add an extra 0 at the start for 36 vales of x and we get 011100011000101001000100101010101110.
- Now, I solve the gates.
- The binary sequence gotten is 101101100111. 
- Here, I made an error. Furthur analysis showed small dots before many gates. These dots invert the input and give a different answer.

[Incorrect solution](../assets/iqtestsolved.png.jpg) 

## Flag:

```
nite{100010011000}
```

## Concepts learnt:
- Logic gates

## Notes:
- Alternate tangent 1: Tried binwalk.
- Critical error: Ignored input inverters.

## Resources:
- Logic Gates (https://www.geeksforgeeks.org/digital-logic/logic-gates/)

# 3. Bare Metal Alchemist
my friend recommended me this anime but i think i've heard a wrong name.
- Included [file](../assets/firmware.elf)

## Solution:
- The attached file is a .elf file, an executable and linkable linux file. Like in GDB baby step 1, I tried executing it first.
- This throws an error.
```bash
./firmware.elf
./firmware.elf: cannot execute binary file: Exec format error
```
- Searching the error, I understood that the file may have requirements like OS or architecture.
- Next, I tried to objdump it.
```sh
objdump -d firmware.elf
firmware.elf:     file format elf32-little
objdump: can't disassemble for architecture UNKNOWN!
```
- Then, I searched up an architecture/OS checker.
- I followed the instructions and found the correct architecture.
```sh
crownless@LAPTOP-6K42D1CN:~$ readelf -h firmware.elf | grep 'Class\|File\|Ma
chine'
  Class:                             ELF32
  Machine:                           Atmel AVR 8-bit microcontroller
```
- Searching, I found that i needed to install some software, which I did.
- I used a different [objdump](../assets/objdump3.txt) on the file.
```sh
avr-objdump -d firmware.elf
```
- This returned a lot of info. Looking at the main for clues.
- Also downloaded Ghidra to decomplie better understand the assembly code as I am not familiar with it.
- Installed Ghidra and JDK for running it.
- Using Ghidra, I found the C code for the file. A lot of things were still in AVR code, like register names.
- The C [code](../assets/decompiled.cs) made no sense so I switched back to the avr elf.
- I looked up more methods and got simavr.
- Installing simavr.
- Using architecture atmega328p as shown in the objdump.

## Flag:

```
FCCTF{Th1s_1s_som3_s1mpl3_4rdu1no_f1rmw4re}
```

## Concepts learnt:
- Microcontroller Assembly and ELF.
- Transforming AVR to C.
- Uses of AVR libraries.

## Notes:
- Had many incorrect tangents; already documented in solution.
- Did not fully understand everything about this.

## Resources:
- Error message information (https://stackoverflow.com/questions/66970902/getting-the-error-bash-program-cannot-execute-binary-file-exec-format-erro)
- Architecture checker (https://stackoverflow.com/questions/3740379/how-can-i-get-the-architecture-of-a-a-file)
- Atmel software (https://www.microchip.com/en-us/development-tool/atmel-avr-toolchain-for-linux)
- C to AVR (https://www.codeproject.com/articles/AVR-Assembler#comments-section)
- XOR (https://medium.com/%40horrow49/decrypting-firmware-a-practical-guide-to-unlocking-xor-encrypted-binaries-493320a91c9c)
- simavr (https://www.instructables.com/Debugging-AVR-code-in-Linux-with-simavr/)
- install (https://github.com/buserror/simavr)
- simavr help (https://www.avrfreaks.net/s/topic/a5C3l000000UUn9EAG/t132157)
