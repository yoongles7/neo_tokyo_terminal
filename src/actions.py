class Action:
    pass

class EscapeAction(Action):
    pass

class MovementAction(Action):
    def __init__(self, dx, dy):
        super().__init__()
        
        self.dx = dx
        self.dy = dy
    
        