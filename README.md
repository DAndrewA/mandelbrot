# mandelbrot
A fractal generator based on the Mandelbrot set

## usage
### mandelbrot.py
This generates the Mandelbrot set using the itterative function z -> z^2 + c, where z always starts at 0.

WIDTH: the width of the created image

HEIGHT: the height of the created image

cutoff: the number of itterations the program will go through before assuming a value is part of the mandelbrot set

zoom: the height of the image from it's centre in terms of the complex plane

centre: where the centre of the image is focused on the complex plain (in the form [a,b] for a + bi)

Once these variables have been manually input, the program can be ran to produce an image - it may take a while for certain parts of the mandelbrot set.

### filledJulia.py
This generates a Julia set based on the input value of c. This again uses the complex function z -> z^2 + c with z being each point on the complex plane.

WIDTH: see above

HEIGHT: see above

cutoff: see above

zoom: see above

focus: the value of c assumed in the function (in the form [a,b] where c = a + bi)

centre: where the centre of the image is focused in terms of the complex plane
