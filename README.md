
# BioE 134 Final Project Submission

## Project Overview

This project provides a graphics program to allow users to generate diagrams of their choosing: 

It includes:
1. **Methods**: Class-bound functions to help the LLM generate the diagram
2. **C9 Wrappers**: Allows the LLM to understand the methods and use them efficiently
3. **PyTests**: Tests to allow the user to see if their instructions are working correctly with the LLM

This program is implemented in **Python**.

---

## Scope of Work

All three of us (Hari, James, Joseph) worked on all parts of this project.

---

## Function Descriptions

### 1. Shape Classes (`Rectangle, Ellipse, TextBox, etc.`)

- **Shape Classes Description**: These classes all have "__init__" and "draw" methods. They take in various inputs such as ("start_coordinate", "end_coordinate", "color", etc.) to store as instance variables in the "Canvas" class, described below.
- **Canvas Class Description**: The "Canvas" class stores all the shapes in a dictionary (to control the order they appear on the screen as well), and features a "draw", "add", and "remove" methods.

## Testing

We tested the program with ChatGPT, with the C9 wrappers and methods. The tests are included in the repository.

The tests include a set of instructions, the desired generated image, and the actual image.

---

## Usage Instructions

Create a set of instructions, pass those instructions into GPT, along with the methods and C9 wrappers, and ask it to run your instructions.

---

## Conclusion

This program allows for anyone to give a set of instructions to a LLM such as ChatGPT, along with our methods and C9 wrappers, in order to generate a diagram of their choosing.
