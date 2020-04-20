from flowers import Alstroemeria
from arrangements import Arrangement

alstro = Alstroemeria("Alstroemeria", "Long", "Green")
print(alstro.name)
print(alstro.petals)
alstro.bloom(10)
print(alstro.petals)

valentine = Arrangement("Valentine")
valentine.enhance(alstro)

for flower in valentine.flowers:
    print(flower)