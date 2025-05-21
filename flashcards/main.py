import json
import random
import os

# Define the questions
questions = {
    "What year did the Titanic sink in the Atlantic Ocean on its maiden voyage?": "1912",
    "What is the capital city of Canada?": "Ottawa",
    "Which planet is known as the Red Planet?": "Mars",
    "Who wrote the play 'Romeo and Juliet'?": "William Shakespeare",
    "What is the smallest country in the world?": "Vatican City",
    "Who developed the theory of evolution by natural selection?": "Charles Darwin",
    "What is the chemical symbol for the element oxygen?": "O",
    "In what year did World War II end?": "1945",
    "What is the largest bone in the human body?": "Femur",
    "Which element has the atomic number 1?": "Hydrogen",
    "Who painted the ceiling of the Sistine Chapel?": "Michelangelo",
    "What is the longest river in the world?": "Nile",
    "Who is the author of the Harry Potter book series?": "J.K. Rowling",
    "What is the square root of 256?": "16",
    "Who was the first man to step on the Moon?": "Neil Armstrong",
    "What is the largest desert in the world?": "Antarctica",
    "What is the chemical formula for water?": "H2O",
    "Who is known as the 'Father of Modern Physics'?": "Albert Einstein",
    "What is the capital city of Australia?": "Canberra",
    "What is the hardest natural substance on Earth?": "Diamond",
}

# Load or initialize memory.json
memory_file = "memory.json"
data = {}

try:
    if os.path.exists(memory_file):
        with open(memory_file, 'r') as f:
            data = json.load(f)
except json.JSONDecodeError:
    print("Error: Unable to decode memory.json, initializing a new file.")
except Exception as e:
    print(f"Error: {e}")

# Initialize data for each question
for question in questions.keys():
    if question not in data:
        data[question] = {"attempts": []}

# Shuffle questions
items = list(questions.items())
random.shuffle(items)

# Start the quiz
correct_count = 0
total_questions = len(items)

print("\n-- Naveen's Flashcard Quiz --")
print("Enter your answers. Press Enter to see the correct answer.")
print("Spelling doesn't matter.\n")

for question, correct_answer in items:
    user_answer = input(f"Q: {question}\nYour answer: ").strip().lower()
    print(f"Correct Answer: {correct_answer}")
    
    # Check if the answer is correct
    is_correct = user_answer in correct_answer.lower()
    
    if is_correct:
        print("Great Job! You got it correct.")
        correct_count += 1
    else:
        print("Incorrect.")
    
    # Record the attempt
    data[question]["attempts"].append({
        "correct": is_correct
    })

# Save the updated data
try:
    with open(memory_file, "w") as f:
        json.dump(data, f, indent=4)
except Exception as e:
    print(f"Error saving memory.json: {e}")

# Display statistics
print(f"\n--- Current Session Performance ---")
print(f"Correct Answers: {correct_count}/{total_questions}")
current_percentage = (correct_count / total_questions) * 100
print(f"Accuracy: {current_percentage:.2f}%")

# Calculate all-time statistics
all_time_correct = 0
all_time_attempts = 0

for question in data:
    for attempt in data[question]["attempts"]:
        all_time_attempts += 1
        if attempt["correct"]:
            all_time_correct += 1

print("\n--- Overall Performance History ---")
print(f"Total Questions Answered: {all_time_attempts}")
print(f"Total Correct Answers: {all_time_correct}/{all_time_attempts}")

if all_time_attempts > 0:
    all_time_percentage = (all_time_correct / all_time_attempts) * 100
    print(f"Overall Accuracy: {all_time_percentage:.2f}%")
else:
    print("No attempts recorded yet.")
    breakpoint