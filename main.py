import sys
from datetime import date
from importlib.metadata import version
from pathlib import Path

import pendulum
from orjson import orjson

from pet import Pet
from pet_store import PetStore

PET_STORE_FILE = 'pet_store.json'


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_package_version(package_name: str) -> str:
    return version(package_name)


def to_plain_date(p_date: pendulum.Date) -> date:
    return date(p_date.year, p_date.month, p_date.day)


def save_pet_store(store: PetStore) -> None:
    pet_store_path = Path(PET_STORE_FILE)
    with open(pet_store_path, 'w') as f:
        pet_store_json = orjson.dumps(store, option = orjson.OPT_INDENT_2).decode('utf-8')
        f.write(pet_store_json)


def main():
    cat = Pet('cat', 12.50)
    cat.birthday = to_plain_date(pendulum.now('UTC').subtract(years = 9).date())
    print(f'\nCat:\n{cat}')
    print(f'repr: {repr(cat)}')
    cat_json: str = orjson.dumps(cat, option = orjson.OPT_INDENT_2).decode('utf-8')
    print(f'orJSON: {cat_json}')

    dog = Pet('dog')
    dog.price = 9.99
    dog.birthday = to_plain_date(pendulum.now('UTC').subtract(years = 2, months = 3).date())
    print(f'\nDog:\n{dog}')
    print(f'repr: {repr(dog)}')
    dog_json: str = orjson.dumps(dog, option = orjson.OPT_INDENT_2).decode('utf-8')
    print(f'orJSON: {dog_json}')

    rabbit = Pet('rabbit', 7.50, date.fromisoformat('2025-01-29'))
    print(f'\nRabbit:\n{rabbit}')
    print(f'repr: {repr(rabbit)}')
    rabbit_json: str = orjson.dumps(rabbit, option = orjson.OPT_INDENT_2).decode('utf-8')
    print(f'orJSON: {rabbit_json}')

    pet_store = PetStore()
    pet_store.add_pet(cat, dog)
    pet_store.add_pet(rabbit)

    print(f'\n{pet_store}')
    pet_store_json: str = orjson.dumps(pet_store, option = orjson.OPT_INDENT_2).decode('utf-8')
    print(f'orJSON: {pet_store_json}')

    save_pet_store(pet_store)


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    print(f'pendulum version: {get_package_version("pendulum")}')
    print(f'orJSON version: {get_package_version("orjson")}')
    print(f'pathlib version: {get_package_version("pathlib")}')
    print(f'The current date/time UTC is {pendulum.now().in_tz("UTC")}')

    main()
