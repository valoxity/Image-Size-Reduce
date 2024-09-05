from PIL import Image
import os
import glob

# Specify the folder name you want to create
folder = 'compressed_images'

# Get the current directory
current_directory = os.getcwd()

# Combine the current directory with the folder name
folder_path = os.path.join(current_directory, folder)

# Check if the folder already exists
if not os.path.exists(folder_path):
    # If the folder doesn't exist, create it
    os.makedirs(folder_path)
    print(f"Folder '{folder}' created successfully.")
else:
    print(f"Folder '{folder}' already exists.")

# Define the file extensions to search for
file_extensions = ['png', 'jpeg', 'jpg']

# Define the target size in KB
target_size_kb = 2048  # 2MB

# Iterate through the files in the directory
for extension in file_extensions: 
    image_files = glob.glob(os.path.join(current_directory, f'*.{extension}'))
    
    # Output folder path
    output_folder = os.path.join(current_directory, folder)

    # Iterate through the image files
    for file_path in image_files:
        # Extract file name without path
        file_name = os.path.basename(file_path)
        
        # Open the image file
        image = Image.open(file_path)
        
        # Set initial quality value
        quality = 65

        width, height = image.size
        # new_size = (width//2, height//2)
        new_size = (1344,756)
        resized_image = image.resize(new_size)


        # Remove metadata and reduce image quality to reduce file size
        resized_image.save(os.path.join(output_folder, file_name), quality=50, optimize=True)
        
        
        # # Check if the file size is greater than the target size
        # while os.path.getsize(os.path.join(output_folder, file_name)) > target_size_kb * 1024 and quality > 5:
        #     # Decrease quality by 5 each time
        #     quality -= 5
            
        #     # Save the image with reduced quality
        #     image.save(os.path.join(output_folder, file_name), quality=quality, optimize=True)
        
        print(f"({file_name}) Successfully compressed to less than {target_size_kb} KB.")
        print("\n")

print("-------------------------------------------------------------------")
print("Please don't forget to visit our website (https://valoxity.com/) :)")
print("-------------------------------------------------------------------")
