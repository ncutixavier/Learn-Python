from Questions import Questions

question_prompt = [
    "What color of apple?\n(a) purple\n(b) red\n(c) yellow\n(d) black\n\n",
    "What color of banana?\n(a) purple\n (b) red\n (c) yellow\n (d) black\n\n",
    "What color of orange?\n (a) green\n (b) red\n (c) yellow\n (d) black\n\n",
    "What color of blackboard?\n (a) green\n (b) red\n (c) yellow\n (d) black\n\n"
]

questions = [
    Questions(question_prompt[0], "a"),
    Questions(question_prompt[1], "c"),
    Questions(question_prompt[2], "c"),
    Questions(question_prompt[3], "d")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got "+str(score)+"/"+str(len(questions))+"\nThank you!")

run_test(questions)
print("____________________________________________________________________")


