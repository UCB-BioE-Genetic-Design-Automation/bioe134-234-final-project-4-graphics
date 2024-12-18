# BioE 134 Final Project README

This document outlines the structure, functionality, and collaborative development process for the C9 Graphics Project, which is designed to generate and manipulate diagrams programmatically. The project consists of three key components: Library of Methods, C9 Wrappers, and PyTests, all implemented in Python. Each team member has contributed equally to their development and integration.

## 1. Library of Methods
- The library provides a set of reusable, class-bound functions for generating and manipulating graphical elements such as rectangles, textboxes, arrows, polygons, and ellipses. These classes and methods simplify diagram creation through intuitive, parameterized functions.
**Key Features**
- Inheritance Structure: Built around a superclass (Element) to promote modularity and maintainability.
- Shape Classes: Specialized subclasses like TextBox, Rectangle, Arrow, and Ellipse allow users to create complex diagrams by combining simple elements.
- Advanced Functionalities: Includes composite elements like TextInOval and LabeledArrow for embedding text inside shapes or along directional arrows.
- Customizable Attributes: Color, coordinates, size, and other visual properties can be customized for precise diagrammatic representation.
- 
- **Example**
- python
- Copy code
- rectangle = Rectangle(width=100, height=50, coordinates=(10, 10), color=(255, 0, 0))
- rectangle.draw(draw_obj)
- 
- These methods are critical for transforming abstract design specifications into tangible graphical outputs.

## 2. C9 Wrappers
The C9 Wrappers encapsulate the methods in JSON-based schemas, allowing integration with language models like GPT for automated diagram generation. This design facilitates high-level querying and instruction sets to programmatically interact with the library.
Key Features
Wrapper Functions: Abstract away the complexities of direct method calls, enabling intuitive usage via simple JSON commands.
Schema Definition: Each function (e.g., Rectangle.draw) is represented with its parameters, inputs, and outputs in the JSON schema.
Interoperability: Connects diagramming logic with the LLM's natural language processing capabilities for seamless user interaction.
Example JSON Command
json
Copy code
{
  "id": "org.c9.function.Rectangle.__init__",
  "name": "Rectangle.__init__",
  "inputs": {
    "width": 100,
    "height": 50,
    "color": [255, 0, 0],
    "coordinates": [10, 10]
  }
}

These wrappers ensure that non-technical users can generate diagrams by interacting with the model through natural language.

## 3. PyTests
PyTests verify the correctness and robustness of the implemented methods and wrappers, ensuring consistent outputs and reliability of the system.
Key Features
Comprehensive Test Cases: Covers edge cases for all major functionalities, including invalid inputs and boundary conditions.
Automation: Provides continuous testing to validate updates or extensions of the library.
Integration Testing: Tests the end-to-end functionality of JSON wrapper commands in conjunction with the graphics library.
Example Test
python
Copy code
def test_rectangle_initialization():
    rect = Rectangle(width=100, height=50, coordinates=(0, 0), color=(255, 0, 0))
    assert rect.width == 100
    assert rect.color == (255, 0, 0)

PyTests guarantee reliability in generating diagrams and executing user commands, contributing to a polished and bug-free product.

## Collaboration and Contributions
All team members equally participated in designing, implementing, and testing the three core components:
Library Development: Jointly structured the inheritance model and implemented individual shape classes.
Wrapper Design: Collaboratively defined the JSON schema to ensure compatibility with natural language queries.
Testing Framework: Developed and executed test cases, ensuring robust functionality and integration.
Workflow
Weekly code reviews and pair programming sessions facilitated collaboration.
Collective brainstorming sessions shaped the design principles for each component.
Responsibilities rotated across library, wrappers, and PyTest development to distribute learning and contributions equitably.

