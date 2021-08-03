<h1 align="center">OSX Thief Catcher</h1>

<p align="center">
  <a href="https://github.com/emirthab/osx-thief-catcher">
    <img src="https://github.com/emirthab/osx-thief-catcher/blob/main/media/logo.png?raw=true" alt="OSX Thief Catcher" width="300">
  </a>
</p>

## Introduction:

:large_blue_circle: An application that detects the vibration that occurs when the wrong password is entered on your Mac Os device and takes photos from your camera when this vibration occurs. Made using python opencv.

## Usage :

* ### Install requirements:
```
pip install -r requirements.txt
```

* ### Run Application:
```
python init.py
```

## How It Works:

* The application listens for the computer to wake up. When the computer wakes up, it starts performing image operations.  
* First, as soon as you wake up, it takes a picture of the password entry screen and memorizes this picture.  
* Then it takes a picture of the screen continuously in a while loop and takes the difference with the one in memory.  
* The difference between the memory photo and the current photo is that the same places are painted black and different places are painted white.  
* So when the password is entered incorrectly, the difference picture will be as follows:  

<p align="left">
    <img src="https://github.com/emirthab/osx-thief-catcher/blob/main/media/start.png?raw=true" alt="start" height="100">
    <img src="https://github.com/emirthab/osx-thief-catcher/blob/main/media/current.png?raw=true" alt="current" height="100">
    <img src="https://github.com/emirthab/osx-thief-catcher/blob/main/media/diff.png?raw=true" alt="diff" height="100">
</p>

* Then our program outputs the histogram of this difference image.  
* Calculates the standard deviation from this histogram. The "stgScreen" value is for the standard deviation value required to open the screen. The "stgWrong" value is for the standard deviation value when the wrong password is entered.  
* You can change these values yourself.  
* Edit the code on line 60 for testing.  

<h3 align="center">Demo Video</h3>

https://user-images.githubusercontent.com/52050284/128033103-0005f162-eeb3-4d1f-b8dd-14574478a357.mp4


