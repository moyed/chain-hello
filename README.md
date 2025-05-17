# Chainlit Agent

A simple chat assistant built with Chainlit and Gemini API.

## Description

This project uses an agent developed on Gemini API.

When you send a task to the assistant, it returns:

* A list of tasks needed to complete the job.
* People responsible for each task.

## Prerequisites

* Python 3.9 or higher
* Chainlit installed (`pip install chainlit`)
* A `.env` file with your `GEMINI_API_KEY`
* Agent model built on Gemini API

## Installation

1. Clone this repository:

   ```bash
   git clone https://your-repo-url.git
   cd your-repo-url/chainlit_agent
   ```
2. Install dependencies with UV package manager:

   ```bash
   uv install
   ```

   Using UV makes a `requirements.txt` file optional.
3. Copy the example environment file and set your API key:

   ```bash
   cp .env.example .env
   # then edit .env and add GEMINI_API_KEY
   ```

## Configuration

* **config.py**: Loads env vars and sets up provider, model, and run configuration.
* **agent.py**: Defines the agent’s name and instructions.
* **main.py**: Contains Chainlit event handlers for chat start and messages.

## Usage

Start the app using Chainlit:

```bash
chainlit run main.py
```

Open the displayed URL in your browser and start chatting.

## Project Structure

```
chainlit_app/
├── config.py       # Env & model setup
├── agent.py        # Agent definition
└── main.py         # Chat event handlers
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
