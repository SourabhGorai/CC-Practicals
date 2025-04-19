import requests
import json

# Azure OpenAI API credentials
API_KEY = "8zQVvmoBZdezoPZKosGdaLrrtoZ6PTzPIqnRIly0j1f1DiCStyliJQQJ99BCACHYHv6XJ3w3AAAAACOGmA8T"
ENDPOINT = "https://nktik-m8hv2vz2-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2025-01-01-preview"

# Function to call the Azure OpenAI API
def chat_with_gpt(prompt):
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY
    }

    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 200,  # Limit response length
        "temperature": 0.7  # Controls randomness
    }

    response = requests.post(ENDPOINT, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"

# Example usage
if __name__ == "__main__":
    user_input = input("Ask GPT-4: ")
    response = chat_with_gpt(user_input)
    print("\nGPT-4 Response:", response)
