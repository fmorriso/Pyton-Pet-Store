from dataclasses import dataclass, field
from typing import Optional

from pet import Pet
from string_builder import StringBuilder


@dataclass
class PetStore:
    available_pets: Optional[list[Pet]] = field(default_factory = list)


    def __post_init__(self):
        if self.available_pets is None:
            self.available_pets = []


    def add_pet(self, *pets: Pet) -> None:
        pet: Pet
        for pet in pets:
            self.available_pets.append(pet)


    def __str__(self):
        s = StringBuilder('Pet Store:\n')

        for pet in self.available_pets:
            s.append(f'\t{pet.__str__()}')
            s.append('\n')

        return s.to_string()
