from typing import Optional

from actions import Action, EscapeAction, MovementAction

class EventHandler:
    def dispatch(self, key: int) -> Optional[Action]:
        action: Optional[Action] = None
        
        if key == "w":
            action = MovementAction(dx = 0, dy = -1)
        elif key == "s":
            action = MovementAction(dx = 0, dy = 1)
        elif key == "a":
            action = MovementAction(dx = -1, dy = 0)
        elif key == "d":
            action = MovementAction(dx = 1, dy = 0)
        
        elif key == "q":
            action = EscapeAction()
            
                
        return action
    