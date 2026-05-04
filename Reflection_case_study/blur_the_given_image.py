from simpleimage import SimpleImage

DEFAULT_FILE = 'mt-rainier.jpeg'

def make_gaussian_blur(image):
    height = image.height
    width = image.width
    new_image = SimpleImage.blank(width, height)

    kernel = [
        [2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2],
        [3, 4, 5, 6, 7, 9,10,11,11,10, 9, 7, 6, 5, 4, 3],
        [4, 5, 6, 7, 9,11,13,14,14,13,11, 9, 7, 6, 5, 4],
        [5, 6, 7, 9,11,14,16,18,18,16,14,11, 9, 7, 6, 5],
        [6, 7, 9,11,14,17,20,22,22,20,17,14,11, 9, 7, 6],
        [7, 9,11,14,17,21,24,26,26,24,21,17,14,11, 9, 7],
        [8,10,13,16,20,24,28,30,30,28,24,20,16,13,10, 8],
        [9,11,14,18,22,26,30,34,34,30,26,22,18,14,11, 9],
        [9,11,14,18,22,26,30,34,34,30,26,22,18,14,11, 9],
        [8,10,13,16,20,24,28,30,30,28,24,20,16,13,10, 8],
        [7, 9,11,14,17,21,24,26,26,24,21,17,14,11, 9, 7],
        [6, 7, 9,11,14,17,20,22,22,20,17,14,11, 9, 7, 6],
        [5, 6, 7, 9,11,14,16,18,18,16,14,11, 9, 7, 6, 5],
        [4, 5, 6, 7, 9,11,13,14,14,13,11, 9, 7, 6, 5, 4],
        [3, 4, 5, 6, 7, 9,10,11,11,10, 9, 7, 6, 5, 4, 3],
        [2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2]
    ]

    kernel_sum = sum(sum(row) for row in kernel)

    for y in range(height):
        for x in range(width):
            total_r = 0
            total_g = 0
            total_b = 0

            for h in range(16):
                for w in range(16):
                    newx = x + (w - 8)
                    newy = y + (h - 8)
                    
                    if 0 <= newx < width and 0 <= newy < height:
                        p = image.get_pixel(newx, newy)
                        weight = kernel[h][w]

                        total_r += p[0] * weight
                        total_g += p[1] * weight
                        total_b += p[2] * weight

            avg_r = total_r // kernel_sum
            avg_g = total_g // kernel_sum
            avg_b = total_b // kernel_sum

            new_image.set_rgb(x, y, avg_r, avg_g, avg_b)

    return new_image


def main():
    filename = get_file()
    image = SimpleImage(filename)
    image.show()
    image = make_gaussian_blur(image)
    image.show()


def get_file():
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()