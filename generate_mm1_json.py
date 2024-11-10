import json

# Define directions and initialize game data
directions = ["N", "E", "S", "W"]
game_data = {}

# Create game states for different positions and directions
for x in range(1, 2):  # Single value for x starting from 1  # Single value for x
    for y in range(17):  # y ranging from 0 to 16 (total 17)
        for direction in directions:
            # Create the state key in the format "x,y direction"
            key = f"{x},{y} {direction}"
            # Create the image file name in the format "IMG_x_y_direction.jpg"
            img_filename = f"/cimgs/IMG_{x}_{y}_{direction}.jpg"
            # Store the image path in the game data
            game_data[key] = {"img": img_filename}

# Write the game data to a JSON file
with open("mm1.json", "w") as json_file:
    json.dump(game_data, json_file, indent=4)
