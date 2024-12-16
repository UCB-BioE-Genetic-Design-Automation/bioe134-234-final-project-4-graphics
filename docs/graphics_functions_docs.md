**Basic Shape Classes: Textbox, Rectangle, Arrow, Polygon, Ellipse**

These classes allow the user to initialize, store, and draw the above shapes onto a canvas. A typical input is basic shape information, such as its coordinates, color, and string input (for the textbox)

**Advanced Shape Classes: CenteredText, TextInEllipse, DashedLine, Degradation Dots, TextInOval, LabeledArrow**

These classes, are identical to the basic shape classes, except in the fact that they require more specific inputs (depending on which advanced shape the user is working with)

**Canvas Class**

The Canvas class features a dictionary stored as an instance variable, and add, remove, and draw methods. The shapes are stored as _"shape_id": shape_ key, value pairs, and are drawn in the order they appear in the dictionary.
