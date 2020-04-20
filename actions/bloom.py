class IBloom:

    def __init__(self):
        self.petals = 0

    def bloom(self, petals):
        self.petals = petals
        print(f"The flower bloomed {self.petals} petals and is beautiful.")