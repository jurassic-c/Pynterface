gui
===

The parent element for all other elements. The game loop should send all of its event to this object once every iteration. The gui object keeps track of the master focus grid and handles all of the navigation between elements by providing child elements with references to their neighbor elements according to the focus grid. The gui object also establishes a tabbing order for tabbing between objects in a fluid and intuitive manner.

Parent Classes
--------------

 - container

Members
-------

 - **focus_coords** : The coordinates on the focus grid of the currently focused element.

 - **keymap** : A reference to the keymap object.

 - **shift** : Boolean. Indicates whether or not the shift button on the keyboard is currently being pressed. Useful for key combinations.

 - **ctrl** : Boolean. Indicates whether ctrl key is currently being pressed.

 - **alt** : Booean. Indicates whether the alt key is currently being pressed.

 - **tabs** : A list of all the child elements, stored in their tab order.

 - **frame_time** : Time elapsed between previous game loop iteration, and the current one.

 - **mouse_pos** : Tuple containing the current (x, y) coordinates of the mouse cursor.

Methods
-------

 - **draw**(*self*, *events*, *frame_time*) : Draws the current state of itself and all of its child elements. Must be called once per game loop iteration.

 - **add**(*self*, *elem*) : Adds an element to its list of child elements. Upon adding an element it updates the focus grid and the tab order. It also recursively establishes itself as the parent gui object for all child elements and gives them focus grid coordinates as well as a tab order.

 - **get_element**(*self*, *elem_id*) : Returns an element of a specified id from a global list of gui elements.

 - **set_focus**(*self*, *focus_coords*) : Given a Tuple containing the focus grid coordinates of an element, this function blurs the previously focused item and updates the *focus_coords*. It's important to not that this function does not actually give the focus to the new object. Either the object has taken the focus on it's own (via the user clicking on it or something), or another navigational method (such as *tab_left()* has given the focus to the new element).

 - **tab**(*self*, *focus_coords*, *options={}*) : This function is called by *gui*'s navigational methods when a user tabs or arrows to a new element. This function gives the focus to the new element and calls *set_focus()*.

 - **tab_left**(*self*) : Finds the next child element in the tab sequence and gives it the focus.

 - **tab_right**(*self*) : Same as *tab_left()*, but finds previous tab element.

 - **item_left**(*self*) : Finds the element to the left of the currently focused element in the *focus_grid*, and gives it the focus.

 - **item_right**(*self*) : Same as *item_left()*, but goes to the right.

 - **item_up**(*self*) : Same as *item_left()*, but goes up.

 - **item_down**(*self*) : Same as *item_left()*, but goes down.

 - **press_focused**(*self*) : Simulates a user mouse press of the currently focused element.

 - **unpress_focused**(*self*) : Simulates the releasing of a user mouse press of the currently focused element.