import curses

class CyberpunkTileset:
    def __init__(self):
        self.tiles = {
            # TERRAIN & ARCHITECTURE
            'neon_street': '░',      # Light pattern
            'dark_street': '▓',      # Dark pattern  
            'building_wall': '█',    # Solid wall
            'window': '▤',           # Grid window
            'reinforced_wall': '▩',  # Heavy wall
            'corporate_logo': '◈',   # Diamond logo
            'tech_pattern': '▞',     # Technical pattern
            
            # TECHNOLOGY & HACKING
            'server_rack': '≡',      # Server equipment
            'circuit': 'Φ',          # Circuit board
            'data_stream': '≈',      # Flowing data
            'binary': '01',          # Binary code
            'hack_effect': '⋆',      # Hacking sparkles
            'energy_core': '◎',      # Power source
            'wireless': '⌔',         # Wireless signal
            
            # CORPORATE & URBAN
            'corp_tower': '▐',       # Skyscraper
            'ad_sign': '◊',          # Advertisement
            'surveillance': '⌖',     # Camera/surveillance
            'security_gate': '╬',     # Checkpoint
            'elevator': '⤓',         # Elevator shaft
            'ventilation': '⌀',      # Vent/duct
            
            # CHARACTERS & ENTITIES
            'player_hacker': 'Ѫ',    # Hacker character
            'player_corp': '♕',      # Corporate character
            'player_runner': '⚡',    # Street runner
            'enemy_guard': '⚔',      # Security guard
            'enemy_drone': '✈',      # Surveillance drone
            'enemy_cyborg': '♼',     # Enhanced human
            'boss_corporate': '♛',   # Corporate executive
            'boss_ai': 'Ψ',          # Rogue AI
            
            # ITEMS & EQUIPMENT
            'credits': '¢',          # Money/credits
            'data_chip': '▯',        # Storage device
            'weapon_energy': '⌇',    # Energy weapon
            'weapon_kinetic': '➳',   # Projectile weapon
            'cyberware': 'ⴲ',        # Cybernetic implant
            'health_pack': '✚',      # Medical supplies
            'backdoor': '⍆',         # Access point
            
            # VEHICLES & TRANSPORT
            'hover_car': '⧈',        # Flying vehicle
            'motorcycle': 'ᗐ',       # Ground vehicle
            'transport': '▭',        # Large transport
            'escape_pod': '○',       # Emergency vehicle
            
            # EFFECTS & ATMOSPHERE
            'neon_glow': '✧',        # Neon light effect
            'rain': '⸰',             # Acid rain
            'smog': '∼',             # Pollution
            'electric_arc': '⚡',     # Electrical effect
            'explosion': '✴',        # Explosion effect
            'shield': '⌽',           # Energy shield
        }
    
    def setup_colors(self):
        curses.start_color()
        # Cyberpunk color palette
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)      # Neon blue
        curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)   # Pink/purple
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)     # Matrix green
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)    # Warning yellow
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)       # Alert red
        curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)     # Neutral white
        curses.init_pair(7, curses.COLOR_BLUE, curses.COLOR_BLACK)      // Corporate blue
        curses.init_pair(8, 8, curses.COLOR_BLACK)  # Gray (if terminal supports 8 colors)