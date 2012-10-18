Events
======

Pynterface has several pygame user events defined. They can be used by importing *Pynterface.events*. All events will include the following information:
 - **elem**: A reference to the clicked element
 - **pos**: A tuple containing the mouse position coordinates

Event Definitions
-----------------

 - FOCUS - Occurs when any element receives focus.

 - BLUR - Occurs when any element loses focus.

 - CLICK - Occurs when a clickable element has been clicked.

 - DOUBLECLICK - Occurs when a clickable element has been double clicked.

 - MOUSEOVER - Occurs when a hoverable element has been hovered over by the mouse cursor.

 - MOUSEOUT - Occurs when a hoverable element no longer has the mouse cursor over it.

 - DWELLCLICK - **NOT YET IMPLEMENTED**. Occurs when a clickable element has been dwell clicked.

 - DRAG - **NOT YET IMPLEMENTED**. Occurs when a draggable element is being dragged.