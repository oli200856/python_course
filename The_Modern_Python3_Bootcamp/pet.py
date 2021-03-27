class Pet:
    allowed = ("cat", "dog", "crocodile", "tiger", "fish", "rat", "pig")
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet.")
        self.name = name
        self.species = species
    def set_species(self,species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet.")
        self.species = species

cat = Pet("Noah", "cat")
dog = Pet("Hazel", "dog ")