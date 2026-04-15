import asyncio
import os
from backboard import BackboardClient
import dotenv

dotenv.load_dotenv()
ASSISTANT_ID = "deba4f6d-a7c3-439c-ad67-3fe79381ee1f"


async def main():
    client = BackboardClient(api_key=os.getenv("BACKBOARD_API_KEY"))
    # Step 1:
    # assistant = await client.create_assistant(
    #     name="My First Assistant",
    #     system_prompt="You are a helpful assistant that responds concisely."
    # )
    # print(f"Created assistant: {assistant.assistant_id}")
    #Step 1 Ends-----------------------

    #Step 2
    # thread = await client.create_thread(ASSISTANT_ID)
    # print(f"Created thread: {thread.thread_id}")
    #Step 2 Ends-----------------------

    #Step 3
    response = await client.add_message(
        thread_id="92205522-339e-4219-b37a-4f71d73502b6",
        content="say Hello World",
        stream=False
    )
    print(f"Assistant: {response.content}")
    #Step 3 Ends------------------------
asyncio.run(main())