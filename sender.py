from PIL import Image
import numpy as np

def make_matrix(contents):
    matrix = []
    for i in range(0,len(contents),3):
        matrix.append([ord(char) for char in contents[i:i+3]])
    return matrix

def get_size(length):
    height = length
    width = 1
    for i in range(1, length//2):
        if length%i==0:
            if height>length//i:
                height = length//i
                width = i
    return width,height

def make_Image(matrix):
    width,height = get_size(len(matrix))
    array = np.zeros([height*50,width*50,3], dtype=np.uint8)
    for i in range(1, height+1):
        for j in range(1, width+1):
            array[(i-1)*50:i*50,(j-1)*50:j*50] = matrix[(i-1)*width + j-1]
    img = Image.fromarray(array)
    img.save('test.png')
    print("Output Stored in test.png")

file_name = input("Enter Filename: ")
f=open(file_name, "r")
contents = str(f.read())
if len(contents)%3!=0:
    padd_length = 3 - len(contents)%3
    contents = contents.ljust(len(contents) + padd_length,'x')
matrix = make_matrix(contents)
make_Image(matrix)
print("done")
