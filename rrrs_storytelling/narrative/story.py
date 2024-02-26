class Story:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.scenes = []  # List to store Scene objects
        self.characters = []  # List to store Character objects

    def add_scene(self, scene):
        """Adds a Scene object to the story."""
        self.scenes.append(scene)

    def add_character(self, character):
        """Adds a Character object to the story."""
        self.characters.append(character)

    def get_current_scene(self):
        """Returns the current scene, assuming the last one in the list."""
        return self.scenes[-1] if self.scenes else None

    def advance_scene(self, new_scene):
        """Advances the story to the next scene."""
        self.add_scene(new_scene)