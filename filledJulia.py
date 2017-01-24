colourPallete = ["#ff0000","#ff3000","#ff4400","#ff5400","#ff6100","#ff6c00","#ff7700","#ff8000","#ff8900","#ff9100","#ff9900","#ffa600","#ffb200","#ffbd00","#ffc800","#ffd200","#ffdc00","#ffe500","#ffee00","#fff700","#ffff00","#f2ff00","#e4ff00","#d5ff00",
        "#c6ff00","#b4ff00","#a1ff00","#8cff00","#72ff00","#51ff00","#00ff00","#00f241","#00e55b","#00d770","#00c881","#00b890","#00a69e","#0092ab","#007bb6","#005ec2","#0033cc","#2030c4","#2e2ebc","#382bb4","#4128ab","#4824a1","#4f2097","#551c8d","#5b1781",
        "#611074","#660066","#7e0061","#92005b","#a40055","#b4004f","#c20048","#d00041","#dd0038","#e9002e","#f40020"]


from tkinter import Tk, Canvas, PhotoImage, mainloop

# basic variable assignment
WIDTH, HEIGHT = 600, 600
cutoff = 300
zoom = 1 # the height of the image in the plane
zoom = [zoom*(WIDTH/HEIGHT),zoom]
focus = [-0.4,0.6]
centre = [0,0] # coordinates of the images centre in the complex plane

# creates the canvas and image object for which the pixels can be edited
app = Tk()
c = Canvas(app, width=WIDTH, height=HEIGHT, bg="#fff")
c.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
c.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

# creates the empty array for the mandelbrot/julia set
imageArray = []
for y in range(HEIGHT):
    imageArray.append([])
    for x in range(WIDTH):
        imageArray[y].append([])

# working based on the z -> z^2 + c equation
def createFilledJulia(array,focus,centre,zoom,cutoff):
    incrementX = 2*zoom[0] / WIDTH
    incrementY = 2*zoom[1] / HEIGHT
    topLeft = [centre[0] - zoom[0], centre[1] - zoom[1]]
    for x in range(WIDTH):
        for y in range(HEIGHT):
            c = focus
            z = [topLeft[0] + x*incrementX,topLeft[1] + y*incrementY]
            n = 0
            while n < cutoff and (z[0]**2 + z[1]**2) < 4:
                a = z[0]
                b = z[1]
                z = [a*a - b*b, 2*a*b]
                z = [z[0] + c[0], z[1] + c[1]]
                n += 1
            array[y][x] = n
    return array

'''
def createColours(array):
    newArr = array
    for i,y in enumerate(array):
        for j,x in enumerate(array[i]):
            rgb = hex((255 - x)*(16**4) + (23)*(16**2) + x)
            rgb = rgb[2:]
            rgb = "#" + rgb
            newArr[i][j] = rgb
    return newArr
'''
def createColours(array):
    newArr = array
    for i,y in enumerate(array):
        for j,x in enumerate(array[i]):
            colour = "#000000"
            if x < cutoff:
                colour = colourPallete[x % len(colourPallete)]
            newArr[i][j] = colour
    return newArr

def drawMandelbrot(imageArray,image):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            image.put((imageArray[y][x]),(x,y))

imageArray = createFilledJulia(imageArray,focus,centre,zoom,cutoff)
imageArray = createColours(imageArray)
drawMandelbrot(imageArray,img)

#img.write("img/julia/" + str(focus[0]) + " + " + str(focus[1]) + "i zoom=" + str(zoom) + ".gif",format="gif")

#print(createMandelbrot(imageArray,centre,zoom,cutoff))

mainloop()
