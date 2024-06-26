

from PIL import Image
import os
import cv2
import numpy as np
from CheckWhiteSpace import check_white_space
from TiffScanner import find_pixel_address

# Example usage:
image_path = os.getcwd() + '/tiffs/test1-line.tif'  # Replace "your_image.tiff" with the path to your TIFF image file
image_path_to_sample = os.getcwd() + '/tiffs/_page_2.tiff'
pixel_addresses, correct_cropped_samples, incorrect_cropped_samples = find_pixel_address(image_path, image_path_to_sample)

# print("Pixel addresses with target color:", pixel_addresses)
print('number of found red pixels = ' + str(len(pixel_addresses)))

sample_size = len(correct_cropped_samples)

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