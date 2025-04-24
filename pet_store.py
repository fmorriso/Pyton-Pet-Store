from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import dataclass_json

from pet import Pet
from string_builder import StringBuilder


@dataclass_json
@dataclass
class PetStore:
    available_pets: Optional[list[Pet]] = field(default_factory = list)


    def __post_init__(self):
        if self.available_pets is None:
            self.available_pets = []


    def add_pet(self, pet: Pet) -> None:
        self.available_pets.append(pet)


    def __str__(self):
        s = StringBuilder('Pet Store:\n')

        for pet in self.available_pets:
            s.append(f'\t{pet.__str__()}')
            s.append('\n')

        return s.to_string()


    def __repr__(self):
        s = StringBuilder('Pet Store:{')

        for pet in self.available_pets:
            s.append(pet.__str__())
            s.append(', ')

        s.append('}')
        return s.to_string()
