Scanera Image Merging
=====================

Janky RGB image merging for a janky scanner based camera.

Usage: python combine.py [directory-and-file-prefix-for-channels]

Say you have images called `jank_image_blue.jpg`, `jank_red.png` and `jank_green.jpg` in
a directory called `my_lovely_images` use

e.g. python combine.py my_lovely_images/jank

User controls
-------------

| key | Action                               |
|-----|--------------------------------------|
| w   | increase chroma                      |
| q   | decrease chroma                      |
| r   | shift colour balance towards red     | 
| g   | shift colour balance towards green   | 
| b   | shift colour balance towards blue    |
| e   | shift colour balance away from red   | 
| f   | shift colour balance away from green | 
| v   | shift colour balance away from blue  | 

Note: keys for moving the colour balance away are the ones to the left of the others. 