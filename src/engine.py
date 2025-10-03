import curses

from typing import Set, Iterable, Any
from actions import EscapeAction, MovementAction
from entity import Entity
from input_handler import EventHandler

class Engine: 
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, player: Entity, stdscr):
        self.entities = entities
        self.event_handler = event_handler
        self.player = player
        self.stdscr = stdscr
        
    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)        # handle event
        
            if action is None:
                continue
            
            if isinstance(action, MovementAction):
                # update player position with bounds checking
                new_x = self.player.x + action.dx
                new_y = self.player.y + action.dy
                
                # keept player within screen bounds
                if 0 <= new_x < screen_width and 0 <= new_y < screen_height:
                    self.player.move(dx = action.dx, dy = action.dy)
                
            elif isinstance(action, EscapeAction):
                break
    
    def render(self):
        self.stdscr.clear()
        
        for entity in self.entities:
            self.stdscr.addstr(entity.y, entity.x, entity.char, entity.color)
            
        self.stdscr.refresh()