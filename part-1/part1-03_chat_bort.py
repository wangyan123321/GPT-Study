import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
COMPLETION_MODEL = "text-davinci-003"


def get_response(prompt):
    response = openai.Completion.create(
        engine=COMPLETION_MODEL,
        prompt=prompt,
        temperature=1.0,
        max_tokens=1024,
        n=1,
        stop=None,
    )
    return response.choices[0].text


questions = []
answers = []


def generate_prompt():
    prompt = ""
    for i in range(len(questions)):
        prompt += "Q: " + questions[i] + "\n"
        if i < len(answers):
            prompt += "A: " + answers[i] + "\n"
    return prompt


def create_robot():
    while True:
        question = input("> ")
        if question == "exit":
            print("我先退下了!")
            break
        questions.append(question)
        answer = get_response(generate_prompt())
        answers.append(answer)
        print("A: " + answer)


create_robot()
