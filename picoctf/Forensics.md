# 1. m00nwalk
Decode this [message](../assets/message.wav) from the moon.

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

# 2. tunn3l v1s10n
We found [this](../assets/tunn3l_v1s10n) file. Recover the flag.
Hint 1: Weird that it won't display right...

## Solution:
- First, I downloaded the file. It again did not have a file extension.
- I used resource 1 to check the opening bits of the file. By further search, this file was confirmed to be bm bitmap format.
- Since bitmaps are representations of pictures, I searched for a bitmap to image converter to convert the file into a .jpg image.
- The converter worked, but only had a placeholder garbage value called notaflag{sorry}.

![Garbage flag](../assets/img1.jpg)

- So, I needed to manipulate the original file. Since there are no other files and the hint seems to be related to the conversion thats already done, the flag must be in the image.
- I zoomed into the image and tried finding hidden text, but found nothing.
- Then, searching online for methods to hide information in images suggested several methods like exiftools, binwalk, colour grading and saturation chnages and header edits.
- I tried many methods but none worked. Binwalk seemed to glitch when I attempted to use it. So, I turned to header editing.
- When I imported the image into a hexeditor, it showed that the format was 12.4% mp3. So, the converter had somehow corrupted the file somewhat.
- So, I opened the original bitmap in the hex editor.
- Changing the width kept corrupting the file. So, I switched to height.
- I found the height pixels and set them from 300 pixels to 400, 450, 500 and so on.
- At 850 pixels the file got corruptedso I tried from 810 onward.
- I saw the flag at 830 pixels.

Image at 820 pixel height:
![No flag](../assets/img6.bmp)

Flag at 830 pixel height:
![Flag](../assets/img7.bmp)

## Flag:

```
picoCTF{qu1t3_a_v13w_2020}
```

## Concepts learnt:
- Hex values and headers.
- File conversion corruption.
- Soft crop images using header manipulation to hide information.
- Leading bits identification.
- Hex editing and information location.

## Notes:
- Alternate tangent 1: Zooming and using OCR tools.
- Alternate tangent 2: Import into photoshop, binwalk to look for any hidden layers.
- Alternate tangent 3: Uncrop using photoshop.
- Alternate tangent 4: Change brightness, contrast and saturation to reveal text.
- Alternate tangent 5: Try a QR scanner for hidden text.

## Resources:
- File leading bits checker (https://hexed.it/)
- Leading bits identification index (https://en.wikipedia.org/wiki/List_of_file_signatures)
- Information aboyt bitmaps (https://en.wikipedia.org/wiki/Bitmap)
- bm to jpg converter (https://online.reaconverter.com/)
- Information hiding using hex (https://cyberhacktics.com/hiding-information-by-changing-an-images-height/#:~:text=Steps,net%20via%20your%20web%20browser).)
- Bitmap header information (https://en.wikipedia.org/wiki/BMP_file_format#:~:text=The%20first%202%20bytes%20of,least%2Dsignificant%20byte%20first).&text=The%20header%20field%20used%20to,same%20as%20BM%20in%20ASCII.)

