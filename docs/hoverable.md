hoverable
=========

This class is used to extend an element. It adds mouse over and mouse out functionality.

Members
-------

 - **enabled**: Boolean

 - **onMouseOver**: A reference to a callback, executed when a mouse over event for this element is fired. Callback should accept two arguments:
 - - *elem*: A reference to the element
 - - *event*: A reference to the event

 - **onMouseOut**: A reference to a callback, executed when a mouse out event for this element is fired. Callback should accept two arguments:
 - - *elem*: A reference to the element
 - - *event*: A reference to the event

Methods
-------

 - **draw**(*self*, *events*): Overrides draw method of element class to provide hover functionality. Be sure to call this draw method from the draw methods of your derived classes.