import time
import random

# List of sentences for typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "In the middle of difficulty lies opportunity.",
    "Life is what happens when you're busy making other plans.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts."
]

def typing_test():
    # Select a random sentence
    sentence = random.choice(sentences)
    print("Type the following sentence as fast as you can:")
    print(f"\n\"{sentence}\"\n")
    
    # Start the timer
    start_time = time.time()
    
    # Get user input
    user_input = input("Your input: ")
    
    # Stop the timer
    end_time = time.time()
    
    # Calculate time taken
    time_taken = end_time - start_time
    
    # Calculate WPM
    words_typed = len(user_input.split())
    minutes_taken = time_taken / 60
    wpm = words_typed / minutes_taken if minutes_taken > 0 else 0
    
    # Calculate accuracy
    correct_words = sum(1 for word1, word2 in zip(user_input.split(), sentence.split()) if word1 == word2)
    accuracy = (correct_words / len(sentence.split())) * 100
    
    # Display results
    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Words typed: {words_typed}")
    print(f"Words per minute (WPM): {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_test()