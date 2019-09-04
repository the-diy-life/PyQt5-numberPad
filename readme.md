# PyQT-numberPad
> This project is a numberpad widget for PyQt5 that is used when you're working with a touchpad and want to input numbers.

> We had a project on a RaspberryPi and a touchscreen that required the user to input a number but we don't have a keyboard so we had to code this widget to be used as a general number pad for the whole project so whenever the user needs to input a number it is shown.
## Features
- Input numbers on a touch screen without a keyboard
- Can be used with any PyQt widget that has 'text' attribute
- A callback function can be passed to the widget to be called after pressing submit. You can use this to verify input and/or update a database.
- You can enter a constant text that the widget will append the entered number to. For example, if the constant text is `Number: ` and the submitted number is 9 the text will be `Number: 9`


## Usage
To use the widget as a popup window:
```
self.MainWindow.setEnabled(False)
self.exPopup = numberPopup(self.MainWindow,self.lineEdit, "Number:", self.callBackOnSubmit, "Argument 1", "Argument 2")
self.exPopup.setGeometry(130, 320,400, 300)
self.exPopup.show() 
```

- `self.MainWindow` is the window that the popup will pop from. It will be disabled at first and enabled again after pressing submit.
- `self.lineEdit` is the field that will be updated with the entered value.
- `Number:` is the constant text.
- `self.callBackOnSubmit` is the callback function that will be called after pressing submit.
- `Argument 1` and `Argument 2` are the arguments for the function `self.callBackOnSubmit`.

> Run the example.py script as a complete example. 

## Video
[Link](https://drive.google.com/file/d/1XXKdKTfD1dPrDbl_IqjJa5VhwPF_PyUS/view?usp=sharing)

## Prerequisites 
You need to have PyQt5 installed on your system. 

To install PyQt5:
```
pip install PyQt5 
```

