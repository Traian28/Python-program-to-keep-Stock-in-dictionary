class Alumno:

	def __init__(self):
		self.diccionario={}
		#self.notas={}

	def menu(self):
		opcion=0
		while opcion!=4 :
			print ("1 - Cargar alumnos ")
			print ("2 - Lista alumnos ")
			print ("3 - Listado de alumnos con notas mayor o iguales a 7 ")
			print ("4 - Finalizar programa ")
			opcion=int(input("Ingrese opcion: "))
			if opcion==1:
				self.cargar()
			elif opcion==2 :
				self.listar()
			elif opcion==3:
				self.notas_altas()
			else :
				print ("FIN PROGRAMA")

	def cargar(self):
		cantidad=int(input("Ingrese cantidad de alumnos a cargar: "))
		for x in range(cantidad):
			nom=input("Ingrese nombre: ")
			nota=int(input("Ingrese nota: "))
			self.diccionario[nom]=nota

	def listar(self):
		for nom in self.diccionario:
			print (nom, self.diccionario[nom])

	def notas_altas(self):
		for nom in self.diccionario:
			if self.diccionario[nom]>=7:
				print (nom, self.diccionario[nom])


alumno1=Alumno()
alumno1.menu()