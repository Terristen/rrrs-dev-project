from narrative.narrative_engine import NarrativeEngine
import asyncio
from concurrent.futures import ThreadPoolExecutor

async def main():
    from  openai_api.api_interaction import APIInteraction
    
    api_interaction = APIInteraction()
    prompt = "Tell me a story about a dragon who loves books."
    response = await api_interaction.send_prompt_async(prompt)
    print(response)

def test():
    # Create a scene
    scene = Scene("scene1", "A quiet village.")

    # Create a memory associated with the scene
    memory = Memory(scene, "It was peaceful and calm.")

    # Create a character and add the memory
    character = Character("John Doe", "A curious wanderer.")
    character.add_memory(memory)

    # Output to verify
    print(f"Character: {character.name}, Profile: {character.profile_data}")
    for mem in character.short_term_memory:
        print(f"Memory: {mem.memory}, Scene: {mem.scene.scene_text}, Timestamp: {mem.timestamp}")

def test_narrative_system():
    from narrative.story import Story
    from character.character import Character
    from character.user_character import UserCharacter
    from narrative.narrative_engine import NarrativeEngine
    from narrative.scene import Scene

    # Create a new story
    story = Story("A Tale of Two Cities", "It was the best of times, it was the worst of times.")

    # Create characters
    user_character = UserCharacter("Charles", "A driven and compassionate protagonist.", "A wonderful person.")
    other_character = Character("Sydney", "A complex character with a mysterious past.", "A not so wonderful person.")
    
    # Add characters to the story
    story.add_character(user_character)
    story.add_character(other_character)

    # Create the initial scene
    initial_scene = Scene("Scene 1", "The story begins in a bustling city filled with hope and despair.")
    story.add_scene(initial_scene)

    # Initialize the Narrative Engine with the story
    narrative_engine = NarrativeEngine(story)

    # For the sake of the test, simulate round-robin interactions
    # This is a placeholder for where the actual round-robin logic would go
    print("Starting the round-robin process...")
    narrative_engine.conduct_round_robin()  # Simplified for demonstration

    # Display the current state of the story
    print(f"Story Title: {story.title}")
    print(f"Story Description: {story.description}")
    for scene in story.scenes:
        print(f"Scene ID: {scene.sceneid}, Scene Text: {scene.scene_text}")
        print("Characters in Scene:")
        for character in story.characters:
            print(f" - {character.name}: {character.description}")


async def test_character_async_functions():
    from narrative.story import Story
    from character.character import Character
    from character.user_character import UserCharacter
    from narrative.narrative_engine import NarrativeEngine
    from narrative.scene import Scene
    from openai_api.api_interaction import APIInteraction
    
    # Create a scene object with all necessary components
    scene = Scene("001", "The ancient forest is silent, save for the whisper of leaves in the wind.")

    # Create a character object with a basic personality
    api_interaction = APIInteraction()  # Ensure this is set up for async
    character = Character("Elara", "A curious explorer with a keen sense of adventure. fear of the dark, fear of the supernatural", "Quick witted Adventurer.", api_interaction)
    scene.add_character(character)
    
    # Test the async functions of the character class with sample scenes
    await character.summarize_memory_async(scene)
    response = await character.respond_to_scene_async(scene)
    
    # Output the results
    print("Response from character's async function:", response)
    
    

if __name__ == "__main__":
    #test_narrative_system()
   asyncio.run(test_character_async_functions())