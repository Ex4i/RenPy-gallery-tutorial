# RenPy-gallery-example

An example of a working RenPy gallery with automatic thumbnails and layout built for default UI.

The code uses RenPy Gallery class which handles the unlocking itself. Images will be unlocked in the gallery as soon as the player encounters them in game. 

To use:
1) add gallery.rpy to your project
2) open the file and change the CGs to your own
3) add a button to navigation screen in screens.rpy (as in the example code): `textbutton "Gallery" action ShowMenu("gallery")`
4) copy images/gallery_overlay into your game directory
5) (optional) for the ease of use define your CGs as image objects as I did in images.rpy


Built using some code snippets (gallery-image class, layout buttons and paging) from another project: https://github.com/Emperrific/Renpy-Tutorials-CG-Gallery

Written for the visual novel Dawn Chorus (https://dawn-chorus.itch.io/dawn-chorus)
