# Importing the 'Car' class from the 'Car' module
from Car import Car

# Importing the 'DatabaseManager' class from the 'DatabaseManager' module
from DatabaseManager import DatabaseManager

# Creating an instance of the DatabaseManager class
database = DatabaseManager()


# Main function for the program
def main():
    # Infinite loop to keep the program running until the exit option is selected
    while True:
        # Printing menu options
        print("Opções:")
        print("Prima [1] para inserir viatura.")
        print("Press [2] para mostrar todas as viaturas.")
        print("Press [3] para mostrar uma viatura.")
        print("Press [4] para atualizar uma viatura.")
        print("Press [5] para remover uma viatura.")
        print("Press [6] para sair.")

        try:
            # Taking input choice
            choice = int(input("Opção: "))

            # Handling different choices
            if choice == 1:
                # Taking input for car details
                car = Car.from_user_input()
                # Inserting the car into the database
                database.insert(car)

            elif choice == 2:
                # Fetching all cars data from the database
                data = database.fetch_all()
                for car in data:
                    print(car)

            elif choice == 3:
                # Showing details of a specific car based on their ID
                carId = input("Introduza a matrícula da viatura: ")
                data = database.fetch_one(carId)
                if data is None:
                    print("Esta viatura não se encontra na base de dados!")
                else:
                    print(data)

            elif choice == 4:
                # Updating details of a specific car
                carId = input("Introduza a matrícula da viatura: ")
                updated_car = Car.from_user_input()
                # Updating the car in the database
                database.update(carId, updated_car)
                print("Viatura atualizada com sucesso!")

            elif choice == 5:
                # Deleting a specific car
                carId = input("Introduza a matrícula da viatura: ")
                database.delete(carId)
                print("Viatura removida com sucesso!")

            elif choice == 6:
                # Exiting the program                        
                break
                
            else:
                # Handling invalid choices
                print("Invalid option key! Please try again!")

        except Exception as e:
            # Handling exceptions and displaying an error message
            print(e)
            print("Invalid student! Please try again!")


# Entry point of the program
if __name__ == "__main__":
    # Calling the main function when the script is executed
    main()
