from PIL import Image
import numpy as np

def get_matrix(array, width, height):
    matrix = []
    for i in range(0,height,50):
        for j in range(0, width, 50):
            matrix.append([k for k in array[i][j]])
    return matrix

def get_contents(matrix):
    contents = ""
    for i in matrix:
        for j in i:
            contents += chr(j)
    return contents

def writeFile(contents):
    output = input("Output File Name: ")
    f = open(output, "w+")
    f.write(contents)
    f.close()
    print("done")

file_name = input("Enter Filename: ")
image = Image.open(file_name)
width,height = image.size
array = np.array(image)
matrix = get_matrix(array, width, height)
contents = get_contents(matrix)
writeFile(contents)
