![Logo](https://zupimages.net/up/24/32/ci15.png)

# AuraEngine

✧ Python images encoder/decoder for NumWorks ✧

❱ Aura allows encoding images to Python files & decoding them on the NumWorks.          
Everything uses Python, making it a perfect solution for building programs on top of it.
## Features

- Encode images of any size or color range.
- Decode images up to 64x64 pixels.
- Decode multiple images from Python files.
  
↻ More Features are planned for future updates.
## Usage/Examples

#### Encode Images
First, install the image encoding tool, either by :
- Downloading the '.exe' file from the releases section.
- Cloning the repo and using the 'aura_encoder.py' file.


Then launch the tool & pick the image you want to encode (64x64 max resolution).        
Press the 'Open' button, a new file called 'colors.txt' should be created.

Finally, copy the content of this file and upload it as a Python script on your calculator.

#### Decode Images
⚠️ WARNING : You need Omega or Upsilon for this tool to work.

First, clone the GitHub repository if you haven't already.              
Then locate the 'aura_decode.py' file & upload it as a Python script on your calculator.

Finaly, after importing the module.                                         
Use the 'picture()' function to decode an image from the given python file.

#### Example
```python
>> picture("example_image.py", pos_x, pos_y, scale)
```
## Credits

This tool uses the modules 'pillow', 'kandinsky', and 'tkinter'.

['pillow' by Aclark](https://pypi.org/project/pillow/)

['kandinsky' by Susideur_YT](https://pypi.org/project/kandinsky/)
