import json
from pathlib import Path
from security_controls import Category, ControlType
import shutil
import random

def fetch_questions():
    path = Path(__file__).parent.parent / "scenarios" / "set-01.json"
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    random.Random().shuffle(data)
    
    for question in data: 
        choices = question['choices']
        ans_index = question['correct']
        ans = choices[ans_index]
        random.Random().shuffle(question['choices'])
        question['choices'] = choices
        
        for index, choice in enumerate(choices):
            if (choice == ans):
                question['correct'] = index

    return data


def hr(char="-"):
    width = shutil.get_terminal_size(fallback=(80, 24)).columns
    print(char * width)

def user_answer(question):
    hr("=")
    user_input = input("Your answer: ").strip()

    if (user_input == question['answer']):
        print(f"✅ Correct. Examples: {question['examples']}")
        return 1 
    else :
        print(f"❌ Incorrect. Correct: {question['answer']} Examples: {question['examples']}")
        return 0

def main():
    score  = 0
    questions = fetch_questions()

    for i, question in enumerate(questions, 1):
        print(f"\nQ{i}: {question['definition']}")
        if (question['domain'] == "category"):
            print(f"    Security Control Categories {Category.MANAGERIAL.value, Category.OPERATIONAL.value, Category.PHYSICAL.value, Category.TECHNICAL.value}")
        if (question['domain'] == "type"):
            print(f"    Security Control Types {ControlType.COMPENSATING.value, ControlType.CORRECTIVE.value, ControlType.DETECTIVE.value, ControlType.DETERRENT.value, ControlType.DIRECTIVE.value, ControlType.PREVENTIVE.value}")
        score += user_answer(question)
        print()
        print(f"{(score / i) * 100:.2f}%")
        print()
        
if __name__ == "__main__":
    main()