from keras.models import load_model
import numpy as np
from PIL import Image
import os
import io
import TiffScanner as TS
from TiffScanner import check_white_space

#Load the image
path1 = os.getcwd() + '/tiffs/_page_3.tiff'
image_path = path1
image = Image.open(image_path)

# Dimensions for the slices
slice_width = 50
slice_height = 120

# Get the dimensions of the image
image_width, image_height = image.size

# Initialize a list to hold the slices
slices = []
slc_images = []
slice_coordinates = []



# Function to calculate approved indices
def get_approved_indices(slices, white_threshold=200, white_ratio_threshold=0.75):
    approved_indices = []
    
    for index, slice_image in enumerate(slices):

        if TS.check_white_space(slice_image):
            approved_indices.append(index)
    
    return approved_indices

# Calculate approved indices
approved_indices = get_approved_indices(slices)
# print(f"Indices of approved slices: {approved_indices}")

# Get the approved slices using the indices
slices_approved = [slices[i] for i in approved_indices]
slc_approved_images = [slc_images[i] for i in approved_indices]
print(f"Number of approved slices: {len(slices_approved)}")

# Example of accessing a specific slice and its coordinates
slice_index = 0  # Change this to the index of the slice you want to access
specific_slice = slices[slice_index]
specific_coords = slice_coordinates[slice_index]
print(f"Slice {slice_index} has top-left coordinates: {specific_coords}")


#name of the array with x y coords = slice_coordinates
#name of slices with less than 75% white = slices_approved

test_data = slices_approved
test_data = np.array(test_data)

print("test_data shape:")
print(test_data.shape)

sheet_model = load_model('first_model.keras')
predictions = sheet_model.predict(test_data)

print("prediction size: " , len(predictions))
print("First few predictions")
print(predictions[100:110])

slc_approved_images[100].show()