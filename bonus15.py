import json

with open("questions.json", "r") as file:
    questions = file.read()

data = json.loads(questions)

print(data)


