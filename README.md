Python Data Export:

A Python application demonstrating object-oriented programming and data serialization through JSON and XML formats.

Features:

- Defines custom classes for different types of records (`Usuario` and `Aluno`).
- Exports object data into JSON format using Python's `json` module.
- Exports object data into XML format using `xml.etree.ElementTree`.
- Uses polymorphism to support different export formats through a common interface.
- Converts object attributes into structured data.

Technologies:

- Python
- JSON
- XML
- Object-Oriented Programming (OOP)

Project Structure:

- `__main__.py`: Creates sample objects and executes the export operations.
- `classes.py`: Contains the data classes, export format classes, and the export function.

How to Run:

1. Make sure Python is installed.
2. Clone this repository.
3. Open the project directory.

python ____main____.py

The application will demonstrate exporting user records to JSON and student records to XML.
