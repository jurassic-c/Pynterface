element
=======

element serves as a base class for almost all other classes in Pynterface. It handles positioning, focusing and many other aspects UI. Custom UI elements should derive from this class.

Members
-------

 - **id**: The ID of the element with respect to it's parent gui object.

 - **rect**: Pygame Rect object for storing geometry of element.

 - **parent**: A reference to the element's parent element. The only element with no parent should be a gui object.

 - **local_x**: The element's x position relative to it's parent

 - **local_y**: The element's y position relative to it's parent

 - **options**: A python Dict object used to store options for the element's various states.

 - **focus_grid** : A local focus grid. In the case of a simple element, the focus grid will be a 1x1 grid containing only a reference to the element. In the case of something more complex like an hbox or a vbox, this will likely be a grid containing the relative positions of all child elements.

 - **focus_coords**: The coordinates of the element on the Focus Grid.

 - **tab_order**: The element's tab order. This is set automatically. Currently, overriding it will do nothing.

 - **onFocus**: A callback which is called when the element receives focus. This callback should accept two arguments:
 - - *elem*: This will be a reference to the element itself.
 - - *event*: A reference to the event which triggered the calling of the callback.

 - **onBlur**: A callback which is called when the element loses focus. This callback should accept two arguments:
 - - *elem*: This will be a reference to the element itself.
 - - *event*: A reference to the event which triggered the calling of the callback.

Methods
-------

 - **draw**(*self*, *events*): called by it's parent element when it's time to draw all of the UI elements. This function is designed to be overridden with your own functionality.

 - **set_gui**(*self*, *gui*): Called automatically by it's parent element, it sets the gui object.

 - **move**(*self*, *x*, *y*): Moves the element to position (*x*, *y*) relative to it's parent's position.

 - **resize**(*self*, *w*, *h*): Resizes element to *w* x *h*.

 - **focus**(*self*, *options={}*): Gives focus to element. If *onFocus* is set, it will be executed.

 - **blur**(*self*): Removes focus from element. If *onBlur* is set, it will be executed.

 - **element_right**(*self*): Returns the element to the right of this element, if any. None if there isn't one.

 - **element_left**(*self*): Returns the element to the left of this element, if any. None if there isn't one.

 - **element_above**(*self*): Returns the element above this element, if any. None if there isn't one.

 - **element_below**(*self*): Returns the element below this element, if any. None if there isn't one.