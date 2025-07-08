import PIL.Image 

#ASCII Characters used to build the output image
ASCII_CHAR = ["@","#","S","%","?","*","+",";",":",",","."]

# resize image according to a new width
def resize_image(image, new_width = 100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width*ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

# convert pixels to a string of ascii charecters
def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHAR[pixel//25] for pixel in pixels])
    return(characters)

def main(new_width=100):
    # get the path of the image and open the image
    path = input("Eneter a valid path name of an image: ")

    try:
        image = PIL.Image.open(path)
    
    except:
        print(path, "is not a valid pathname of an image. ")

    #convert image to ASCII
    new_image_data = pixel_to_ascii(grayify(resize_image(image)))

    #format 
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range (0, pixel_count,new_width))

    # Print 
    print(ascii_image)

    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f: 
        f.write(ascii_image)

main()