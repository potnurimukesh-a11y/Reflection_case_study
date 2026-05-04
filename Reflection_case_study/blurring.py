
from simpleimage import SimpleImage

DEFAULT_FILE = 'mt-rainier.jpeg'

def blur_image(image, passes):
    if passes == 0:
        return image

    width = image.width
    height = image.height

    blurred = SimpleImage.blank(width, height)

    for h in range(height):
        for w in range(width):

            total_r = 0
            total_g = 0
            total_b = 0
            count = 0

            for dh in [1]:
                for dw in [-1, 0, 1]:

                    nh = h + dh
                    nw = w + dw

                    if 0 <= nh < height and 0 <= nw < width:
                        r, g, b = image.get_pixel(nw, nh)

                        total_r += r
                        total_g += g
                        total_b += b
                        count += 1

            avg_r = total_r // count
            avg_g = total_g // count
            avg_b = total_b // count

            blurred.set_rgb(w, h, avg_r, avg_g, avg_b)

    return blur_image(blurred, passes - 1)


def main():
    # Get file and load image
    filename = get_file()

    # Show the original image
    original = SimpleImage(filename)
    original.show()

    # Blur the image
    blurred = blur_image(original, 50)
    blurred.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()