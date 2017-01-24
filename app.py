from tkinter import Tk, Canvas, PhotoImage, mainloop

# could do with refining
PALLETE = ["#ff0000","#ff3000","#ff4400","#ff5400","#ff6100","#ff6c00","#ff7700","#ff8000","#ff8900","#ff9100","#ff9900","#ffa600","#ffb200","#ffbd00","#ffc800","#ffd200","#ffdc00","#ffe500","#ffee00","#fff700","#ffff00","#f2ff00","#e4ff00","#d5ff00",
        "#c6ff00","#b4ff00","#a1ff00","#8cff00","#72ff00","#51ff00","#00ff00","#00f241","#00e55b","#00d770","#00c881","#00b890","#00a69e","#0092ab","#007bb6","#005ec2","#0033cc","#2030c4","#2e2ebc","#382bb4","#4128ab","#4824a1","#4f2097","#551c8d","#5b1781",
        "#611074","#660066","#7e0061","#92005b","#a40055","#b4004f","#c20048","#d00041","#dd0038","#e9002e","#f40020"]

class Polynomial:
    # order : highest order exponent of the natural numbers
    # coefficients : ordered array for the coefficients of each exponent (from ^1 to ^order)
    # Note, each coefficient is a real number, and this can only perform natural exponents
    def __init__(self,order,coefficients):
        self.order = order
        self.coefficients = coefficients

    # x : the number the equation is being solved for
    # c : the constant in the equation
    def solve(self,z,c):
        values = [c]
        powerValues = [z]

        expo = 1
        while expo < self.order:
            a = powerValues[expo-1]
            a = [(a[0] * z[0]) - (a[1] * z[1]),(a[0] * z[1]) + (a[1] * z[0])]
            powerValues.append(a)
            expo += 1

        for i in range(self.order):
            a = powerValues[i]
            coef = self.coefficients[i]
            a = [a[0] * coef, a[1] * coef]
            values.append(a)

        finalValue = [0,0]
        #print(values)
        for v in values:
            finalValue[0] += v[0]
            finalValue[1] += v[1]

        return finalValue

class Viewer:
    def createSet(self):
        self.array = self.createEmpty()

        if self.mode == 0:
            array = createMandelbrot(self)
        elif self.mode == 1:
            array = createJulia(self)
        elif self.mode == 2:
            array = createMandelbrotFromPolynomial(self)

        self.drawImage()

    def redraw(self,event):
        incrementX = 2*self.span[0] / self.WIDTH
        incrementY = 2*self.span[1] / self.HEIGHT
        topLeft = [self.centre[0] - self.span[0], self.centre[1] - self.span[1]]
        positionClicked = [topLeft[0] + ((event.x//1)*incrementX), topLeft[1] + ((event.y//1)*incrementY)]

        self.centre = positionClicked
        self.span[0] = self.span[0] / self.zoomFactor
        self.span[1] = self.span[1] / self.zoomFactor
        self.cutoff += self.cutoffScalar

        '''
        #can comment out
        print("Centre at : " + str(self.centre[0]) + " " + str(self.centre[1]) + "i")
        print("Span is : " + str(self.span[1])
        print("Zoom at : x" + str(1/self.span[1]) + " zoom")
        '''

        self.createSet()

    # creates the window for each individual image
    def drawImage(self):
        for y in range(len(self.array)):
            for x in range(len(self.array[y])):
                colour = "#000000"
                if self.array[y][x] < self.cutoff:
                    colour = PALLETE[self.array[y][x] % len(PALLETE)]
                self.img.put(colour,(x,y))

        '''
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                image.put((self.array[y][x]),(x,y))
        '''

    # creates the empty array for each new set
    def createEmpty(self):
        arr = []
        for y in range(self.HEIGHT):
            arr.append([])
            for x in range(self.WIDTH):
                arr[y].append([])
        return arr

    # w : WIDTH of the window housing the image
    # h : HEIGHT of the window housing the image
    # cuttof : cuttoff value for the number of itterations
    # span : (REPLACES zoom) the span of half the image in height
    # centre : the location on the complex plane of the image's centre
    # mode : 0 for mandelbrot, 1 for julia (optional, defaults to mandelbrot)
    # focus : optional for the focus of the julia set
    # zoomFactor : the factor by which clikcing on the image zooms it in by
    # cutoffScalar : the numerical increase in the scalar for each zoom - it should be greater than 0 as a smaller area requires a higher definition in the set
    # polynomial : defaults to x^2 + c, the function that the program itterates over (TO BE ADDED)
    def __init__(self,w,h,cutoff,span,centre,mode=0,focus=[0,0],zoomFactor=10, cutoffScalar=50,polynomial = [0,1]):
        self.WIDTH = w
        self.HEIGHT = h
        self.cutoff = cutoff
        self.span = [span*(w/h),span]
        self.centre = centre
        self.mode = mode
        self.focus = focus
        self.zoomFactor = zoomFactor
        self.cutoffScalar = cutoffScalar
        self.array = []
        self.polynomial = Polynomial(len(polynomial),polynomial)

        self.app = Tk()
        self.c = Canvas(self.app,height=self.HEIGHT,width=self.WIDTH)
        self.c.bind("<Button-1>",self.redraw)
        self.c.pack()

        self.img = PhotoImage(width=self.WIDTH, height=self.HEIGHT)
        self.c.create_image((self.WIDTH/2, self.HEIGHT/2), image=self.img, state="normal")

        self.createSet()


# working based on the z -> z^2 + c equation
def createMandelbrot(o):
    incrementX = 2*o.span[0] / o.WIDTH
    incrementY = 2*o.span[1] / o.HEIGHT
    topLeft = [o.centre[0] - o.span[0], o.centre[1] - o.span[1]]
    for x in range(o.WIDTH):
        for y in range(o.HEIGHT):
            c = [topLeft[0] + x*incrementX,topLeft[1] + y*incrementY]
            z = [0,0]
            n = 0
            while n < o.cutoff and (z[0]**2 + z[1]**2) < 4:
                a = z[0]
                b = z[1]
                z = [a*a - b*b, 2*a*b]
                z = [z[0] + c[0], z[1] + c[1]]
                n += 1
            o.array[y][x] = n
    return o.array

# working based on the z -> z^2 + c equation
def createJulia(o):
    incrementX = 2*o.span[0] / o.WIDTH
    incrementY = 2*o.span[1] / o.HEIGHT
    topLeft = [o.centre[0] - o.span[0], o.centre[1] - o.span[1]]
    for x in range(o.WIDTH):
        for y in range(o.HEIGHT):
            c = o.focus
            z = [topLeft[0] + x*incrementX,topLeft[1] + y*incrementY]
            n = 0
            while n < o.cutoff and (z[0]**2 + z[1]**2) < 4:
                a = z[0]
                b = z[1]
                z = [a*a - b*b, 2*a*b]
                z = [z[0] + c[0], z[1] + c[1]]
                n += 1
            o.array[y][x] = n
    return o.array

# creates a set based on the mandelbrot, but using different polynomials
def createMandelbrotFromPolynomial(o):
    incrementX = 2*o.span[0] / o.WIDTH
    incrementY = 2*o.span[1] / o.HEIGHT
    topLeft = [o.centre[0] - o.span[0], o.centre[1] - o.span[1]]
    for x in range(o.WIDTH):
        for y in range(o.HEIGHT):
            c = [topLeft[0] + x*incrementX,topLeft[1] + y*incrementY]
            z = [0,0]
            n = 0
            while n < o.cutoff and (z[0]**2 + z[1]**2) < 4:
                z = o.polynomial.solve(z,c)
                n += 1
            o.array[y][x] = n
    return o.array

#m = Viewer(600,600,200,2,[0,0])
#j = Viewer(600,600,200,2,[0,0], mode=1,focus=[-0.835,-0.2321]) # Julia set
#p1 = Viewer(300,300,200,2,[0,0],mode=2,polynomial=[-1,0,2]) # should produce mandelbrot set
p2 = Viewer(300,300,150,2,[0,0],mode=2,polynomial=[1,1,1]) # based on polynomial x^3 -2x^2 + x + c

mainloop()
