from openai_api import APIInteraction
from .memory import Memory
from utils import debug_print


class Character:
    # Constants for LLM instructions as multi-line strings
    REPLY_INSTRUCTION = """
    How do you feel about what's happening now?
    What do you want to happen next?
    What do you fear?
    What do you need or want?
    Format your thoughts and feelings regarding these questions as a list delineated by \n.
    """

    SUMMARY_INSTRUCTION = """
    Think about the events of this scene thus far and provide a list of things that you will remember, or that have or will make an impact on your character.
    """

    def __init__(self, name, profile_data, description, api_interaction=None):
        self.name = name
        self.profile_data = profile_data
        self.description = description
        self.short_term_memory = []  # List to store order-sensitive short-term memory statements
        self.long_term_memory = []  # List to store long-term memory statements
        self.current_scene = ""
        self.api_interaction = api_interaction or APIInteraction()
        
    def quick_description(self):
        """Returns a quick description of the character."""
        return f"{self.name}: {self.description}"

    def add_memory(self, memory):
        """Adds a Memory instance to the character's short-term memory.

        Args:
            memory (Memory): The memory to add.
        """
        if isinstance(memory, Memory):
            self.short_term_memory.append(memory)
        else:
            print("The provided memory is not an instance of Memory class.")

    
    def update_short_term_memory(self, memory_statement, scene):
        memories = memory_statement.split('\n')
        for memory in memories:
            self.short_term_memory.append(Memory(scene, memory))
        

    def summarize_memory(self, scene):
        """
        Summarizes the character's experiences in a given scene, storing the summary in long-term memory,
        and clears the short-term memories associated with that scene.

        Args:
            scene (Scene): The scene to be summarized.
        """
        # Use the scene's format_for_llm function to include detailed scene information in the prompt
        scene_context = scene.format_for_llm()  # Assuming Scene class has this method
        # Append the SUMMARY_INSTRUCTION and specific memories related to the scene
        prompt = f"{Character.SUMMARY_INSTRUCTION}\n{scene_context}\nExisting Memories:\n" + \
                "\n".join([memory.memory for memory in self.short_term_memory if memory.scene == scene])

        # Send the prompt to the LLM for generating a summary
        response = self.api_interaction.send_prompt(prompt)
        # Assume the response is formatted as multiple lines, each representing a separate memory
        long_term_memories = response.split('\n')
        # Store these summarized memories in long-term memory
        for memory in long_term_memories:
            self.long_term_memory.append(Memory(scene, memory))

        # Clear short-term memories related to this scene
        self.short_term_memory = [memory for memory in self.short_term_memory if memory.scene != scene]


    def construct_response_context(self, scene):
        """
        Constructs the response context for the character, including detailed scene information.
        
        Args:
            scene (Scene): The current scene object.
        """
        # Basic character information
        context = f"Who I am: {self.profile_data}\n"
        
        # Including short-term and long-term memory in the context
        current_scene_memories = [memory.memory for memory in self.short_term_memory if memory.scene == scene]
        context += "Short-term memory: " + "\n".join(current_scene_memories) + "\n"
        context += "Summary of story: " + "\n".join([memory.memory for memory in self.long_term_memory]) + "\n"
        
        # Utilizing the scene's format_for_llm method to include scene and participant info
        # This assumes that the Scene class has a method named 'format_for_llm' or similar
        scene_info = scene.format_for_llm() if hasattr(scene, 'format_for_llm') else f"Current Scene: {scene.sceneid}"
        
        # Combining the character context with the formatted scene information
        full_context = f"{context}\n{scene_info}"
        return full_context

    def respond_to_scene(self, scene):
        context = self.construct_response_context(scene)
        prompt = Character.REPLY_INSTRUCTION + "\n" + context
        response = self.api_interaction.send_prompt(prompt)
        return response


    async def summarize_memory_async(self, scene):
        """
        Asynchronously summarizes the character's experiences in a given scene,
        storing the summary in long-term memory, and clears the short-term memories
        associated with that scene.
        """
        scene_context = scene.format_for_llm()
        prompt = f"{Character.SUMMARY_INSTRUCTION}\n{scene_context}\nExisting Memories:\n" + \
                 "\n".join([memory.memory for memory in self.short_term_memory if memory.scene == scene])

        # Asynchronously send the prompt to the LLM for generating a summary
        response = await self.api_interaction.send_prompt_async(prompt)
        long_term_memories = response.split('\n')

        for memory in long_term_memories:
            self.long_term_memory.append(Memory(scene, memory))

        self.short_term_memory = [memory for memory in self.short_term_memory if memory.scene != scene]

    async def respond_to_scene_async(self, scene):
        """
        Asynchronously generates the character's response to the current scene.
        """
        context = self.construct_response_context(scene)
        prompt = Character.REPLY_INSTRUCTION + "\n" + context
        debug_print(f"submitted by:{self.name}\n{prompt}")
        response = await self.api_interaction.send_prompt_async(prompt)
        return response