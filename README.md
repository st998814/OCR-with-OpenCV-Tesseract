# OCR-with-OpenCV-Tesseract

### _A basic photo or image OCR project using OpenCV&Tesseract_ 

There are two major function for this project
* Recognize character from image which is visual object that create or altered by a computer.
* Process the photo that were taker by digital camera,parsing the information of it. 

All the config and function can be altered by different photo/image condition


#### Necessary pre-work

1.Grayscaling(OpenCV)

2.Thresholding(OpenCV)

#### Advanced processing for photograph

3.Dilating(OpenCV)

4.Eroding(OpenCV)

5.Opening (with PLTmodule)


####  Drawing box using Pytesseract
* On a character level

* On a Pixel level

* Based on a regex template



#### Running Tesseract 
```sh
custom_config = r' -l chi_tra --oem 3 --psm 6'
pytesseract.image_to_string(image, config=custom_config))
```
The configuration settting might have the great impact to the result

The full table of Tesseract config show as below
| Code | Description |
| ------ | ------ |
| --psm NUM  | Specify page segmentation mode. |
|0 | Orientation and script detection (OSD) only.|
|1 | Automatic page segmentation with OSD.|
|2| Automatic page segmentation with OSD.|
|3| Automatic page segmentation, but no OSD, or OCR.|
|4| Assume a single column of text of variable sizes.|
|5| Assume a single uniform block of vertically aligned text.|
|6| Assume a single uniform block of text.|
|7| Treat the image as a single text line.|
|8| Treat the image as a single word.|
|9| Treat the image as a single word in a circle.|
|10| Treat the image as a single character.|
|11| Sparse text. Find as much text as possible in no particular order.|
|12| Sparse text with OSD.|
|13| Raw line. |
| --oem NUM  |Specify OCR Engine mode. |
| 0 | Legacy engine only.|
| 1 | Neural nets LSTM engine only.|
| 2 | Legacy + LSTM engines.|
| 3 | Default, based on what is available.|





