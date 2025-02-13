import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

score = 0

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-",  alternative)
    user_choice = int(input("Enter your choice: "))
    question["user_choice"] = user_choice
    if question["user_choice"] == question["correct_answer"]:
        score += 1

for question in data:
    message = f"question: {question['question_text']}, your answer: {question['user_choice']}, correct answer: {question['correct_answer']}"
    print(message)
print("score: ", score)
print("percentage correct: ", score / len(data) * 100, "%")


# print(data)
# print(score)




