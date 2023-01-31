from nodo import node 
from PIL import Image #ip install pillow
from principal import Framework as fw
import numpy as np
import cv2 #pip install opencv-python
import principal as p
from principal import principal

class Laberinto(object):
    nodes = []
    def __init__(self,matriz):

        x = 0
        while x < len(matriz):
            contador=0
            contador2 =0
            nodos = []#lista para guardar los nodos
            y = 0
            while y < len(matriz):
                if int(matriz[x][y][0]) >= 230 and int(matriz[x][y][1]) >= 0 and int(matriz[x][y][1]) <= 20 and int(matriz[x][y][2]) >= 0 and int(matriz[x][y][2]) <= 20 and contador == 0:
                    nodos.append(node(True,x,y,(int(matriz[x][y][0]),int(matriz[x][y][1]),int(matriz[x][y][2]))))
                    contador = 1 #el nodo es inicial ya que es 255,0,0
                    print("X:",x,"Y:",y,"RGB:",matriz[x][y])

                # elif(contador2==0):
                #     nodos.append(node(True,x,y,(int(matriz[x][y][0]),int(matriz[x][y][1]),int(matriz[x][y][2]))))
                #     contador=1
                else:
                    nodos.append(node(False,x,y,(int(matriz[x][y][0]),int(matriz[x][y][1]),int(matriz[x][y][2]))))
                    #print("X:",x,"Y:",y,"RGB:",matriz[x][y])
                y += 1
            self.nodes.append(nodos)
            x += 1
# Se crea una clase Laberinto, que contiene un atributo nodos, una lista que guarda los objetos de tipo node.
# En el constructor __init__ se itera sobre la matriz que se recibe como parámetro, y se crean nodos con sus respectivos atributos.
# El contador se usa para determinar si el nodo es el inicial, ya que en la matriz solo hay uno.






def iniciar():
    n = int(input("Ingrese n:\n"))
    mat = p.discretizar(p.im,n) # Carga la imagen mediante p.im con imagen.open, como segundo parametro recibe n, define la calidad de la imagen.
    # print("mat es : ")
    # print(mat)
    nodos =Laberinto(mat) # Creamos los nodos a partir de la matriz generada por la imagen y por n.
    # print("Nodos es : ")
    # print(nodos.nodes)
    varInicial = ()#Se crea una variable llamada varInicial
    x = 0 #Se define la variable x iniciandola en 0, esto se usara para saber cual es el vector inicial.
    for row in nodos.nodes: #Se define el vector inicial.
        for item in row:
            if(item.es_inicial and x == 1):
                varInicial = (item.x,item.y)#Cuando encuentre un valor de 255 ,0 ,0 osea un rojo lo define como punto inicial.
            x=x=1
    print("La posicion del nodo inicial es "+str(varInicial)) #Se muestra el vector.

    discret_matrix = Image.fromarray(mat.astype(np.uint8))
    final_matrix = discret_matrix.resize((1000, 1000))
    final_matrix.show()
    final_matrix.save("imagenGuardada.bmp")
    while True:
        print("Seleccione el algoritmo:\n1.Breadth First Search (BFS)\n2.Depth First Search (DFS)\n3.A* con Euristica Euclidiana\n4.A* con Euristica Chebyshev\n5.salir")
        option = input()
        print("opcion es igual a ",option)
        if option == "1":
            problem1 = fw(nodos.nodes,varInicial,1)
            solucion1 = principal(problem1)
            image_solution(solucion1,problem1,mat,1)
        elif option == "2":
            print("Entre al 2")
            problem2 = fw(nodos.nodes,varInicial,2)
            solucion2 = principal(problem2)
            image_solution(solucion2,problem2,mat,2)
        elif option == "3":     
            problem3 = fw(nodos.nodes,varInicial,3)
            solucion3 = principal(problem3)
            image_solution(solucion3,problem3,mat,3)
        elif option == "4":
            problem4 = fw(nodos.nodes,varInicial,4)
            solucion4 = principal(problem4)
            image_solution(solucion4,problem4,mat,4)
        elif option == "5":
            break
        else:
            print("Selecciona una opcion: ")


def image_solution(solucion,problem,matrix,n):
    print("La solucion es:")
    print(solucion)
    print("El problema es:")
    print(problem)
    print("La matrix es:")
    print(matrix)
    color = (93,173,226) if n == 1 else (186,74,0) if n == 2 else (66,0,50) if n == 3 else (247,220,111)
    sol = matrix
    if solucion.final_path == False: 
        print ('No hay solucion')
    else:
        for pix in solucion.final_path:
            if pix == problem.initial or pix in problem.goal:
                pass
            else:
                sol[pix[0]][pix[1]] = color
        

    new_im = Image.fromarray(matrix.astype(np.uint8))
    new_image = new_im.resize((1000, 1000))
    new_image.show()
    print ('La solucion es:')
    new_image.save("solucion"+str(n)+".bmp")



iniciar()
#resuelve la ruta óptima para llegar a un punto de destino a partir de un punto de origen. El programa tiene la capacidad de recibir una imagen como entrada, la cual es discretizada para crear una matriz de nodos, cada uno de los cuales contiene información sobre la ubicación y el color de los pixeles. El usuario luego puede elegir entre varios algoritmos de búsqueda para encontrar la ruta óptima. Una vez que el camino óptimo se encuentra, se puede ver en una imagen discretizada de la imagen de entrada y se puede guardar como una imagen de salida.