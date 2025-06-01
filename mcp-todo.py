from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


resp = client.responses.create(
    model="gpt-4.1",
    tools=[
        {
            "type": "mcp",
            "server_label": "todo",
            "server_url": "https://remote-mcp-server-authless.waltxxw.workers.dev/mcp",
            "require_approval": "never",
        },
    ],
    input="add sing a song today to my todo list",
)


print(resp.output_text)