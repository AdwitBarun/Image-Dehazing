import os
import cv2
import image_dehazer

def remove_haze_and_save(input_image_path, output_folder):
    # Read input image
    HazeImg = cv2.imread(input_image_path)
    if HazeImg is None:
        print(f"Error: Could not read image at {input_image_path}")
        return
    
    # Remove Haze
    HazeCorrectedImg, haze_map = image_dehazer.remove_haze(HazeImg, showHazeTransmissionMap=False)

    # Save haze transmission map
    haze_map_path = os.path.join(output_folder, f"haze_map_{os.path.basename(input_image_path)}")
    cv2.imwrite(haze_map_path, haze_map)

    # Save enhanced image
    enhanced_image_path = os.path.join(output_folder, f"enhanced_image_{os.path.basename(input_image_path)}")
    cv2.imwrite(enhanced_image_path, HazeCorrectedImg)

    # Display original hazy image (optional)
    cv2.imshow('original_hazy_image', HazeImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Path to the directory containing images
    input_folder = "Images"

    # Output folder to save results
    output_folder = "outputImages"
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            input_image_path = os.path.join(input_folder, filename)
            remove_haze_and_save(input_image_path, output_folder)
        else:
            print(f"Skipping {filename} as it is not a supported image format (jpg or png).")

