import datetime as dt
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Tuple

from string_builder import StringBuilder


@dataclass
class Pet:
    type: str
    price: Optional[float] = 0
    birthday: Optional[dt.date] = datetime.now(dt.timezone.utc).date()


    def age(self) -> Optional[Tuple[int, str]]:
        """return a tuple containing the whole number of years or months followed by a string of either months or
        years"""
        if self.birthday is None:
            return None
        today = datetime.now(dt.timezone.utc).date()
        birthdate = self.birthday

        # Calculate age in years
        age_years = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age_years -= 1

        # If age is less than 1 year, calculate age in months
        if age_years < 1:
            # Calculate age in months
            age_months = (today.year - birthdate.year) * 12 + today.month - birthdate.month
            if today.day < birthdate.day:
                age_months -= 1
            return age_months, 'months'

        # Otherwise, return age in years
        return age_years, 'years'


    def __str__(self):
        s = StringBuilder()

        s.append('Type: ')
        s.append(self.type)

        s.append(', Price: ')
        s.append(f'${self.price:.2f}')

        s.append(', Birthday: ')
        s.append(f'{self.birthday:%Y-%m-%d}')

        s.append(', Age: ')
        s.append(f'{self.age()[0]} {self.age()[1]}')

        return s.to_string()
