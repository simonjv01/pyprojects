import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-",  alternative)
    user_choice = int(input("Enter your choice: "))
    question["user_choice"] = user_choice
    if question["user_choice"] == question["answer"]:
        question["correct"] = True

print(data)



