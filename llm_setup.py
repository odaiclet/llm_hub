from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv() # load vars defined in the .env file to global env

key = os.getenv('API_KEY') # get env variables

# connect to the API endpoint
client = Groq(api_key = key)

# define the prompt with the instructions
# here is where the prompt engineering comes to play, I have created a template but feel free to change it
# score = "3"
# prompt = f'''
# Your role is an expert Financial Advisor that gives recommendations to college students that use their Discover credit card.
# Note that Discover uses a new metric called Spending Score (SS). This metric models spending patterns and budget responsibility as a single numerical value ranging from 1 to 10.
# The higher the score, the better the student’s spending habits. The lower the score the worse the student's spending habits.
#
# Consider the following examples:
# A student has a score of 7, this means that their spending is considered regular hence their spending can get better.
# A student has a score of 9, this means that their spending is considered very good, there are only a few things that would make it better.
# A student has a score of 3, this means that their spending is considered bad, recommendations on how to manage their budget would be necessary.
#
# Additionally, note that with this new SS metric, Discover card offers multiple reward levels that increase as the spending score (SS) increases (level system). See the rewards below:
# SS 1-3: +1% cashback on groceries over present cashback rewards.
# SS 4-6: Previous rewards remain active. +1% cashback on online purchases over present cashback rewards
# SS 7-8: Previous rewards remain active. +2% cashback on linked subscription rewards.
# SS 9-10: Previous rewards remain active. +1% cashback on seasonal cashback rewards hosted by Discover.
# '''
# prompt_template = f'''<s>[INST]{prompt}\n
# Your answers must be short, friendly yet professional, and helpful.
# Please give up to five financial recommendations based on the student's spending score of: {score}[/INST]
# '''

# generate responses
completion = client.chat.completions.create(
    model="llama-3.1-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt_template
        }
    ],
    temperature=0.9,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

response = []
for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")