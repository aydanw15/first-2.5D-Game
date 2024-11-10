import os

#Directory containing the images
directory = 'X:/assetsForGame'  #Replace with your actual path

#Assuming images are named in sequence and we know the directions and positions
directions = ["N", "E", "S", "W"]
y_range = 20
x_value = 0  #This can be changed if more x values are needed

current_index = 0
image_files = sorted(os.listdir(directory))  #Make sure they are in order

for y in range(y_range):
    for direction in directions:
        if current_index < len(image_files):
            old_name = image_files[current_index]
            new_name = f"IMG_{x_value}_{y}_{direction}.jpg"
            
            old_path = os.path.join(directory, old_name)
            new_path = os.path.join(directory, new_name)
            
            os.rename(old_path, new_path)
            print(f"Renamed '{old_name}' to '{new_name}'")
            
            current_index += 1
