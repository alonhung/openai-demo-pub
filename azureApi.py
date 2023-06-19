#chat
#Note: The openai-python library support for Azure OpenAI is in preview. import os
import openai
import os
openai.api_type = "azure"
openai.api_base = "https://oneport-openai-test-hong.openai.azure.com/" 
openai.api_version = "2023-05-15"
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "49e5c3349a1a4302b90c9fdc446d9330"

def generateChatResponse(prompt):
    messages = []
    messages.append({"role": "system", "content": "Your name is Karabo. You are a helpful assistant."})

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)
    print("messages:",messages)

    try:
        response = openai.ChatCompletion.create(
            engine="hong-gpt-35-turbo-0301",
            messages=messages,
            temperature=1, 
            max_tokens=800, 
            top_p=0.95, 
            frequency_penalty=0, 
            presence_penalty=0, 
            stop=None)
    except Exception as e:
        print(e)
        answer = str(e)
        return answer
            
    try:
        answer = response['choices'][0]['message']['content'].replace('\n', '<br>')
    except Exception as e:
        print(e)
        answer = str(e)
        return answer
    return answer