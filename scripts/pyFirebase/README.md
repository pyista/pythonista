# pyFirebase

A python script to send (arduino) serial monitor data to frebase database.

## Dependencies

1. firebase
2. serial
3. json

## [Script Snippet](./main.py)

```py
firebase = firebase.FirebaseApplication('https://___YOUR_PROJECT_NAME____.firebaseio.com/')

while 1:
    myData = (arduinoData.readline().strip())
    myData = (myData.decode('utf-8'))
    result = firebase.put('MainNode/Leaf','temp',myData)
```

## Description

This script extracts data from the serial port using the function `serial.Serial('port', baud rate).readline()`. And after that we chain on a strip() function.

Then the data extracted is decoded in `utf-8` encoding. After this we simply push the script to our database using firebase.put() method.

## Usage

`python main.py`

## Author

- [Madhav Bahl](https://github.com/MadhavBahlMD)