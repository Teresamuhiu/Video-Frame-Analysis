# First, install OpenCV: pip install opencv-python matplotlib
import cv2  # Library for image and video processing
import matplotlib.pyplot as plt  # Library for showing images

# Name of the video you want to process
video_name = 'test.mp4'

# Open the video file
video = cv2.VideoCapture(video_name)

# Check if video opened successfully
if not video.isOpened():
    print("Oops! Can't open the video.")
    exit()

# Create a folder to save processed frames
import os
os.makedirs('my_frames', exist_ok=True)

# Counter to keep track of frames
frame_number = 0

# Keep processing frames until video ends
while True:
    # Read a single frame from video
    success, image = video.read()
    
    # Stop if no more frames
    if not success:
        break
    
    # Turn colorful image to black and white
    black_and_white = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Find edges in the black and white image
    edge_image = cv2.Canny(black_and_white, 50, 150)
    
    # Save the edge image
    cv2.imwrite(f'my_frames/frame_{frame_number}.png', edge_image)
    
    # Show first 3 frames to help understand what's happening
    if frame_number < 3:
        plt.figure(figsize=(10, 4))
        plt.subplot(1, 2, 1)
        plt.title('Black and White')
        plt.imshow(black_and_white, cmap='gray')
        plt.subplot(1, 2, 2)
        plt.title('Edges')
        plt.imshow(edge_image, cmap='gray')
        plt.show()
    
    # Count frames
    frame_number += 1

# Close the video
video.release()

# Tell user how many frames were processed
print(f"I processed {frame_number} frames! Check the 'my_frames' folder.")