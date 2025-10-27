# 1. I like Logic
i like logic and i like files, apparently, they have something in common, what should my next step be.
- Included [file](../assets/challenge.sal)

## Solution:
- The folder includes a .sal file. Searching for it reveals that it is a Salae logic analyser file. This is helped by the fact that the description mentions logic files.
- Opened the file. I saw 1s and 0s in the third channel.
- First, I exported the raw data. I could not find anything useful in that.
- So, I searched up an ascii analyser for it.
- The ascii analyser gave a csv file with sentences. I exported the file and used resource 2 to convert the csv to 1 sentence.
- I opened the sentence in Word, and used find and replace to replace 0-9, fullstop and commas with blank, replaces COMMA with ,.
- This gave a legible paragraph with a flag format in it.  

Extracted and cleaned sentence in a [TXT file](../assets/logic.txt)

## Flag:

```
FCSC{bdeeeeadfceaebbbebbddecbaea}
```

## Concepts learnt:
- Logic files and types.
- Data storage using binary logic pulses.

## Notes:
- Alternate tangent 1: Export raw data and binary.

## Resources:
- Salae analyser guide (https://support.saleae.com/user-guide/using-logic/saving-loading-and-exporting-data)
- CSV to delimited (https://delim.co/#)
