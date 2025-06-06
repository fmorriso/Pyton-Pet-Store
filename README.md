# Python Pet Store

A pet store written in Python, not a pet store that currently sells pythons.

The *Pet* and *PetStore* classes use:

* __@dataclass__ - to simplify creation of *Pet* and *PetStore* objects.

## Tools Used

| Tool     |  Version |
|:---------|---------:|
| Python   |   3.13.3 |
| orjson   |  3.10.17 |
| pathlib  |    1.0.1 |
| pendulum |    3.1.0 |
| PyCharm  | 2025.1.0 |
| VSCode   |   1.99.0 |

## Change History

| Date       | Description                                                      |
|:-----------|:-----------------------------------------------------------------|
| 2025-04-23 | Initial creation                                                 |
| 2025-04-24 | Differentiate between str() and repr(), add to_json() capability |
| 2025-04-28 | Modify add_pet() to allow multiple pet objects                   |
| 2025-04-29 | replace dataclasses_json with orjson, add pet birthday           |
| 2025-04-30 | add ability to read/write the pet store from/to the file system  |

## References

* [Master Python dataclasses [In-Depth Tutorial]](https://www.golinuxcloud.com/python-dataclasses/)
* [Understanding and Using Data Classes in Python](https://datagy.io/python-data-classes/)
* [Python Data Class: A Better Way to Store Data](https://python.land/python-data-classes)
* [Python Dataclass](https://docs.python.org/3/library/dataclasses.html)
* [Understanding Python Dataclasses](https://www.geeksforgeeks.org/understanding-python-dataclasses/)
* [Python Data Classes (With Examples)](https://pyseek.com/2025/03/python-data-classes/#google_vignette)
* [orjson documentation](https://github.com/ijl/orjson)
* [pendulum](https://pendulum.eustace.io/docs/)