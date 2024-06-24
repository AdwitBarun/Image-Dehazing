# Single-Image-Dehazing-Python
python implementation of the paper: "Efficient Image Dehazing with Boundary Constraint and Contextual Regularization"

## Installation and Running the tests

### method 1
  ```
  pip install image_dehazer
  ```
  
  **Usage:**
  ```
  import image_dehazer										# Load the library

  HazeImg = cv2.imread('image_path')						# read input image -- (**must be a color image**)
  HazeCorrectedImg, HazeTransmissionMap = image_dehazer.remove_haze(HazeImg)		# Remove Haze

  cv2.imshow('input image', HazeImg);						# display the original hazy image
  cv2.imshow('enhanced_image', HazeCorrectedImg);			# display the result
  cv2.waitKey(0)											# hold the display window
  ```
### user controllable parameters (with their default values):
```
airlightEstimation_windowSze=15
boundaryConstraint_windowSze=3
C0=20
C1=300
regularize_lambda=0.1
sigma=0.5
delta=0.85
showHazeTrasmissionMap=True
```
### method 2

  1. Go to the src folder
  2. run the file "example.py"
  3. sample images are stored in the "Images/" folder
  4. Output images will be stored in the "outputImages/" folder


# Libraries needed:
  1.numpy==1.19.0
  
  2.opencv-python
  
  3.scipy

# Theory
This code is an implementation of the paper "Efficient Image Dehazing with Boundary Constraint and Contextual Regularization"
The algorithm can be divided into 4 parts:
  - Airlight estimation
  - Calculating boundary constraints
  - Estimate and refine Transmission
  - Perform Dehazing using the estimated Airlight and Transmission
  
