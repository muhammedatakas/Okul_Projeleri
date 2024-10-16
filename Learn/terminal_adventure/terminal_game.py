import random
import ollama

# A function to interact with the Ollama model and stream responses
def generate_story_and_options(prompt):
    story_prompt = prompt + "\n\n" + \
                   "Continue the story and provide 3-4 options for what happens next. " + \
                   "Sometimes, mention finding coins."

    # Use streaming to get the response as it generates
    stream = ollama.chat(model='llama3', messages=[
        {"role": "user", "content": story_prompt}
    ], stream=True)

    full_story = ""
    for chunk in stream:
        content = chunk['message']['content']
        print(content, end='', flush=True)  # Print each chunk as it arrives
        full_story += content

    return full_story  # Return the full story once streaming is complete

# Check for 'The End' to conclude the story
def check_for_story_end(story_segment):
    return "The End" in story_segment or "fatal mistake" in story_segment.lower()

# Function to simulate finding coins in the story
def check_for_coins(story_segment):
    if "found" in story_segment.lower() and "coin" in story_segment.lower():
        return random.randint(10, 100)  # Random coin amount found
    return 0

# Main interactive storytelling loop with coin collection and sudden end conditions
def interactive_story():
    prompt = "You are a brave adventurer who has just entered an ancient temple. What will you do next?"
    total_coins = 0  # Initialize coin counter
    story_over = False
    
    while not story_over:
        # Generate the next part of the story, including options
        story_segment = generate_story_and_options(prompt)
        print("\n\n")  # Add space after the streamed story segment

        # Check if the player found coins
        coins_found = check_for_coins(story_segment)
        if coins_found > 0:
            total_coins += coins_found
            print(f"\nYou found {coins_found} coins! Total coins: {total_coins}")

        # End the story if coins exceed 1000 or story concludes naturally
        if total_coins >= 1000:
            print("\nCongratulations! You've collected 1000 coins. The adventure is complete!")
            story_over = True
            break

        if check_for_story_end(story_segment):
            print("\nThe story has concluded.")
            story_over = True
            break

        # Extract options (assuming they are numbered in the story)
        options_start = story_segment.rfind("1.")
        if options_start == -1:
            print("\nNo options were generated. Ending the story.")
            break

        story_text = story_segment[:options_start].strip()
        options_text = story_segment[options_start:].strip()

        print("\nYour choices:")
        print(options_text)

        # Get user input
        choice = input("Choose an option (enter the number): ")
        while not choice.isdigit():
            choice = input("Invalid choice. Please enter a valid number: ")

        # If the choice leads to sudden death or a "wrong" decision, end the game
        if "wrong choice" in story_segment.lower() or "fatal mistake" in story_segment.lower():
            print("\nOh no! You've made a fatal mistake. The adventure is over.")
            story_over = True
            break

        # Update the prompt to continue the story based on the player's choice
        prompt = f"You chose option {choice}. Now, continue the story."

# Run the interactive story
if __name__ == "__main__":
    interactive_story()
