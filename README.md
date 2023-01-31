# Lab-IA

Para ejecutar el codigo se debe installar: 

#pip install opencv-python
#pip install pillow

Para las opciones 2, 3 y 4 considerar que toma más tiempo para encontrar la solucion

Link prueba rapida solucion laberinto: https://youtu.be/ta7y2RfzTNg
-------------------------------------------------------
Explicacion de porqué escogimos: 
-> A* con Euristica Euclidiana: porque es útil para resolver problemas de búsqueda en grafos porque combina la búsqueda informada y la búsqueda en anchura para encontrar una solución óptima de manera eficiente. Además proporciona una estimación precisa de la distancia hasta el objetivo, permitiendo a A* priorizar los nodos más cercanos y reducir el tamaño del espacio de búsqueda. Esto se traduce en una mejora en la velocidad de la búsqueda y una solución más óptima.

-> A* con Euristica Chebyshev: porque es útil para resolver problemas de búsqueda en grafos que tienen restricciones de movimiento diagonal. En este cazo el maze necesita considerar todas las opciones posibles para encontrar el camino adecuado. Además que es ventajosa ya que como se basa en la distancia más larga entre dos puntos y es adecuada para entornos donde los movimientos diagonales tienen un costo igual al de los movimientos horizontales y verticales.
