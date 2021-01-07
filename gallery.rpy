init python:

    ### CONFIG ###
    # file extension of the CGs, used in creating automatic thumbnails
    cg_format = ".jpg" 
    # path to CGs
    cg_path = "images/cg/" 
    # number of columns of thumbnails in the gallery grid
    max_x = 3 
    # number of rows of thumbnails in the gallery grid
    max_y = 3 
    # this will be the width of the thumbnails, height will be calculated automatically for 16:9 aspect ratio thumbnails
    # recommended sizes:
    # 290 for 1280x720 resolution
    # 400 for 1920x1080 resolution
    thumbnail_x = 290
    ### END OF CONFIG ###

    max_page = max_x * max_y
    thumbnail_y = int(thumbnail_x * 0.5625) # to change the aspect ratio from 16:9 to 4:3, change the value in formula to 0.75
    gallery_resolution_scaling = config.screen_width / 1280.0
    gallery_navigation_width = int(290 * gallery_resolution_scaling)
    gallery_page = 0
    gallery_items = []
    g = Gallery()
    g.transition = dissolve
    g.locked_button = im.Scale("images/gallery_overlay/gallery_locked.png",thumbnail_x,thumbnail_y)

    # A class for gallery items (no need to change anything here)
    # when creating a GalleryItem object, provide images in a list, you can put more than one to have more images displayed consecutively after another under one button
    # if no thumbnail is provided as the 3rd argument, it will be built automatically from the 1st image in 16:9 aspect ratio
    # alternatively the path to the custom thumbnail can be provided as the 3rd argument during object creation
    class GalleryItem:
        def __init__(self, name, images, thumb=None):
            self.name = name
            self.images = images 
            if thumb is None:
                self.thumb = im.Scale(cg_path+images[0]+cg_format,thumbnail_x,thumbnail_y) 
            else:
                self.thumb = im.Scale(thumb,thumbnail_x,thumbnail_y)

        def num_images(self):
            return len(self.images)

image gallery_idle_overlay = im.Scale("images/gallery_overlay/gallery_idle_overlay.png",thumbnail_x,thumbnail_y)
image gallery_background_overlay: 
    "images/gallery_overlay/gallery_background_overlay.png"
    zoom gallery_resolution_scaling

screen gallery():

    python:
        if len(gallery_items) == 0:

            ### CGs ###
            # Provide button name, a list of images to display, and alternatively a path to a custom thumbnail
            gallery_items.append(GalleryItem("trees", ["cg trees"]))
            gallery_items.append(GalleryItem("gres", ["cg gres", "cg gres side"], "images/cg/cg gres thumbnail.jpg"))

            for item in gallery_items:
                g.button(item.name)
                for img in item.images:
                    g.unlock_image(img)

        start = gallery_page * max_page
        end = min(start + max_page - 1, len(gallery_items) - 1)


    ### Layout ###
    tag menu
    style_prefix "game_menu"
    add im.Blur(gui.main_menu_background, 1.5)
    add "gui/overlay/main_menu.png"
    add "gallery_background_overlay"

    hbox:
        vbox:
            style_prefix "navigation"
            yalign 0.9
            xsize gallery_navigation_width
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
                add g.make_button(item.name, item.thumb, idle_border="gallery_idle_overlay", xalign=0.5, yalign=0.5)
            for i in range(end - start + 1, max_page):
                null