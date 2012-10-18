event_manager
=============

event_manager is a class for keeping track of which callbacks are bound to which events and executing them.

Members
-------

 - **event_bindings**: A python Dict object which holds the references to the callbacks according to their associated event.

 - **callback_ids**: A python Dict object that stores the location of each callback according to its id in *event_bindings*.

 - **max_id**: The current maximum id for the callbacks. It is incremented each time a new callback is bound with *bind()*.

Methods
-------

 - **bind**(*self*, *event*, *callback*): Binds a callback to an event. *event* should be an integer reference to an event. *callback* should be a reference to a function which accepts as its only argument a reference to the event which triggered the callback. **Returns**: *id*: integer reference to your bound callback. Use this to unbind it.

 - **unbind**(*self*, *callback_id*): Unbinds a previously bound callback, identified by it's callback_id.

 - **run**(*self*, *events*): Given a list of pygame events, this method will execute all bound callbacks for the events in the list.