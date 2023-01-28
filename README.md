Convert your gifs into a series of pbm images to play gifs on I2C Oled Displays. Use the provided _animate.py_ script to play animations.<br /> ![Demo](https://i.imgur.com/DjaMIxR.gif)

## Installation
This converter is built for Windows, you can use the **executable** file in _/exe_ to directly run the application or use the following commands to run the application using python. You can copy the generated pbm images and play them on Oled Display.

##### NOTE: Make sure you have _pipenv_ installed and at least python 3.9 in your system.
```
cd gif_to_pbm
pipenv shell
python app.py
```
## Tools
In this section, you will be able to set the total number of images that will be played as the frames on the display. According to my setup, a Raspberry Pi 4 4GB was able to run animations at _10fps_. By default, total animation frames are set to 25 frames. <br />
Resisizing depends on the Oled display check if it is 128x64 or 128x32 before resizing. The crop tool can be used to pad the animation in whichever position is desired. Note some displays are multicolored and need to be padded if you want uniform colour in the animation.

## Adjust
Use the slider to adjust the tolerance value, also make use of arrow keys to move through the animation, and check for clippings. White and light gray images are displayed on the screen make use of invert option if necessary.<br />
| *Good*  | *Bad* |
| ----- | ----- | 
|![Good](https://i.imgur.com/e01UFFd.jpeg) | ![Bad](https://i.imgur.com/nkZUSUF.jpeg) | <br />

## Playing the Gif
Make sure you have the necessary libraries installed, [reference](https://www.youtube.com/watch?v=lRTQ0NsXMuw, "Youtube").<br />
Run the animate.py script using 
```
cd gif_to_pbm
pipenv shell
python animate.py
```
Place your own converted gif into the folder and change the name to your animation folder on _line 31_.
