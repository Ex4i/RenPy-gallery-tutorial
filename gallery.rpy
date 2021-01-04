init python:

    ### CONFIG ###
    cg_format = ".jpg" # file extension of the CGs, used in creating automatic thumbnails
    cg_path = "images/cg/" # path to CGs
    max_x = 3 # number of columns of thumbnails in the gallery grid
    max_y = 3 # number of rows of thumbnails in the gallery grid
    thumbnail_crop_x = 285 # this will be the width of the thumbnails, height will be calculated automatically for 16:9 aspect ratio thumbnails
    ### END OF CONFIG ###

    max_page = max_x * max_y
    thumbnail_crop_y = int(thumbnail_crop_x * 0.5625) # to change the aspect ratio from 16:9 to a different one, modify the value in formula
    gallery_page = 0
    gallery_items = []
    g = Gallery()
    g.transition = dissolve
    g.locked_button = im.Scale("gui/locked.png",thumbnail_crop_x,thumbnail_crop_y)

    class GalleryItem:
        def __init__(self, name, images, thumb=None, locked="gui/locked.png"):
            self.name = name
            self.images = images # provide images in a list, you can put more than one to have more images displayed consecutively after another under one button
            if thumb is None:
                self.thumb = im.Scale(cg_path+images[0]+cg_format,thumbnail_crop_x,thumbnail_crop_y) # if no thumbnail is provided as the 3rd argument, it will be built automatically from the 1st image in 16:9 aspect ratio
            else:
                self.thumb = im.Scale(thumb,thumbnail_crop_x,thumbnail_crop_y) # alternatively the path to the custom thumbnail can be provided as the 3rd argument during object creation
            self.locked = locked

        def num_images(self):
            return len(self.images)

screen gallery():

    python:
        if len(gallery_items) == 0:

            ### CGs ###
            gallery_items.append(GalleryItem("trees", ["cg trees"]))
            gallery_items.append(GalleryItem("gres", ["cg gres", "cg gres side"], "images/cg/cg gres thumbnail.jpg"))

            for item in gallery_items:
                g.button(item.name)
                for img in item.images:
                    g.unlock_image(img)

        start = gallery_page * max_page
        end = min(start + max_page - 1, len(gallery_items) - 1)

    tag menu
    style_prefix "game_menu"
    add im.Blur(gui.main_menu_background, 1.5)
    add "gui/overlay/main_menu.png"
    add "gui/overlay/gallery_background_overlay.png"

    hbox:
        vbox:
            style_prefix "navigation"
            yalign 0.9
            xsize 290
            xpos gui.navigation_xpos
            spacing gui.navigation_spacing

            textbutton "Previous":
                if gallery_page > 0:
                    action SetVariable("gallery_page", gallery_page - 1)
            textbutton "Next":
                if (gallery_page + 1) * max_page < len(gallery_items):
                    action SetVariable("gallery_page", gallery_page + 1)
            textbutton "Return" action Return()

        grid max_x max_y:
            xfill True
            yfill True
            for i in range(start, end + 1):
                $ item = gallery_items[i]
                add g.make_button(item.name, item.thumb, idle_border=im.Crop("gui/overlay/gallery_idle_overlay.png",(0,0,thumbnail_crop_x,thumbnail_crop_y)), xalign=0.5, yalign=0.5)
            for i in range(end - start + 1, max_page):
                null