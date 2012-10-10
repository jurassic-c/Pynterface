clickable
=========

This class is used to extend an element. It adds click and double click functionality.

Members
-------

 - **enabled**: Boolean

 - **onClick**: A reference to a callback, executed when a click event for this element is fired. Callback should accept two arguments:
 - - *elem*: A reference to the element
 - - *event*: A reference to the event

 - **onDoubleClick**: A reference to a callback, executed when a double click for this element event is fired. Callback should accept two arguments:
 - - *elem*: A reference to the element
 - - *event*: A reference to the event

 - **onMouseDown**: A reference to a callback, executed when a mousedown event for this element is fired. Callback should accept two arguments:
 - - *elem*: A reference to the element
 - - *event*: A reference to the event

 - **onMouseUp**: A reference to a callback, executed when a mouseup event for this element is fired. Callback should accept two arguments:
 - - *elem*: A reference to the element
 - - *event*: A reference to the event

 - **double_click_timeout**: Maximum number of milliseconds between two mousedown events for them to count as a double click. **Default**: 200

Methods
-------

 - **draw**(*self*, *events*): Called by the element's parent element at draw time. Overrides draw method of element class to handle click events. Be sure to call this from the draw method of your derived class.

 - **double_click**(*self*): Executes double click functionality.

 - **press**(*self*): Simulates a mouse press on the element. Will execute *onMouseDown* callback.

 - **unpress**(*self*, *click=0*): Simulates a release of the mouse button over the element. *click* indicates the type of click event to fire.
 - - *0* : No click. This will happen in the case of a button, for instance, over which the user has clicked, but the release of the mouse button occurs outside of the button geometry.
 - - *1* : Single click
 - - *2* : Double click