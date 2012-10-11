hbox and vbox
=============

Hbox is a container which displays child elements horizontally. Vbox is a container which displays child elements vertically.

Parent classes
--------------
 - container

Members
-------

 - **padding** : Number of pixels to place between child elements. (Really should be called spacing)

Methods
-------

 - **add**(*self*, *elem*) : Adds a child element and moves it either vertically or horizontally according to box orientation.

 - **get_focus_grid**(*self*) : Returns a version of the focus grid which has Null spaces filled with long elements.