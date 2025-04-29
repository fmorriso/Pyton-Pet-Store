import sys
from importlib.metadata import version

from orjson import orjson

from pet import Pet
from pet_store import PetStore


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_package_version(package_name: str) -> str:
    return version(package_name)


def main():
    cat = Pet('cat', 12.50)
    print(f'\nCat:\n{cat}')
    print(f'repr: {repr(cat)}')
    cat_json: str = orjson.dumps(cat, option = orjson.OPT_INDENT_2).decode('utf-8')
    print(f'orJSON: {cat_json}')

    dog = Pet('dog')
    print(f'\nDog:\n{dog}')
    dog.price = 9.99
    print(f'repr: {repr(dog)}')
    dog_json: str = orjson.dumps(dog, option = orjson.OPT_INDENT_2).decode('utf-8')
    print(f'orJSON: {dog_json}')

    rabbit = Pet('rabbit', 7.50)
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


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    print(f'orJSON version: {get_package_version("orjson")}')

    main()
