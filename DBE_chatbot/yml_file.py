import yaml
import random
EXAMPLE_TEXT = 'Hi, How is it going?'
with open('greetings.yml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    conversations = data["conversations"]

bot_response_arr = []
for conv_pair in conversations:
    if EXAMPLE_TEXT in conv_pair:
        bot_response_arr.append(conv_pair[1].capitalie())
        
print(random.choice(bot_response_arr))
s.translate(None, string.punctuation)