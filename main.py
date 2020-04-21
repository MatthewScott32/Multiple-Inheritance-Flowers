from flowers import Alstroemeria
from flowers import BabysBreath
from flowers import Daisy
from arrangements import Arrangement

valentine = Arrangement("Valentine")
mother = Arrangement("Mother's Day")

alstro = Alstroemeria("Alstroemeria", "Long", "Green")
print(alstro.name)
alstro.bloom(10)

valentine.enhance(alstro)

baby = BabysBreath("Baby's Breath", "Short", "Blue")
print(baby.name)
baby.bloom(5)

valentine.enhance(baby)

daisy = Daisy("Daisy", "Medium", "Yellow")
print(daisy.name)
daisy.bloom(7)

valentine.enhance(daisy)

for flower in valentine.flowers:
    print(flower)

mother.enhance(daisy)
mother.enhance(alstro)

for flower in mother.flowers:
    print(flower)