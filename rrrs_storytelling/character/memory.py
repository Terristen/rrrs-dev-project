from datetime import datetime

class Memory:
    def __init__(self, scene, memory):
        self.scene = scene  # This now expects a Scene object instead of a string
        self.memory = memory
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Adjustments to other methods as necessary to accommodate the Scene object

