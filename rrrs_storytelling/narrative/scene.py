class Scene:
    def __init__(self, sceneid, scene_text):
        self.sceneid = sceneid
        self.scene_text = scene_text
        self.characters = []  # Array of character objects in the scene

    def add_character(self, character):
        """Adds a character to the scene."""
        self.characters.append(character)

    def get_character_descriptions(self):
        """Returns a quick description of all characters in the scene."""
        descriptions = [char.quick_description() for char in self.characters]
        return "\n".join(descriptions)

    def format_for_llm(self):
        """Formats scene information specifically for generating prompts for the LLM."""
        participants = self.get_character_descriptions()
        formatted_prompt = (
            f"Scene: {self.sceneid}\n"
            f"Participants: {participants}\n\n"
            f"{self.scene_text}"
        )
        return formatted_prompt
