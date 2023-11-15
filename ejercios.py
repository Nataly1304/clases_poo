class Estudiante: #aca nos muestra clase estudiante de la cual como atributos tiene codigo,nombre,apellido
    
    codigo=0 # aca nos indica que codigo tiene un  valor numerico 
nombre="" # aca nos indica que nombre tiene cadena de texto   
apellido="" # aca nos indica que apellido tiene cadena de texto   

def imprimirDatos(self,codigo,nombre,apellido):
    print (self.codigo, self.nombre, self.apellido) # self en los métodos de una clase se utiliza para referirse a la instancia actual de la clase.


adso=Estudiante() # se crea objeto llamdo adso

#Accediendo a través del objeto adso a los atributos de la clase estudiante y dando valores 

adso.codigo = 1
adso.nombre = 'Sandra'
adso.apellido='Cruz'

adso.imprimir_Datos()

#Clase Constructor
class Estudiante1: #  #aca nos muestra clase estudiante1 de la cual como atributos tiene codigo,nombre,apellido 

    def __init__(self, codigo, nombre,apellido): # Método _init_ Inicializa la clase Estudiante1 con los parámetros código, nombre y apellido.
        self.codigo = codigo
        self.nombre = nombre
        self.apellido=apellido

    def imprimirInformacion(self):# en esta line nos imprime mostrando el codigo, nombre, apellido del estudiante

        print (self.codigo, self.nombre, self.apellido)

adso1 =Estudiante1(2,'Maria','Galindo') # aca se creo como una variable pero en si es una instancia de la 
# clase estuaidnte1 mostrandonos los valor de codigo que es 2, nombre que es maria y apellido que es galindo 
adso1.imprimirInformacion() # Se llama al método imprimirInformacion de la instancia adso1.

