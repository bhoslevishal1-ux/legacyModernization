from openai import OpenAI

class ParagraphSummarizer:

    def __init__(
        self,
        api_key,
        base_url,
        model
    ):
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

        self.model = model

    def summarize(
        self,
        code
    ):

        prompt = f"""
You are a COBOL modernization expert.

Analyze the COBOL paragraph.

Provide:

1. Purpose
2. Business Rules
3. Suggested Java Method Name

COBOL:

{code}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return (
            response
            .choices[0]
            .message
            .content
        )