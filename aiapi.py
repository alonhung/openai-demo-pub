# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import config
openai.api_key = config.DevelopmentConfig.OPENAI_KEY

def generateChatResponse(prompt):
    messages = []
    messages.append({"role": "system", "content": "Your name is Karabo. You are a helpful assistant."})

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)

    response = openai.Completion.create(model="gpt-3.5-turbo",messages=messages)
    

    try:
        answer = response['choices'][0]['message']['content'].replace('\n', '<br>')
    except:
        answer = 'Oops you beat the AI, try a different question, if the problem persists, come bacl later.'
    print("answer:",answer)
    return answer
