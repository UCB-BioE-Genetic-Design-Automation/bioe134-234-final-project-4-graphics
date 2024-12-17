pip install pytest

import pytest
from PIL import Image, ImageDraw
from copy_of_bioe_134_graphics_test_book import (
    TextBox, Rectangle, Arrow, Polygon, Ellipse, 
    CenteredText, TextInEllipse, TextInBox, DashedLine, 
    DegradationDots, TextInOval, LabeledArrow
)

@pytest.fixture
def image_draw():
    # Provides a blank image and its draw object for testing
    img = Image.new("RGB", (200, 200), "white")
    draw = ImageDraw.Draw(img)
    return draw

def test_textbox(image_draw):
    element = TextBox("Hello", (10, 10), (0, 0, 0))
    element.draw(image_draw)

def test_rectangle(image_draw):
    element = Rectangle(50, 30, (20, 20), (255, 0, 0))
    element.draw(image_draw)

def test_arrow(image_draw):
    element = Arrow((10, 10), (100, 100), (0, 255, 0))
    element.draw(image_draw)

def test_polygon(image_draw):
    element = Polygon([(10, 10), (50, 10), (30, 40)], (0, 0, 255))
    element.draw(image_draw)

def test_ellipse(image_draw):
    element = Ellipse(50, 30, (60, 60), (128, 0, 128))
    element.draw(image_draw)

def test_centered_text(image_draw):
    element = CenteredText("Centered", (100, 100), (0, 0, 0), 12)
    element.draw(image_draw)

def test_text_in_ellipse(image_draw):
    element = TextInEllipse("Inside", 50, 30, (40, 40), (200, 200, 200), (0, 0, 0))
    element.draw(image_draw)

def test_text_in_box(image_draw):
    element = TextInBox("Boxed", 60, 40, (10, 10), (0, 255, 255), (0, 0, 0))
    element.draw(image_draw)

def test_dashed_line(image_draw):
    element = DashedLine((10, 10), (100, 10), (0, 0, 0), [5, 2], 2)
    element.draw(image_draw)

def test_degradation_dots(image_draw):
    element = DegradationDots([(30, 30), (40, 40), (50, 50)], 5, (255, 0, 0))
    element.draw(image_draw)

def test_text_in_oval(image_draw):
    element = TextInOval("Oval Text", 80, 50, (60, 60), (100, 100, 200), (0, 0, 0))
    element.draw(image_draw)

def test_labeled_arrow(image_draw):
    element = LabeledArrow((10, 10), (100, 10), (0, 0, 0), 3, "Arrow Label", (5, -10), (0, 0, 255))
    element.draw(image_draw)


