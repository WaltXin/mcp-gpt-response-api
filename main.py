from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def main():
    client = OpenAI()
    response = client.responses.create(
            model="gpt-4.1",
            tools=[{"type": "web_search_preview"}],
            input="What was a positive news story from today?"
        )
    print(response.output_text)

if __name__ == "__main__":
    main()