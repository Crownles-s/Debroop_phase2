# 1. m00nwalk
Decode this message from the moon.

## Solution:
- Open the given link, which downloads an audio file.
- The given hints point us in the correct direction. The first research about the Apollo 11 moon landing's video transmission shows the technology at use: SSTV.
- Search google for any possible SSTV decrypters.
- Use a free online SSTV decrypter reveals an image file, the link in resources.
- This file has the flag.

![SSTV File](../assets/sstv_decoded_a66f1482-b89e-4472-8c15-7f54ab341a38.png?raw=true)

## Flag:

```
picoCTF{beep_boop_im_in_space}
```

## Concepts learnt:
- SSTV usage for image transfer.
- Various 'encoding' types for SSTV.

## Notes:
- Alternate tangent 1: Tried to analyse a histogram of the wav file.
- Alternate tangent 2: Tried to analyse waveforms of the wav file.

## Resources:
- Scottie Explanation (https://radio.clubs.etsit.upm.es/blog/2019-08-10-sstv-scottie1-encoder/)
- SSTV in the Moon Landing (https://www.scopeofwork.net/how-slow-scan-tv-shaped-the-moon/)
- SSTV decryption (https://hxp1.pythonanywhere.com/)
