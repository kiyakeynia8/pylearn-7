import os
import imageio

file_list = sorted(os.listdir("Assignment 8/tamrin/gift/images"))

IMAGES = []

for file_name in file_list:
    file_path = "Assignment 8/tamrin/gift/images/" + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)

imageio.mimsave("Assignment 8/tamrin/gift/my_output.gif",IMAGES)