class node(object):
	es_inicial = False
	x = 0
	y = 0 
	color = ()
	def __init__(self,es_inicial,x,y,color):
		self.es_inicial = es_inicial
		self.x = x
		self.y = y
		self.color = color
#El código anterior define una clase llamada node que se usa para crear objetos que representan nodos en un gráfico. Esta clase tiene cuatro atributos: initial (booleano), x, y (enteros) y color (tupla). El método __init__ se usa para inicializar los atributos de cada nodo cuando se crea.