import json
import sys
from pathlib import Path
import shutil
import random

SET_1 = Path(__file__).parent.parent / "scenarios" / "set-01.json"
SET_2 = Path(__file__).parent.parent / "scenarios" / "set-02.json"

def fetch_questions(path):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    random.Random().shuffle(data)
    return data

def hr(char="-"):
    width = shutil.get_terminal_size(fallback=(80, 24)).columns
    print(char * width)

def user_answer(question):
    hr("=")
    user_input = input("Your answer: ").strip()
    choices = question['choices']
    if (user_input == choices[question['correct']]):
        print(f"✅ Correct. Examples: {question['examples']}")
        return 1 
    else :
        print(f"❌ Incorrect. Correct: {choices[question['correct']]} Examples: {question['examples']}")
        return 0



def main():
    score = 0
    questions = fetch_questions(SET_1)

    for i, question in enumerate(questions, 1):
        print(f"\nQ{i}: {question['question']}")
        print(f"Choices: {question['choices']}")
        score += user_answer(question)
        print(f"Score: {score}/{i} ({(score / i) * 100:.2f}%)")
        print()

    print(f"~~~ Finished SET 1: {score}/{len(questions)} "
          f"({(score / len(questions)) * 100:.2f}%) ~~~")
    hr("-")

    score = 0
    questions = fetch_questions(SET_2)

    for i, question in enumerate(questions, 1):
        print(f"\nQ{i}: {question['question']}")
        print(f"Choices: {question['choices']}")
        score += user_answer(question)
        print(f"Score: {score}/{i} ({(score / i) * 100:.2f}%)")
        print()

    print(f"~~~ Finished SET 2: {score}/{len(questions)} "
          f"({(score / len(questions)) * 100:.2f}%) ~~~")
    
if __name__ == "__main__":
    main()