import os 
#Clase para definir un vertice 
class vertice:
    #Se crea un constructor
    def __init__(self,i):
        """
        
        """
        #Iniciamos la variable Id
        self.id=i
        #Inicializamos la variable visitado
        self.visitado=False
        #Inicializamos la variable self 
        self.nivel=-1
        #Inicializamos la varible vecinos
        self.vecino=[]

    def agregarVecino(self,v):
        #En caso de que no exista el vertice creado
        if not v in self.vecino:
            #Agregar al apendice 
            self.vecino.append(v)

class grafica:
    #Se crea el metodo construcutor
    def __init__(self):
        #Creamos un diccionario para guardar los vertices 
        self.vertices={}

    def agregarVertice(self,v):
        #En caso de que no exista el vertice creado
        if v not in self.vertices:
            #Agregar al apendice 
            self.vertices[v]= vertice(v)
    
    def agregararista(self,a,b):
        #Conectara las vertices vecinas por una arista si se encuentran alamecenados
         #si se encuentra en el vertice entonces accederemos a los vertices
        if  a in self.vertices and b in self.vertices:
            #Creamos la arista de una lado hacia el otro
            self.vertices[a].agregarVecino(b)
            #Creamos la arista desde un vertice hasta su inicial para crear bidireccionolidad 
            self.vertices[b].agregarVecino(a)

def main():
    #incializamos la funcion grafica 
    g=grafica()
    #Creamos los nodos del grafo
    l=["Casa","Parque","Iglesia","Lago","Centro","Discoteca","Escuela","Universidad"]
    #Para el vertice en cada nada 
    for v in l :
        #Agregamos los vertices 
        g.agregarVertice(v)
    #Creamos las aritas 
    a=["Casa","Iglesia","Casa","Parque","Casa","Lago","Iglesia","Centro","Parque","Centro","Lago","Centro","Centro","Escuela","Centro","Universidad","Escuela","Discoteca","Universidad","Discoteca"]
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