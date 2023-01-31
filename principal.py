#Se importan las librerias necesarias para el funcionamiento
from numpy import asarray
import numpy as np
from PIL import Image
import itertools


im = asarray(Image.open('1.bmp'))

class principal(object):
	final_path = []
	def __init__(self,problem):
		self.problem = problem#asignamos el problema a una variable
		print("Grap retorna lo siguiente:")
		print(self.graph_search(problem))
		self.final_path = self.graph_search(problem)#asignamos el resultado del metodo graph_search al atributo final_path


	def breadth_first(self,frontier):
		path = frontier[0]#inicializamos el camino con el primer elemento de la lista de fronteras
		for index in range(len(frontier)-1):#recorremos la lista de fronteras
			if len(frontier[index+1]) > len(path):#si la longitud del camino siguiente en la lista es mayor que el camino actual
				path = frontier[index+1]#actualizamos el camino actual con el camino siguiente
		return path#devolvemos el camino mas largo de la lista

	def depth_first(self,frontier):
		print("Entre al metodo del 2.")
		path = frontier[0]#inicializamos el camino con el primer elemento de la lista de fronteras
		for index in range(len(frontier)-1):#recorremos la lista de fronteras
			if len(frontier[index+1]) < len(path):#si la longitud del camino siguiente en la lista es menor que el camino actual
				path = frontier[index+1]#actualizamos el camino actual con el camino siguiente
		return path#devolvemos el camino mas corto de la lista de fronteras


	def euclidea(self,punto1,punto2):
		distancia = np.sqrt((punto1[0]-punto2[0])**2 + (punto1[1]-punto2[1])**2)
		return distancia#devolvemos la distancia euclidea

	def chebyshev(self,punto1,punto2):
		return max((punto2[0]-punto1[0]),(punto2[1]-punto1[1]))#calculamos la distancia de chebyshev entre dos puntos


	def A_estrella(self,frontier,euristica):
		func = []
		for goal in (self.problem.goal):
			for path in frontier:
				if euristica == 1:
					func.append((len(path) + self.euclidea((path[len(path)-1][0],path[len(path)-1][1]),goal),path))
				elif euristica == 2:
					func.append((len(path) + self.chebyshev((path[len(path)-1][0],path[len(path)-1][1]),goal),path))
		return min(func)[1]


	def remove_choice(self,frontier):
		if self.problem.met == 1:
			path = self.breadth_first(frontier)
		elif self.problem.met == 2:
			path = self.depth_first(frontier)
		elif self.problem.met == 3:
			path = self.A_estrella(frontier,1)
		else:
			path = self.A_estrella(frontier,2)
		print("Regrese el camino")
		return path


	def graph_search(self, problem):##Problema 2 prueba
		frontier = [[problem.initial]]
		explored = []
		final_path = []
		while True:
			if len(frontier):
				print("Ando llamando al ciclo")
				path = self.remove_choice(frontier)

				frontier.remove(path)
				s = path[-1] # Le dice traiga el ultimo color del path
				explored.append(s)
				#print(s)
				if problem.goal_test(s):
					return path
				for a in problem.actions(s):
					result = problem.result(s,a)
					if result not in explored:
						new_path = []
						new_path.extend(path)
						new_path.extend([result])
						frontier.extend([new_path])
			else:
				return False

					
#El código anterior es una clase que resuelve problemas usando una búsqueda en grafos. Esta clase contiene varias funciones útiles para la solución del problema. Estas funciones incluyen: breadth_first, depth_first, euclidea, chebyshev, A_estrella y remove_choice. Estas funciones permiten al problema encontrar el camino óptimo a través de un grafo. El método graph_search es el método principal que se utiliza para encontrar la solución óptima al problema. Esta función recorre el grafo y busca los caminos posibles para llegar a la solución óptima.

#Se define la clase Framework que contiene los atributos necesarios para el funcionamiento del framework
class Framework(object):
	initial = ()
	matrix = []
	goal = ()
	met = 0
	def __init__(self, matrix, initial,met):
		self.matrix = matrix
		self.dim = len(matrix)
		self.initial = initial
		self.goal = self.get_goal()
		self.met = met

#Se define la funcion actions que devuelve una lista de acciones posibles dada una posición
	def actions(self,s):
		actions = []
		try:
		
			if self.matrix[s[1]][s[0]+1].color == (255,255,255) and s[1] < 500:
				actions.append('derecha')
			if self.matrix[s[1]][s[0]-1].color ==(255,255,255) and s[1] >0: 
				actions.append('izquierda') 
			if self.matrix[s[1]+1][s[0]].color ==(255,255,255) and s[0] < 500:
				actions.append('abajo') 
			if self.matrix[s[1]-1][s[0]].color ==(255,255,255) and s[0] > 0:
				actions.append('arriba') 
		except:
			#print (s)
			pass
		#print(actions)
		return actions

#Se define la funcion result que devuelve la posición resultante de aplicar una acción a una posición
	def result(self,s,a):
		#print ('result',s,a)
		result = self.matrix[s[1]][s[0]+1] if a == 'derecha' else ( self.matrix[s[1]][s[0]-1] if a == 'izquierda' else ( self.matrix[s[1]-1][s[0]] if a == 'arriba' else ( self.matrix[s[1]+1][s[0]] if a == 'abajo' else 'nada')))
		#print('result adentro', result)
		return result.y,result.x

#Se define la funcion goal_test que devuelve true si la posición coincide con el objetivo
	def goal_test(self,s):
		print("El color es ", self.matrix[s[0]][s[1]].color)
		#print('goal test',s,'color',self.matrix[s[0]][s[1]].color)
		if self.matrix[s[0]][s[1]].color[0] >= 0 and self.matrix[s[0]][s[1]].color[0] <= 20 and self.matrix[s[0]][s[1]].color[1] >= 240 and self.matrix[s[0]][s[1]].color[1] <= 254 and self.matrix[s[0]][s[1]].color[2] >= 0 and self.matrix[s[0]][s[1]].color[2] <= 20:
			return True
		else:
			return False

#Se define la funcion step_cost que devuelve el costo de una acción dada dos posiciones
	def step_cost(self,s0,a,s1):
		return 1

#Se define la función path_cost que devuelve el costo total de un conjunto de estados
	def path_cost(self,estados):
		return len(estados)

#Se define la función get_goal que devuelve una lista de los objetivos en el mapa.
	def get_goal(self):
			#print("Se esta corriendo la funcion:")
			goals = []
			for row in self.matrix:
				for point in row:
					if (point.color[0]>=0 and point.color[0]<=20) and (point.color[1]>=230 and point.color[1]<=255) and (point.color[2]>=0 and point.color[2]<=20):
						goals.append((point.x,point.y))
			#print(goals)
			return goals


def discretizar(im,n):
    vector = np.array(im)
    size = vector.shape
    filas = int(size[0]/n)
    columnas = int(size[1]/n)
    matrix = np.zeros((filas,columnas,3))
    for i in range(0,filas):
        for j in range(0,columnas):
            tuple = vector[i*n:(i*n)+n,j*n:(j*n)+n,:]
            v = np.mean(tuple,axis=(0,1))
            matrix[i,j,:] = v
    return matrix


def determinate(discret_square):
	colors = []
	#print len(discret_square)
	for x,y in discret_square:
		colors.append((im[y][x][0],im[y][x][1],im[y][x][2]))

		#if 48<x<64 and 448<y<464:
		#	print((im[y][x][0],im[y][x][1],im[y][x][2]))

	r = round(colors.count((254,0,0))/529.0,2)
	r1 = round(colors.count((254,0,0))/529.0,2)
	g = round(colors.count((0,255,0))/529.0,2)
	w = round(colors.count((255,255,255))/529.0,2)
	b = round(colors.count((0,0,0))/529.0,2)

	if r+r1 > 0.00:
		return [255,0,0]
	elif g > 0.00:
		return [0,255,0]
	elif w > 0.00:
		return [255,255,255]
	else:
		return [0,0,0]


def dibujarSolucion(solucion,matrix):
    for i in range(len(solucion)):
        matrix[solucion[i][0]][solucion[i][1]] = (66,0,50)
    new_im = Image.fromarray(matrix.astype(np.uint8))
    new_image = new_im.resize((1000, 1000))
    new_image.show()
    new_image.save("solucion.bmp")
#El código anterior divide la imagen "1.bmp" en una matriz de n x n, luego toma cada cuadrado de la matriz y determina el color predominante entre los pixeles del cuadrado. Por último, crea una imagen con los colores asignados a cada cuadrado y la guarda como "solucion.bmp".


def createMatrix(): 
	matrix = np.zeros((int(len(im)/8),int(len(im[0])/8),3))
	for i in range(0,len(im),8):
		for j in range(0,len(im[0]),8):
			discret_square = list(itertools.product(range(j, j+8), range(i, i+8)))
			matrix[int(i/8),int(j/8)] = determinate(discret_square)
	return matrix





