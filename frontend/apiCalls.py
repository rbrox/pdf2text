import json
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

def fetchData(preprocessed_text):
    
    systemPrompt = "You are a informed pdf reader designed to output JSON. of format {title: str, summary: str, comments: str}."
    userPrompt = "Generate a JSON object from the text:"
    
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": userPrompt + preprocessed_text},
        ]
    )
    content_str = response.choices[0].message.content
    content_dict = json.loads(content_str)
    return content_dict
    

def callGPT3(filePath="preprocessed_text.txt", systemPrompt="", userPrompt=""):
    client = OpenAI(api_key=api_key)
    with open(filePath, 'r') as f:
        txt = f.read()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": systemPrompt},
            {"role": "user", "content": userPrompt + txt},
        ]
    )

    # Extracting the content from response.choices
    content_str = response.choices[0].message.content
    content_dict = json.loads(content_str)

    # Writing the content to response.txt
    with open('response.txt', 'w') as f:
        f.write(content_str)

    # Dumping the content as JSON to response.json
    with open('response.json', 'w') as f:
        json.dump(content_dict, f, indent=4)

    return content_dict

if __name__ == "__main__":
    sysPrompt = "You are a informed pdf reader designed to output JSON. of format {title: str, summary: str, comments: str}."
    userPrompt = "Generate a JSON object from the text:"
    res = fetchData("The quick brown fox jumps over the lazy dog")
    print(res)
