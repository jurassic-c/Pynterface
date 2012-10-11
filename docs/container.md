container
=========

An element which contains other elements.

Parent Classes
--------------
 - element

Members
-------

 - **child_elements** : A list of child element objects

 - **child_ids** : A Dict containing a map of child element ids to their corresponding index in *child_elements*

 - **focus_id** : Should the container become focused for some reason, it is likely that one of the child elements will be the actual target of the focus. This *focus_id* is the index of this object in *child_elements*

Methods
-------

 - **draw**(*self*, *events*) : An overridable method which is called by its parent object at draw time. It also automatically calls *draw()* for all of its child elements.

 - **add**(*self*, *elem*) : Adds a given element to the list of child elements.

 - **move**(*self*, *x*, *y*) : Moves the element to (*x*, *y*) relative to it's parent element, also moves all child elements accordingly.

 - **first_child**(*self*) : Returns the first child in the list of child elements

 - **last_child**(*self*) : Returns the last child in the list of elements.