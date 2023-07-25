import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Load an example image
image_path = 'holiday_groupimage-scaled2.jpg'
image = plt.imread(image_path)
image = np.array(image, dtype=np.float32) / 255.0 
print(image)# Normalize the image to values between 0 and 1

# Create a simple CNN model with a single convolutional layer
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(filters=16, kernel_size=(3, 3), activation='relu', input_shape=image.shape),
])

# Expand the dimensions of the image to match the input shape of the model
input_image = np.expand_dims(image, axis=0)

# Apply the filter to the image using the model
filtered_image = model.predict(input_image)

# Select one of the filtered channels to visualize (e.g., the first channel)
channel_to_visualize = 0
filtered_channel = filtered_image[0, :, :, channel_to_visualize]

# Display the original and filtered images
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtered_channel)  
plt.title(f'Filtered Channel {channel_to_visualize}')
plt.axis('off')

plt.show()