# Definition of the Car class
class Car:
    # Constructor method to initialize a Car instance with provided attributes
    def __init__(self, carId, dataMat, marca, modelo, categ, dataRev, email):
        # Assigning provided values to instance variables
        self.carId = carId
        self.dataMat = dataMat
        self.marca = marca
        self.modelo = modelo
        self.categ = categ
        self.dataRev = dataRev
        self.email = email

    # Class method to create a Car instance from user input
    @classmethod
    def from_user_input(cls):
        # Taking user input for each attribute
        carId = input("Introduza a matrícula da viatura: ")
        dataMat = input("Introduza a data da matrícula: ")
        marca = input("Introduza a marca da viatura: ")
        modelo = input("Introduza o modelo da viatura: ")
        categ = input("Introduza a categoria da viatura: ")
        dataRev = input("Introduza a data da última revisão: ")
        email = input("Indique o endereço de email a notificar: ")

        # Creating and returning a new Car instance with user-provided values
        return cls(carId, dataMat, marca, modelo, categ, dataRev, email)
