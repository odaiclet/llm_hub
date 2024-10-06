# Instructions on how to run the LLM

### 1. Copy API key
1. Visit to the developer playground of [groq.com](https://console.groq.com/?_gl=1*aejmar*_gcl_au*ODE3NTQ0NDUzLjE3MjgyMzU0NzI.*_ga*OTY2OTUzNzguMTcyODIzNTQ3MQ..*_ga_4TD0X2GEZG*MTcyODIzNTQ3MS4xLjEuMTcyODIzNTQ3MS42MC4wLjA) and create a developer account
2. On the left menu click on "API Keys" and generate api key.
3. After generating the key click on copy.
### 2. Pase the key on a ".env" file
1. create file called ".env"
2. The contents should look like:<br>
`API_KEY = your_groq_api_key #Note: don't use quotation marks`

### 3. install these libraries 
- python-dotenv : this is for parsing env variables into global env
- gloq : for connecting to the llm endpoint
- os : for reading env variables

`pip install python-dotenv gloq os`

### 4. run program
Now you can run your `llm_setup.py` file. Remember that you can edit the prompt portion to have the LLM respond to your questions.

# Tips:
### spending score definition
Use something similar to this to produce the spending score definition/criteria
prompt_template = "I need to define a 'metric' or 'score' that models people's spending. How would you define this metric? and how would the buckets be classified? Make sure the score is 1 for really bad spending and 10 for really good."

