from .character import Character

class UserCharacter(Character):
    def __init__(self, name, profile_data, description):
        super().__init__(name, profile_data, description)
        # Initialize any additional properties specific to UserCharacter

    def submit_action(self, action):
        """
        User submits an action which kicks off the round-robin narration.

        Args:
            action (str): The user's action or decision to progress the story.
        """
        # Process the user's action. This could involve updating the story context,
        # adding to the character's own memory (if applicable), or directly interacting
        # with the narrative engine to trigger the round-robin sequence.
        
        # Example placeholder for triggering round-robin process
        self.trigger_round_robin(action)
    
    def trigger_round_robin(self, action):
        """
        Initiates the round-robin narration process among characters.

        Args:
            action (str): The user's action that triggers the round-robin.
        """
        # Logic to notify the narrative engine or controller to start
        # the round-robin process with other characters.
        pass

    # Include any other methods that need to be customized for the user character.
