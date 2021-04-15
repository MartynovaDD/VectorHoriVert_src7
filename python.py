from PIL import Image
from numpy import array

def func(InputFile1,InputFile2,OutputFile):
    try:
        background = Image.open(InputFile1,'r')
    except FileNotFoundError:
        print("Error! Cannot find file...")
        exit(-1)
    try:
        foreground = Image.open(InputFile2,'r')
    except FileNotFoundError:
        print("Error! Cannot find file...")
        exit(-1)
    arr1=array(background)
    arr2=array(foreground)
    if arr1.shape[0]<arr2.shape[0] or arr1.shape[1]<arr2.shape[1]:
        print("Размер неверный")
        exit()
    k = int((arr1.shape[0]-arr2.shape[0])/2)
    m = int((arr1.shape[1]-arr2.shape[1])/2)
    for i in range(k,k+arr2.shape[0]):
        for j in range(m,m+arr2.shape[1]):
            arr1[i,j,0]=arr2[i-k,j-m,0]
            arr1[i,j,1]=arr2[i-k,j-m,1]
            arr1[i,j,2]=arr2[i-k,j-m,2]
    img = Image.fromarray(arr1)
    img.save(OutputFile)
arg1 = input()
arg2 = input()
arg3 = input()
func(arg1,arg2,arg3)
