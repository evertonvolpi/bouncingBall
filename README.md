# bouncingBall
Created in a Raspberry Pi equiped with a GFX Hat.</br>
## Library
Functions:
**displayObject**</br>
Takes *object* and start coordinates *x* and *y* as arguments and displays object at the GFX Hat's screen.</br>
**eraseObject**</br>
Takes *object* and start coordinates *x* and *y* as arguments and erases object at the GFX Hat's screen.</br>
**moveObject**</br>
Takes *obj*, start coordinates *x* and *y* and speed *vx* and *vy* as arguments and displays the object at start coordinates, then erases the object and continuosly displays it in the new positions accordingly with the speed.</br>
**checkCollision**</br>
Checks if the object collides with the GFX Hat screen's limit within the next movement in *moveObject*.</br>
**bouncingBall**</br>
Takes *obj*, start coordinates *x* and *y* and speed *vx* and *vy* as arguments and displays the object in a continuing bouncing movement on the GFX Hta's screen.</br>
## Test Driver:
Tests the functions of the library.
