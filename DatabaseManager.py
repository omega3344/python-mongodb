# Import libraries for environment variables
import os
from dotenv import load_dotenv

# Importing the 'pymongo' module for MongoDB interaction
import pymongo

# Definition of the PyMongoDatabase class
class DatabaseManager:
    # Constructor method to initialize the database connection
    def __init__(self):
        # Load environment variables
        load_dotenv()
        try:
            ENV_USER = os.getenv('USER')
            ENV_PASSWORD = os.getenv('PASSWORD')
            #ENV_USER = os.environ['USER']
            #ENV_PASSWORD = os.environ['PASSWORD']
        except KeyError:
            raise KeyError("Token not available!")

        # Initialize the 'client' variable to None
        client = None
        try:
            # Creating a MongoClient to connect to the local MongoDB server
            client = pymongo.MongoClient(f'mongodb+srv://{ENV_USER}:{ENV_PASSWORD}@viaturas.wbh61sv.mongodb.net/?retryWrites=true&w=majority&appName=viaturas')
            # Getting the 'guimadiesel' database from the MongoDB server
            self.db = client['guimadiesel']
            # Getting the 'viaturas' collection from the 'mongodb' database
            self.collection = self.db['viaturas']
        except Exception as e:
            # Handling exceptions and printing an error message if connection fails
            print(f"Error: {e}")
        finally:
            # Close the MongoDB client if it was initialized
            if client is None:
                client.close()
                print("Connection closed.")

    # Method to insert car data into the 'viaturas' collection
    def insert(self, car):
        try:
            # Creating a dictionary with student details
            data = {
                '_id': car.carId,
                'dataMat': car.dataMat,
                'marca': car.marca,
                'modelo': car.modelo,
                'categ': car.categ,
                'dataRev': car.dataRev,
                'email': car.email
            }
            # Inserting the car data into the 'viaturas' collection and obtaining the inserted ID
            carId = self.collection.insert_one(data).inserted_id
            # Printing a message indicating the successful insertion of data with the obtained ID
            print(f"Informação introduzida: {carId}")
        except Exception as e:
            # Handling exceptions and printing an error message if data insertion fails
            print(f"Error: {e}")

    # Method to fetch a specific car's data based on car ID
    def fetch_one(self, carId):
        # Querying the 'students' collection to find data for a specific student based on student ID
        data = self.collection.find_one({'_id': carId})
        return data

    # Method to fetch all cars data from the 'viaturas' collection
    def fetch_all(self):
        # Querying the 'viaturas' collection to find all data
        data = self.collection.find()
        return data

    # Method to update a specific car's data based on car ID
    def update(self, carId, car):
        # Creating a dictionary with updated car details
        data = {
            '_id': car.carId,
            'dataMat': car.dataMat,
            'marca': car.marca,
            'modelo': car.modelo,
            'categ': car.categ,
            'dataRev': car.dataRev,
            'email': car.email
        }
        # Updating the car data in the 'viaturas' collection
        self.collection.update_one({'_id': carId}, {"$set": data})

    # Method to delete a specific car's data based on car ID
    def delete(self, carId):
        # Deleting a car's data from the 'viaturas' collection based on car ID
        self.collection.delete_one({'_id': carId})
