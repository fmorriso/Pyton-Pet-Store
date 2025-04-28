import sys
from importlib.metadata import version

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
    print(cat.to_json())

    dog = Pet('dog')
    print(f'\nDog:\n{dog}')
    dog.price = 9.99
    print(f'repr: {repr(dog)}')
    print(dog.to_json())

    rabbit = Pet('rabbit', 7.50)
    print(f'\nRabbit:\n{rabbit}')
    print(f'repr: {repr(rabbit)}')
    print(rabbit.to_json())

    pet_store = PetStore()
    pet_store.add_pet(cat, dog)
    pet_store.add_pet(rabbit)

    print(f'\n{pet_store}')
    print(pet_store.to_json())


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    print(f'PySide6 version: {get_package_version("pyside6")}')
    print(f'PySide6-Addons version: {get_package_version("pyside6-addons")}')
    print(f'PyAutoGUI version: {get_package_version("pyautogui")}')
    main()
