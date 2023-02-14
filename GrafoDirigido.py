"""
Este programa simula un grafo dirigido con sus aristan tomando en cuenta los conceptos basicos de este
para poder simularlo de una manera sencilla y entendible
Autores:
José SanMartín
Versión:
VER 1.1
"""
import os 
#Clase para definir un vertice 
class vertice:
    """
    Es una clase la cual nos ayudara a generar los vertices del grafo
    ------------
       No tiene parametro de entrada
           
    Retorna:
    ------------
       No tiene parametro de retorno
    """
    #Se crea un constructor
    def __init__(self,i):
        """
    Es una funcion la cual inicializara la clase que estamos creando y todos los atributos y componente
    dentro de ella
    ------------
       i: representar la id es decir el nombre que vamos a darle a una variable 
           
    Retorna:
    ------------
       No tiene parametro de retorno
    """
        #Iniciamos la variable Id, son las letras o numeros que le daremos a los vertices
        self.id=i
        #Inicializamos la variable visitado
        self.visitado=False
        #Inicializamos la variable self 
        self.nivel=-1
        #Inicializamos la varible vecinos
        self.vecino=[]

    def agregarVecino(self,v):
        """
    Es una funcion la cual creara los "vecinos" es decir las aristas que son mas cercanas 
    una de las otra 
    ------------
       v: representar la id del vertice vecino, es decir da el nombre del vertice mas cercano
       al cual se conecta a otro
           
    Retorna:
    ------------
       No tiene parametro de retorno
    """
        #En caso de que no exista el vertice creado
        if not v in self.vecino:
            #Agregar al apendice 
            self.vecino.append(v)

class grafica:
    """
    Es una clase la cual nos ayudara a generar la "grafica" general del grafo
    ------------
       No tiene parametro de entrada
           
    Retorna:
    ------------
       No tiene parametro de retorno
    """
    #Se crea el metodo construcutor
    def __init__(self):
        """
    Es una funcion la cual inicializara la clase que estamos creando y todos los atributos y componente
    dentro de ella
    Recibe
    ------------
       No tiene parametro de entrada
           
    Retorna:
    ------------
       No tiene parametro de retorno
    """
        #Creamos un diccionario para guardar los vertices 
        self.vertices={}

    def agregarVertice(self,v):
        """
    Es una funcion la cual nos permitira agregar los vertices del grafo siempre y cuando 
    este no este ya agregado en una lista de vertices
     Recibe
    ------------
       v: Es el vertice de creado por el usuario 
           
    Retorna:
    ------------
       No tiene parametro de retorno
    """
        #En caso de que no exista el vertice creado
        if v not in self.vertices:
            #Agregar al apendice 
            self.vertices[v]= vertice(v)
    
    def agregararista(self,a,b):
        """
    Es una funcion que nos ayuda a agregar las aristas en este caso que seran a una sola direccion
    pues no tienen un orde establecido
    ------------
      a: Refiere un punto en el cual inicia la arista y se dirigira hacia b
      b: Refiere un punto en el cual  termina la arista 
           
    Retorna:
    ------------
       No tiene parametro de retorno
    """
        #Conectara las vertices vecinas por una arista si se encuentran alamecenados
         #si se encuentra en el vertice entonces accederemos a los vertices
        if  a in self.vertices and b in self.vertices:
            #Creamos la arista de una lado hacia el otro
            self.vertices[a].agregarVecino(b)
            

def main():
    """
    Es una clase la cual nos ayudara a generar la "grafica" general del grafo
    ------------
       No tiene parametro de entrada
           
    Retorna:
    ------------
       No tiene parametro de retorno
    """
    #incializamos la funcion grafica 
    g=grafica()
    #Creamos los nodos del grafo
    l=["Fuente de Agua","Tuberia A","Tuberia B","Tuberia C","Tuberia D","Tuberia E","Lavabo"]
    #Para el vertice en cada nada 
    for v in l :
        #Agregamos los vertices 
        g.agregarVertice(v)
    #Creamos las aritas 
    a=["Fuente de Agua","Tuberia A","Tuberia A","Tuberia B","Tuberia B","Tuberia C","Tuberia C","Tuberia D","Tuberia D","Tuberia E","Tuberia E","Lavabo","Lavabo","Fuente de Agua"]
    #Recorremos las lista de 2 en 2 hasta llegar al estado objetivo
    for i in range(0,len(a)-1,2):
        #creamos otra lista con cada vertice y sus vecinos
        g.agregararista(a[i],a[i+1])
    #Imprimimos cada vertice junto con sus vecinos para ver si es correcto
    for v in g.vertices:
        #Imprimimos cada vertice junto con sus vecinos para ver si es correcto
        print(v,g.vertices[v].vecino)

#Creamos un main para 
if __name__ == '__main__':
    #Creamos una tabla
    print("Nodo │  Vecinos")
    #Realizamos el main
    main()
    os.system("pause")
