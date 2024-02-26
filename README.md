# rrrs-dev-project
Master folder for the RRRS project which includes several subprojects and associated folders

## Round-Robin-Reactive-Storytelling (RRRS) System

An innovative agent-oriented ensemble-based AI assisted interactive story teller that injects the user into the story as a character with thoughts, feelings, and opinions which help drive the direction of the story, without requiring the user to be an author of the story.

### Innovative Solution to Technical Limitations of the Genre
Most collaborative narrative AI systems allow a user to chat with or even co-create a narrtive, but have a number of AI-based limitations.

1. Most systems allow the user to define a single character to talk to
2. Multiple character conversation systems are not reliable in maintaining the personality of the various characters
3. Characters are static, and don't tend to learn new things or change their behavior due to events in the story, leading to inorganic interactions.
4. AI context lengths mean you must sacrifice character profile detail for more narrative length
5. The user often ends up taking the bulk of the writing responsibility, as opposed to being a participant in the story; ai characters tend to become repetitive and even degrade in qualityy and quantity of returned input.

### How RRRS tries to fix these issues

1. The user defines their character, just as they would theother characters, giving life and personality to their avatar that other characters can understand
2. Can defined an unlimited number of characters to participate in the story.
3. Every character has their own identity, personality profile, and wants and goals.
4. Every Character reads and reacts organically to the story privately to the storyy-teller agent, providing context and rich meta-data to allow a rich narrative to develop
5. Every character has their own short and long-term memory that do not clutter the main story context with extra confusing detail, allowing the story teller to stick to a coherent story more easily
6. Every character summarizes their parts of the story independently! This is HUGE! If a character is not in a scene, then they will not have memoryy of anything that happend in that scene, allowing characters to be surprised by events or even allowing different interpretations of events by different characters.

### How is this possible?

Using a custom agent-based system, you can define a character with natural language and the RRRS system uses highly-tailored zero-shot instructions through multiple recurring LLM calls to allow the agents to think independently from each other while experiencing the same story. The Story/Scene/Character/Memory (SSCM) architecture allows characters to maintain their own memories and thoughts, allowing their character to develop over the course of the story, without sacrificing the primary story context length.

Speaking of context length; the main story context is broken into scenes. This means that each scene can use the bulk of your available context, and a new scene will not substantially grow your context towards its limit. A Story summarization process happens at the end of each scene, allowing the story teller to maintain continuity of the overarching story without having to maintain all the text of the story in every request. 

This is also the case with characters, which have their own unique interpretation of the events of a scene, which form new memories which may later influence their personality or behavior. Their memories do not affect the story context size, or the available context for other characters... meaning system latency tollerance is the only tradeoff for adding more characters to your story.

### TLDR;

Instead of a user and an AI chatting and contributing to the context length with each prompt and response, there are several hidden LLM calls that happen in the background to each uniquely process the story from a certain perspective. Then, the ongoing internal-thinking of the characters (and user) are provided to the narrator, who writes the story appropriately. It's a wholey new way to experience collaborative storytelling that is closer to a D&D session with an expert DM than a discord chat room.

### Coming Features

* Integration with Stable Diffusion which will allow an illustrator-agent to craft accurate and interesting visualizations of the the scenes as they happen.
* Alternate workflows and customizable storyteller instructions
* web-ui? Maybe?
* Do-Over and Undo options for user to force a rewrite
* publication tools that can take a story and scenes and export them in e-book style/form
* user-as-narrator feature, allowing you to be the writer receiving feedback from the characters as you go
* standardized character profile formats for easy character crafting
* user-directed scene and chapter controls/setup/steering
