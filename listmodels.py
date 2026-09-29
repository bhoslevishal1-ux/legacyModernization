from openai import OpenAI

client = OpenAI(
    api_key="sk-y6vsj5_nwr6-W0sTm2LMuQ",
    base_url="http://10.221.0.164:4000"
)

models = [
    "si-dd-gpt-4",
    "si-dd-gpt-4.1",
    "si-dd-gpt-4.1-mini",
    "si-dd-gpt-4o",
    "si-dd-o4-mini"
]

for model in models:
    try:
        print(f"\nTesting {model}")

        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": "hello"
                }
            ]
        )

        print("SUCCESS")
        print(response.choices[0].message.content)

    except Exception as e:
        print("FAILED")
        print(e)