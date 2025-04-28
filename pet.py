from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json

from string_builder import StringBuilder


@dataclass_json
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
