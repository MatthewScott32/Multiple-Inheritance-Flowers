class Arrangement:
    def __init__(self, name):
        self.name = name
        self.flowers = list()

    # def enhance(self, flowers):
    #     self.flowers.append(flowers)

    def enhance(self, flowers):
        try:
            if flowers.stem == "Long":
                self.flowers.append(flowers)
                print(f'The {flowers} is perfect for {self.name} arrangements.')

            else:
                print(f'{flowers} isn\'t good for this. Don\'t try to put it in the {self.name} arrangement')
        except AttributeError as ex:
            print(f'{flowers} isn\'t romantic, don\'t try to put it in the {self.name} arrangement')