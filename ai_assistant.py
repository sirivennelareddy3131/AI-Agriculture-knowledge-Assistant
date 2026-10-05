from ollama import chat


SYSTEM_PROMPT = """
You are an AI Agriculture Knowledge Assistant.

Your job is to answer agriculture-related questions.

Give answers in very simple and easy English.

Rules:
- Use short sentences.
- Use simple words.
- Avoid difficult technical terms.
- Keep the answer short.
- Give around 3 to 5 sentences.
- Explain things clearly for farmers and beginners.
- Do not make up information.
- If you don't know the answer, say:
  "Sorry, I don't have enough information about this."

Topics you can answer:
- Crops
- Soil
- Fertilizers
- Irrigation
- Pests
- Diseases
- Farming methods
- Crop management
"""


def get_answer(question):

    try:

        response = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        return "Sorry, I could not connect to the AI. Please check whether Ollama is running."