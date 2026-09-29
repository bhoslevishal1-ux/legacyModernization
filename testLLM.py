from openai import OpenAI

client = OpenAI(
    api_key="sk-y6vsj5_nwr6-W0sTm2LMuQ",
    base_url="http://10.221.0.164:4000"
)

response = client.chat.completions.create(
    model="si-dd-gpt-4.1",
    messages=[
        {
            "role": "user",
            "content": "Say hello"
        }
    ]
)

print(response.choices[0].message.content)