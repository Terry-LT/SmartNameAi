import ollama


def get_new_file_name(text):
    print("It will take some times, please wait!")
    command = '''My file contains this information. What would you name this file based on its content? Do not write anything except a JSON object. Your response must look like this: { "filename": "YOUR_OUTPUT_WITHOUT_FILE_EXTENSION" }.'''
    stream = ollama.chat(
        model='llama3.1',
        messages=[
            {'role': 'user',
             'content': f'''"{text}". {command}'''
             }
        ],
        stream=True,
    )
    output = ''''''
    for chunk in stream:
        output += chunk['message']['content']
        #print(chunk['message']['content'], end='', flush=True)
    return output