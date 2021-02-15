# Landolt C Generator

# pulling from lines of code from :
# https://www.djmannion.net/psych_programming/vision/draw_shapes/draw_shapes.html

# create a bigger outter circle (black)
# create a smaller inner circle (white)
# create a white rectangle (c-gap)

# create a Landolt-C!
# repeat this process for 100 different pixel-width c-gaps, manipulating the visual acuity of the Landolt C's

import psychopy.visual
import psychopy.event

for x in range(99):

    # r modifies the size of the smaller circle. Change r to change the thickness of the C
    r = .4

    # p designates the number of pixels
    p = x + 1

    # set window parameters
    win = psychopy.visual.Window(
        size=[400, 400],
        units="pix",
        fullscr=False,
        color=[1, 1, 1]
    )

    # set outter circle parameters & color (black)
    circle = psychopy.visual.Circle(
        win=win,
        units="pix",
        radius=150,
        fillColor=[-1, -1, -1],
        lineColor=[-1, -1, -1],
        edges=128
    )

    # set inner circle parameters & color (white)
    circle2 = psychopy.visual.Circle(
        win=win,
        units="pix",
        radius=150*r,
        fillColor=[1, 1, 1],
        lineColor=[1, 1, 1],
        edges=128
    )

    # set c-gap rectangle parameters & color (white)
    rect = psychopy.visual.Rect(
        win=win,
        units="pix",
        width=150,
        height=p,
        fillColor=[1, 1, 1],
        lineColor=[1, 1, 1]
     )


    # draw the two circles
    circle.draw()
    circle2.draw()

    # offset the position of the rectangle to draw the C
    rect.pos = [100,0]
    rect.draw()

    win.flip()

    # grab the image to save it
    win._getFrame().save(str('imageFiles/landoltC_'+str(p)+'.png'))
    # uncomment if you want to look at every image
    # psychopy.event.waitKeys()

    # close the window 
    win.close() 

##########################

# draw a circle, without a gap (unique to Trent's experimental wishes)
win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False,
    color=[1, 1, 1]
)

circle = psychopy.visual.Circle(
    win=win,
    units="pix",
    radius=150,
    fillColor=[-1, -1, -1],
    lineColor=[-1, -1, -1],
    edges=128
)


circle2 = psychopy.visual.Circle(
    win=win,
    units="pix",
    radius=150*r,
    fillColor=[1, 1, 1],
    lineColor=[1, 1, 1],
    edges=128
)


circle.draw()
circle2.draw()


win.flip()

win._getFrame().save(str('imageFiles/circle.png'))

win.close() 