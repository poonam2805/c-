import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("i.jpg", 1)

# Resize the images
half = cv2.resize(image, (0, 0), fx=0.1, fy=0.1)
bigger = cv2.resize(image, (1050, 1610))
stretch_near = cv2.resize(image, (780, 540), interpolation=cv2.INTER_NEAREST)

# Titles for the images
Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]

# List of images to display
images = [image, half, bigger, stretch_near]

# Create the subplot
count = 4
for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    # Convert from BGR to RGB for displaying with matplotlib
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Optionally remove axes for cleaner view

# Show the plot
plt.show()
