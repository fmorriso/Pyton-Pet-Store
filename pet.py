from dataclasses import dataclass
from typing import Optional

from string_builder import StringBuilder


@dataclass
class Pet:
    type: str
    price: Optional[float] = 0

    def __str__(self):
        s = StringBuilder()

        s.append('Type: ')
        s.append(self.type)

        s.append(', Price: ')
        s.append(f'${self.price:.2f}')

        return s.to_string()

    def __repr__(self):
        s = StringBuilder('Pet{')

        s.append('Name: ')
        s.append(self.type)
        s.append(', Price: ')
        s.append(f'{self.price:.2f}')

        s.append('}')
        return s.to_string()
