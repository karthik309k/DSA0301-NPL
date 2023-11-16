import openai

# Set your OpenAI GPT-3 API key
openai.api_key = 'your_api_key_here'

# Define a prompt for GPT-3
prompt = "Once upon a time in a land far, far away,"

# Generate text using GPT-3
response = openai.Completion.create(
    engine="text-davinci-003",  # You can choose a different engine
    prompt=prompt,
    max_tokens=100  # Adjust as needed
)

# Print the generated text
generated_text = response.choices[0].text
print(generated_text)
