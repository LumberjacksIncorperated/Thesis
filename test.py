import Image
import numpy

def image2pixelarray(filepath):
        """
        Parameters
        ----------
        filepath : str
            Path to an image file

        Returns
        -------
        list
            A list of lists which make it simple to access the greyscale value by
            im[y][x]
        """
    im = Image.open(filepath).convert('L')
    (width, height) = im.size
    greyscale_map = list(im.getdata())
    greyscale_map = numpy.array(greyscale_map)
    greyscale_map = greyscale_map.reshape((height, width))
    return greyscale_map

image = image2pixelarray("document.jpeg")
print image
 
