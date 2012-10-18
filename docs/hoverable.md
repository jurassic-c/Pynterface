hoverable
=========

This class is used to extend an element. It adds mouse over and mouse out functionality.

Members
-------

 - **hover_enabled**: Boolean

Methods
-------

 - **set_gui**(*self*, *gui*): Sets up the bindings for mouse events. Must be called by set_gui method of any derived classes.

 - **draw**(*self*, *events*): Overrides draw method of element class to provide hover functionality. Be sure to call this draw method from the draw methods of your derived classes.

Event
-----
 - MOUSEOVER

 - MOUSEOUT