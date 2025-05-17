import chainlit as cl
from agents import Runner
from config import run_config
from agent import agent1

@cl.on_chat_start
async def on_chat_start():
    # Initialize history on chat start
    cl.user_session.set("history", [])
    await cl.Message(
        content="Hello! I am your assistant. How can I help you today?"
    ).send()

@cl.on_message
async def on_message(message: cl.Message):
    # Retrieve and update history
    history = cl.user_session.get("history", [])
    history.append({"role": "user", "content": message.content})

    # Run the agent with conversation history
    result = await Runner.run(
        input=history,
        run_config=run_config,
        starting_agent=agent1,
    )

    # Append assistant response to history and send it
    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)
    await cl.Message(content=result.final_output).send()
