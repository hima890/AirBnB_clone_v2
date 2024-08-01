![airbnb](hbnb_logo.png)
# AirBnB Clone - The Console

![airbnb_concept](consept_image.png)

# AirBnB Clone - The Console

The console is the first segment of the AirBnB project that will collectively cover fundamental concepts of higher-level programming. The goal of the AirBnB project is to eventually deploy our server as a simple copy of the AirBnB website (HBnB). A command interpreter is created in this segment to manage objects for the AirBnB (HBnB) website.

## Table of Contents
- [Functionalities](#functionalities)
- [Environment](#environment)
- [Installation](#installation)
- [File Descriptions](#file-descriptions)
- [Usage](#usage)
- [Examples of Use](#examples-of-use)
- [Bugs](#bugs)
- [Authors](#authors)
- [License](#license)

## Functionalities
This command interpreter provides the following functionalities:
- Create a new object (e.g., a new User or a new Place)
- Retrieve an object from a file, a database, etc.
- Perform operations on objects (count, compute stats, etc.)
- Update attributes of an object
- Destroy an object

## Environment
This project is interpreted/tested on Ubuntu 20.04 LTS using Python 3.8.10.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/alexaorrico/AirBnB_clone.git
   ```
2. Access the AirBnB directory:
   ```bash
   cd AirBnB_clone
   ```
3. Run `hbnb` (interactively):
   ```bash
   ./console.py
   ```
4. Run `hbnb` (non-interactively):
   ```bash
   echo "<command>" | ./console.py
   ```

## File Descriptions
- `console.py`: The console contains the entry point of the command interpreter. List of commands this console currently supports:
  - `EOF`: Exits the console
  - `quit`: Exits the console
  - `<emptyline>`: Overwrites the default empty line method and does nothing
  - `create`: Creates a new instance of BaseModel, saves it (to the JSON file), and prints the id
  - `destroy`: Deletes an instance based on the class name and id (saves the change into the JSON file)
  - `show`: Prints the string representation of an instance based on the class name and id
  - `all`: Prints all string representations of all instances based or not on the class name
  - `update`: Updates an instance based on the class name and id by adding or updating attribute (saves the change into the JSON file)

- `models/` directory contains classes used for this project:
  - `base_model.py`: The BaseModel class from which future classes will be derived
    - `__init__(self, *args, **kwargs)`: Initialization of the base model
    - `__str__(self)`: String representation of the BaseModel class
    - `save(self)`: Updates the attribute `updated_at` with the current datetime
    - `to_dict(self)`: Returns a dictionary containing all keys/values of the instance

  - Classes inherited from BaseModel:
    - `amenity.py`
    - `city.py`
    - `place.py`
    - `review.py`
    - `state.py`
    - `user.py`

- `models/engine` directory contains the File Storage class that handles JSON serialization and deserialization:
  - `file_storage.py`: Serializes instances to a JSON file & deserializes back to instances
    - `all(self)`: Returns the dictionary `__objects`
    - `new(self, obj)`: Sets in `__objects` the obj with key `.id`
    - `save(self)`: Serializes `__objects` to the JSON file (path: `__file_path`)
    - `reload(self)`: Deserializes the JSON file to `__objects`

- `tests/` directory contains all unit test cases for this project:
  - `test_models/test_base_model.py`: Contains the `TestBaseModel` and `TestBaseModelDocs` classes
    - `TestBaseModelDocs` class:
      - `setUpClass(cls)`: Set up for the doc tests
      - `test_pep8_conformance_base_model(self)`: Test that `models/base_model.py` conforms to PEP8
      - `test_pep8_conformance_test_base_model(self)`: Test that `tests/test_models/test_base_model.py` conforms to PEP8
      - `test_bm_module_docstring(self)`: Test for the `base_model.py` module docstring
      - `test_bm_class_docstring(self)`: Test for the `BaseModel` class docstring
      - `test_bm_func_docstrings(self)`: Test for the presence of docstrings in `BaseModel` methods
    - `TestBaseModel` class:
      - `test_is_base_model(self)`: Test that the instantiation of a `BaseModel` works
      - `test_created_at_instantiation(self)`: Test `created_at` is a public instance attribute of type `datetime`
      - `test_updated_at_instantiation(self)`: Test `updated_at` is a public instance attribute of type `datetime`
      - `test_diff_datetime_objs(self)`: Test that two `BaseModel` instances have different datetime objects

  - `test_models/test_amenity.py`: Contains the `TestAmenityDocs` class
    - `setUpClass(cls)`: Set up for the doc tests
    - `test_pep8_conformance_amenity(self)`: Test that `models/amenity.py` conforms to PEP8
    - `test_pep8_conformance_test_amenity(self)`: Test that `tests/test_models/test_amenity.py` conforms to PEP8
    - `test_amenity_module_docstring(self)`: Test for the `amenity.py` module docstring
    - `test_amenity_class_docstring(self)`: Test for the `Amenity` class docstring

  - `test_models/test_city.py`: Contains the `TestCityDocs` class
    - `setUpClass(cls)`: Set up for the doc tests
    - `test_pep8_conformance_city(self)`: Test that `models/city.py` conforms to PEP8
    - `test_pep8_conformance_test_city(self)`: Test that `tests/test_models/test_city.py` conforms to PEP8
    - `test_city_module_docstring(self)`: Test for the `city.py` module docstring
    - `test_city_class_docstring(self)`: Test for the `City` class docstring

  - `test_models/test_file_storage.py`: Contains the `TestFileStorageDocs` class
    - `setUpClass(cls)`: Set up for the doc tests
    - `test_pep8_conformance_file_storage(self)`: Test that `models/file_storage.py` conforms to PEP8
    - `test_pep8_conformance_test_file_storage(self)`: Test that `tests/test_models/test_file_storage.py` conforms to PEP8
    - `test_file_storage_module_docstring(self)`: Test for the `file_storage.py` module docstring
    - `test_file_storage_class_docstring(self)`: Test for the `FileStorage` class docstring

  - `test_models/test_place.py`: Contains the `TestPlaceDoc` class
    - `setUpClass(cls)`: Set up for the doc tests
    - `test_pep8_conformance_place(self)`: Test that `models/place.py` conforms to PEP8
    - `test_pep8_conformance_test_place(self)`: Test that `tests/test_models/test_place.py` conforms to PEP8
    - `test_place_module_docstring(self)`: Test for the `place.py` module docstring
    - `test_place_class_docstring(self)`: Test for the `Place` class docstring

  - `test_models/test_review.py`: Contains the `TestReviewDocs` class
    - `setUpClass(cls)`: Set up for the doc tests
    - `test_pep8_conformance_review(self)`: Test that `models/review.py` conforms to PEP8
    - `test_pep8_conformance_test_review(self)`: Test that `tests/test_models/test_review.py` conforms to PEP8
    - `test_review_module_docstring(self)`: Test for the `review.py` module docstring
    - `test_review_class_docstring(self)`: Test for the `Review` class docstring

  - `test_models/test_state.py`: Contains the `TestStateDocs` class
    - `setUpClass(cls)`: Set up for the doc tests
    - `test_pep8_conformance_state(self)`: Test that `models/state.py` conforms to PEP8
    - `test_pep8_conformance_test_state(self)`: Test that `tests/test_models/test_state.py` conforms to PEP8
    - `test_state_module_docstring(self)`: Test for the `state.py` module docstring
    - `test_state_class_docstring(self)`: Test for the `State` class docstring

  - `test_models/test_user.py`: Contains the `TestUserDocs` class
    - `setUpClass(cls)`: Set up for the doc tests
    - `test_pep8_conformance_user(self)`: Test that `models/user.py` conforms to PEP8
    - `test_pep8_conformance_test_user

(self)`: Test that `tests/test_models/test_user.py` conforms to PEP8
    - `test_user_module_docstring(self)`: Test for the `user.py` module docstring
    - `test_user_class_docstring(self)`: Test for the `User` class docstring

## Usage
The console works in both interactive and non-interactive modes.

### Examples of use
## Interactive Mode
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create User
(hbnb) show User 1234-1234-1234
(hbnb) destroy User 1234-1234-1234
(hbnb) all User
(hbnb) update

Bugs
No known bugs at this time.
```
### Bugs
No known bugs at this time.


### Authors
Ibrahim Hanafi
Ahmed basher

Second part of Airbnb: Ruba Salih

### License
Public Domain. No copy write protection.
