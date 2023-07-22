# Author: Ashlyn Musgrave
# GitHub Username: ashlyn-musgrave
# Date: 7/21/2023
# Description: This program can add a pet, delete a pet, search for the owner of a pet,
# save data to a JSON file, load data from a JSON file, and gett a set of all pet
# species

import json

class DuplicateNameError(Exception):
    """Raises a system error when the name of a dog has already been entered"""
    pass
class NeighborhoodPets:
    """This class has methods for adding a pet, deleting a pet, searching for the
    owner of a pet, saving data to a JSON file, loading data from a JSON file, and
    getting a set of all pet species."""
    def __init__(self):
        self._petLibrary = {}

    def add_pet(self, name, species, owner):
        """This method takes as parameters the name of the pet, the species of the pet,
        and the name of the pet's owner"""
        if name not in self._petLibrary.keys():
            self._petLibrary[name] = {"name" : name, "species": species, "owner" : owner}
    try:
        add_pet()
    except DuplicateNameError:
        print("You have entered a duplicate name")
    def delete_pet(self, name):
        """This method takes as a parameter the name of the pet and deletes that pet"""
        if name in self._petLibrary.keys():
            self._petLibrary.pop(name)

    def get_owner(self, name):
        """This method takes as a parameter the name of the pet and returns the name of its owner."""
        if name in self._petLibrary.keys():
            return self._petLibrary[name]["owner"]
        else:
            return "owner not found"

    def save_as_json(self, file_name):
        """This method takes as a parameter the name of a file and saves it in JSON format
        with that name."""
        data = self._petLibrary
        with open(file_name, 'w') as outfile:
            json.dump(data, outfile)

    def read_json(self, file_name):
        """This method takes as a parameter the name of a file to read and loads that file"""
        with open(file_name) as json_file:
            self._petLibrary = json.load(json_file)

    def get_all_species(self):
        """This method takes no parameters and returns a Python set of the species of all pets."""
        petSpecies = {pet["species"] for pet in self._petLibrary.values()}
        return petSpecies

np = NeighborhoodPets()
try:
    np.add_pet("Fluffy", "gila monster", "Oksana")
    np.add_pet("Tiny", "stegasaurus", "Rachel")
    np.add_pet("Spot", "zebra", "Farrokh")
except DuplicateNameError:
    print('You tried to enter a pet with the same name as another pet.')
np.save_as_json("pets.json")
np.delete_pet("Tiny")
spot_owner = np.get_owner("Spot")
np.read_json("other_pets.json")  # where other_pets.json is a file it saved in some previous session
species_set = np.get_all_species()
