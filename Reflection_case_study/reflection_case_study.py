"""
This program takes an image and generates a reflection.
The top half of the generated image is the same as the original.
The bottom half is the mirror reflection of the top half.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'mt-rainier.jpeg'

def make_reflected(filename):
    image = SimpleImage(filename)
    height = image.height
    width = image.width
    image.show()
    new_image = SimpleImage.blank(width, 2 * height)
    for height in range(0,image.height):
        for width in range(0, image.width):
            p = image._get_pix_(width, height)
            new_image.set_rgb(width, height, p[0], p[1], p[2])
    h = height
    i = 0
    for height in range(h,-1,-1):

        for width in range(0, image.width):
            p = image._get_pix_(width, height)
            new_image.set_rgb(width, h+i, p[0], p[1], p[2])
        i = i + 1
        
    print(h)
    
    # write your code here. Create a new_image with blank and do the necessary. the blank image 
    # should be of double the height of the original image. after doing this in the 19th line
    # have you observed that i am returning new_image. So by this time the new_image is already
    # FINAL REFLECTION IMAGE.

    return new_image


def main():
    # Get file and load image
    filename = get_file()

    # Show the original image
    original = SimpleImage(filename)
    original.show()

    # Show the reflected image
    reflected = make_reflected(filename)
    reflected.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()