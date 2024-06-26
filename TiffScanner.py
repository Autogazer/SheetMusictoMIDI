

from PIL import Image
import os
import cv2
import numpy as np


def find_pixel_address(image_path, image_path_to_sample):
    # Open the TIFF image
    image = Image.open(image_path)
    image_to_sample = Image.open(image_path_to_sample)
    # Convert the image to RGB mode if it's not already in that mode
    image = image.convert("RGB")
    image_to_sample = image_to_sample.convert("RGB")

    # Get the pixel data of the image
    pixels = image.load()
    #pixels_to_sample = image_to_sample.load()
    #image.show()
    

    # Initialize a list to store the coordinates of pixels with the target color
    target_pixels = []
    cropped_samples = []
    bad_cropped_samples = []
    
    # Iterate through each pixel in the image
    for x in range(image.width):
        for y in range(image.height):
            # print pixel values
            # print(pixels[x,y])
            sample = get_cropped_sample(x, y, image_to_sample)
            np_sample = np.array(sample)
            # Check if the pixel color matches the target color
            if (pixels[x, y][0] >= 200) & (pixels[x,y][1] <= 100) & (pixels[x,y][2] <= 100):
                # If it matches, add the coordinates to the list
                target_pixels.append((pixels[x, y]))
                     
                sample = get_cropped_sample(x, y, image_to_sample)
                np_sample = np.array(sample)

                if is_less_than_75_percent_white_space(np_sample) == True:
                    cropped_samples.append(get_cropped_sample(x, y, image_to_sample)) 
                    # cropped_samples.append(get_cropped_sample(x, y, image))
                            
                            #print('found a red')
                            #print(pixels[x,y])
            
            elif (pixels[x,y][0] <= 30) & (pixels[x,y][1] <= 30) & (pixels[x,y][2] <= 30):

                sample = get_cropped_sample(x, y, image_to_sample)
                np_sample = np.array(sample)
                if is_less_than_75_percent_white_space(np_sample) == True:
                        bad_cropped_samples.append(get_cropped_sample(x, y, image_to_sample)) 
    
    return target_pixels, cropped_samples, bad_cropped_samples

def is_less_than_75_percent_white_space(image):
    # Read the image
    # image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Threshold the image to create a binary image
    _,binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # Count total pixels and white pixels
    total_pixels = binary_image.size
    white_pixels = np.sum(binary_image == 255)
    
    # Calculate the percentage of white space
    whitespace_percentage = (white_pixels / total_pixels) * 100
    
    # Check if less than 75% white space
    if whitespace_percentage < 90:
        return 1
    else:
        return 0

def get_cropped_sample(x_cor, y_cor, image):

    # Coordinates of the pixel around which you want to crop
    #x_cor = 100  # Replace with the x-coordinate of the pixel
    #y_cor = 150  # Replace with the y-coordinate of the pixel

    # Define the size of the cropped region around the pixel
    crop_width = 50  # Width of the cropped region
    crop_height = 120  # Height of the cropped region

    # Calculate the bounding box for cropping
    left = x_cor - crop_width // 2
    upper = y_cor - crop_height // 2
    right = x_cor + crop_width // 2
    lower = y_cor + crop_height // 2

    # Crop the image around the specified pixel
    cropped_image = image.crop((left, upper, right, lower))

    # Save or display the cropped image
    #cropped_image.show()  # Displays the cropped image
    return cropped_image
    # cropped_image.save("cropped_image.jpg")  # Saves the cropped image to a file

# Example usage:
image_path = os.getcwd() + '/tiffs/test1-line.tif'  # Replace "your_image.tiff" with the path to your TIFF image file
image_path_to_sample = os.getcwd() + '/tiffs/_page_2.tiff'
pixel_addresses, correct_cropped_samples, incorrect_cropped_samples = find_pixel_address(image_path, image_path_to_sample)

# print("Pixel addresses with target color:", pixel_addresses)
print('number of found red pixels = ' + str(len(pixel_addresses)))

sample_size = len(correct_cropped_samples)

# for i in range(10):
#    print((pixel_addresses[i]))
# for i in range(5): 
#    incorrect_cropped_samples[i].show()

# for i in range(sample_size-10, sample_size - 1):
#     incorrect_cropped_samples[i].show()

# print('size of cropped samples = ' + str(len(incorrect_cropped_samples)))

# np.save('centered_staff', correct_cropped_samples)
# np.save('uncentered_samples', incorrect_cropped_samples)

train_data_size = len(correct_cropped_samples) * 2

rand_pos_indexs = np.array(range(len(correct_cropped_samples)))
np.random.shuffle(rand_pos_indexs)
rand_neg_indexs = np.array(range(len(incorrect_cropped_samples)))
np.random.shuffle(rand_neg_indexs)

training_set = []
training_labels = []

for i in range (train_data_size):
    if (i%2 == 0):
        training_set.append(correct_cropped_samples[rand_pos_indexs[i//2]])
        training_labels.append(1)
    else:
        training_set.append(incorrect_cropped_samples[rand_neg_indexs[i//2]])
        training_labels.append(0)

np.save('training_images', training_set)
np.save('training_labels', training_labels)