import openai

def morse_to_text(morse_code):
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '-----': '0', '/': ' '
    }

    words = morse_code.strip().split('   ')
    letters = [word.split(' ') for word in words]
    decoded_text = ''

    for word in letters:
        for letter in word:
            decoded_text += morse_dict.get(letter, '?')
        decoded_text += ' '

    return decoded_text.strip()

openai.api_key = input("enter your OpenAI API key to start a conversation\n")
print("--------------------------------")

conversation = []

while (True):
    prompt = input()
    conversation.append({"role" : "user", "content" : prompt})
    response = openai.ChatCompletion.create(model = "gpt-3.5-turbo-16k", messages = conversation, max_tokens = 200, temperature = 1)
    
    morse_response = openai.ChatCompletion.create(model = "gpt-3.5-turbo-16k", messages = [response.choices[0].message, {"role" : "user", "content" : "Now respond in morse code"}], max_tokens = 500, temperature = 0)
    morse_response.choices[0].message.content = morse_to_text(morse_response.choices[0].message.content)
    conversation.append(morse_response.choices[0].message)
    print(conversation[-1].content)