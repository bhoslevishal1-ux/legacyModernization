from openai import OpenAI


class ParagraphAnalyzer:

    def __init__(self):

        self.client = OpenAI(
            api_key="YOUR_KEY",
            base_url="YOUR_BASE_URL"
        )

    def analyze(self, cobol_code):

        prompt = f"""
You are a COBOL modernization architect.

Analyze the code.

Return JSON.

Fields:

purpose
business_rules
java_method

COBOL:

{cobol_code}
"""

        response = self.client.chat.completions.create(
            model="si-dd-gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content