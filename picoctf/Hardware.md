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
