
from PIL import Image
from io import BytesIO
import io
from xeger import Xeger
import tkinter as tk
import random
import numpy as np
from PIL import Image as im 

from base64 import b64encode
from os import urandom

# Value Encoding  Value Encoding  Value Encoding  Value Encoding
#      0 A            17 R            34 i            51 z
#      1 B            18 S            35 j            52 0
#      2 C            19 T            36 k            53 1
#      3 D            20 U            37 l            54 2
#      4 E            21 V            38 m            55 3
#      5 F            22 W            39 n            56 4
#      6 G            23 X            40 o            57 5
#      7 H            24 Y            41 p            58 6
#      8 I            25 Z            42 q            59 7
#      9 J            26 a            43 r            60 8
#     10 K            27 b            44 s            61 9
#     11 L            28 c            45 t            62 +
#     12 M            29 d            46 u            63 /
#     13 N            30 e            47 v
#     14 O            31 f            48 w         (pad) =
#     15 P            32 g            49 x
#     16 Q            33 h            50 y


def porcentaje_similitud(arr1, arr2):
    if arr1.shape != arr2.shape:
        raise ValueError("Los arreglos deben tener el mismo tamaño para compararlos.")
    iguales = np.sum(arr1 == arr2)
    total_elementos = arr1.size
    porcentaje = (iguales / total_elementos) * 100
    return porcentaje

def CrearPoblacion(ancho, alto, format, mode, poblacion):
    poblacionAleatoria = []
    for i in range(poblacion):
        myimage = Image.new(mode=mode, size = (ancho, alto), color = (255, 255, 255))
        for x in range(ancho):
            for y in range(alto):
                r=random.randint(0, 255)
                g=random.randint(0, 255)
                b=random.randint(0, 255)
                myimage.putpixel((x,y), value=(r,g,b))
        #myimage.show()        
        buffer = io.BytesIO()
        myimage.save(buffer, format=format)
        imagen_bytes = buffer.getvalue()
        image = Image.open(BytesIO(imagen_bytes))
        numpy_array = np.array(image)
        #print(numpy_array)
        poblacionAleatoria.append(numpy_array)
    return poblacionAleatoria

def Mutacion(hijo1, original):
    for i in range(3000):
        puntosW = random.randint(0,(width-1))
        puntosH = random.randint(0,(height-1))
        position = random.randint(0,2)
        #print(hijo1[puntosH][puntosW][position])
        if original[puntosH][puntosW][position] != hijo1[puntosH][puntosW][position]:
            hijo1[puntosH][puntosW][position] = random.randint(0,255)
            #print(hijo1[puntosH][puntosW][position])
    return hijo1

def mainLoop(hijo2, originalImg, iteration):
    for i in range(iteration):
        porcentaje = porcentaje_similitud(hijo2, originalImg)
        if porcentaje < 99.00:
            hijo2 = Mutacion(hijo2, originalImg)
            data = im.fromarray(hijo2) 
            data.save('temp_pic.png') 
            gfg_picture = tk.PhotoImage(file="temp_pic.png")
            tk.Label(right_frame,  image=gfg_picture,  bg='grey').grid(row=0,  column=0,  padx=5,  pady=5)
            tk.Label(right_frame,  text=f"Avg: {porcentaje:.2f}%",  relief=tk.RAISED).grid(row=3,  column=0,  padx=5,  pady=3,  ipadx=10)
            tk.Label(right_frame,  text=f"int: {i}",  relief=tk.RAISED).grid(row=5,  column=0,  padx=5,  pady=3,  ipadx=10)
            root.update()
        else:
            break

def startAlg():
    iterations = interations.get()
    mainLoop(hijo2, originalImg, int(iterations))
        
#IMAGEN INICIAL
filepath = "corazonp.png"
img = Image.open((filepath))
width = img.width 
height = img.height 
format = img.format
mode = img.mode
with open("corazonp.png", "rb") as image_file:
    data = image_file.read()
#byteOriImg = bytearray(data)
image = Image.open(BytesIO(data))
originalImg = np.array(image)
###################

imgPoblacion = CrearPoblacion(width, height, format, mode, 1)
hijo2 = Mutacion(imgPoblacion[0], originalImg)

root  =  tk.Tk()  # create root window
root.title("ALGORITMO GENETICOS")
root.maxsize(900,  600)  # width x height
root.config(bg="skyblue")

# Create left and right frames
left_frame  =  tk.Frame(root,  width=200,  height=  400,  bg='grey')
left_frame.grid(row=0,  column=0,  padx=10,  pady=5)

right_frame  =  tk.Frame(root,  width=650,  height=400,  bg='grey')
right_frame.grid(row=0,  column=1,  padx=10,  pady=5)

# Create frames and labels in left_frame
tk.Label(left_frame,  text="Original Image",  relief=tk.RAISED).grid(row=0,  column=0,  padx=5,  pady=5)
image  =  tk.PhotoImage(file="corazonp.png")  # edit the file name to use a different image
original_image  =  image.subsample(2,2)

tk.Label(left_frame,  image=original_image).grid(row=1,  column=0,  padx=5,  pady=5)
#tk.Label(right_frame,  image=image,  bg='grey').grid(row=0,  column=0,  padx=5,  pady=5)

tool_bar  =  tk.Frame(left_frame,  width=180,  height=185,  bg='grey')
tool_bar.grid(row=2,  column=0,  padx=5,  pady=5)

def clicked():
    '''if button is clicked, display message'''
    print("Clicked.")

# Example labels that serve as placeholders for other widgets
# tk.Label(tool_bar,  text="Tools",  relief=tk.RAISED).grid(row=0,  column=0,  padx=5,  pady=3,  ipadx=10)
# tk.Label(tool_bar,  text="Filters",  relief=tk.RAISED).grid(row=0,  column=1,  padx=5,  pady=3,  ipadx=10)

# # For now, when the buttons are clicked, they only call the clicked() method. We will add functionality later.
# tk.Button(tool_bar,  text="Select",  command=clicked).grid(row=1,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')
# tk.Button(tool_bar,  text="Crop",  command=clicked).grid(row=2,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')
# tk.Button(tool_bar,  text="Rotate &amp; Flip",  command=clicked).grid(row=3,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')
# tk.Button(tool_bar,  text="Resize",  command=clicked).grid(row=4,  column=0,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')
tk.Label(tool_bar,  text="Iteraciones",  relief=tk.RAISED).grid(row=0,  column=1,  padx=5,  pady=3,  ipadx=10)
interations = tk.Entry(tool_bar)
interations.grid(row=1,  column=1,  padx=5,  pady=3,  ipadx=10)
tk.Button(tool_bar,  text="Iniciar",  command=startAlg).grid(row=2,  column=1,  padx=5,  pady=5,  sticky='w'+'e'+'n'+'s')

root.mainloop()








    





