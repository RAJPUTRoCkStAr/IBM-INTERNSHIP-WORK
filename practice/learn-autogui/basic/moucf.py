import pyautogui as pag 
# print(f"it will say size of window {pag.size()}")
# print(f"it will say position of the cursor{pag.position()}")
# pag.moveTo(100, 200,2)  # moves mouse to X of 100, Y of 200.
# pag.move(0, 50,2)       # move the mouse down 50 pixels. by default it will be there in 0.1 sec so it will be good practice to give some time
# pag.dragTo(100, 200,2,button='left') # drag mouse to X of 100, Y of 200 while holding down left mouse button
# pag.drag(30, 0, 2, button='right')   # drag the mouse left 30 pixels over 2 seconds while holding down the right mouse button
# pag.moveTo(100, 100, 2, pag.easeInQuad)     # start slow, end fast
# pag.moveTo(100, 100, 2, pag.easeOutQuad)    # start fast, end slow
# pag.moveTo(100, 100, 2, pag.easeInOutQuad)  # start and end fast, slow in middle
# pag.moveTo(100, 100, 2, pag.easeInBounce)   # bounce at the end
# pag.moveTo(100, 100, 2, pag.easeInElastic)  # rubber band at the end
# pag.click() #it will click on the mouse
# pag.click(x=100, y=200) #it will go to x and y position and than click on it 
# pag.click(button='right') #it will right click on the mouse 
# pag.click(clicks=2)  # double-click the left mouse button
# pag.click(clicks=2, interval=0.25)  # double-click the left mouse button, but with a quarter second pause in between clicks
# pag.click(button='right', clicks=3, interval=0.25)  # triple-click the right mouse button with a quarter second pause in between clicks
# pag.mouseUp()  # does the same thing as a left-button mouse click
# press the right button down
# pag.mouseUp(button='right', x=100, y=200)  # move the mouse to 100, 200, then release the right button up.
# pag.scroll(10)   # scroll up 10 "clicks"
# pag.scroll(-10)  # scroll down 10 "clicks"
pag.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"