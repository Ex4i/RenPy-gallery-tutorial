# RenPy-gallery-example

An example of a working RenPy gallery with automatic thumbnails and layout built for default UI.

The code uses RenPy Gallery class which handles the unlocking itself. Images will be unlocked in the gallery as soon as the player encounters them in game. 

To use add gallery.rpy to your project, open the file and change the CGs to your own, and add a button to navigation screen in screens.rpy (as in the example code):
`textbutton "Gallery" action ShowMenu("gallery")`

Built using some code snippets from another project: https://github.com/Emperrific/Renpy-Tutorials-CG-Gallery

Used in the visual novel Dawn Chorus (https://dawn-chorus.itch.io/dawn-chorus)
