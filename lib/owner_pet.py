class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Initialize an empty list to hold pets

    def pets(self):
        """Returns the list of pets owned by this owner."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner and sets the pet's owner."""
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet class")
        self._pets.append(pet)  # Add the pet to the owner's list
        pet._owner = self  # Set the pet's owner without using the setter

    def get_sorted_pets(self):
        """Returns a sorted list of pets by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Class variable to hold all pet instances

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("pet_type must be one of " + ", ".join(Pet.PET_TYPES))

        self.name = name
        self.pet_type = pet_type
        self._owner = None  # Initialize the owner as None
        Pet.all.append(self)  # Add this pet to the list of all pets

        if owner:
            self.owner = owner  # Set the owner if provided

    @property
    def owner(self):
        """Returns the pet's owner."""
        return self._owner

    @owner.setter
    def owner(self, value):
        """Sets the pet's owner, ensuring it's an instance of Owner."""
        if value is not None and not isinstance(value, Owner):
            raise Exception("owner must be an instance of Owner class")
        self._owner = value  # Set the owner
        if value:  # If owner is set, add this pet to the owner's pets
            value.add_pet(self)

