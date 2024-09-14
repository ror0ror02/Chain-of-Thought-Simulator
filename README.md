# Chain-of-Thought-Simulator


This project is a simulation of the Chain of Thought concept, inspired by OpenAI's o1 project in early access.

## About the Project

The Chain of Thought Simulator is an experimental web application that mimics the thinking process of an advanced AI model, similar to OpenAI's o1. Our project aims to demonstrate how AI can use a chain of reasoning to solve complex problems, much like a human would.

## Key Simulation Features

- **Thought Chain**: The AI "thinks" about the question, providing a step-by-step reasoning process.
- **Adaptive Learning**: Simulation of AI attempts to improve its reasoning strategies.
- **Task Breakdown**: Demonstration of how AI breaks down complex problems into simpler steps.
- **Error Correction**: Simulation of the process where AI recognizes and corrects its mistakes.
- **Flexible Approach**: Illustration of how AI tries different approaches when the current one isn't working.

## Technologies

- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- AI Simulation: Configurable to use various LLM models (default: GPT-4)

## Installation and Setup

1. Clone the repository:
   
*git clone https://github.com/your-username/chain-of-thought-simulator.git*

*cd chain-of-thought-simulator*

3. Install dependencies:

*pip install flask flask-cors openai python-dotenv tenacity*

3. Create a `.env` file in the root directory and add your API key:

*OPENAI_API_KEY=your_api_key_here*

4. Run the Flask server:

*python app.py*

5. Open `index.html` in your web browser.

## Usage

1. Enter a complex question or task in the input field.
2. Observe the simulation of the AI's "thinking" process.
3. Study the step-by-step chain of reasoning presented by the AI.
4. Receive the final answer based on the conducted analysis.

## Configuring Different LLM Models

This simulator is designed to be flexible and can work with various Language Model APIs. By default, it uses OpenAI's GPT-4, but you can easily configure it to use other models:

1. Open `app.py`
2. Locate the `generate_content_with_retry` function
3. Modify the API call to use your preferred LLM model

Example for using a different OpenAI model:

*model="gpt-3.5-turbo",  # Change this to your preferred model*

For using other LLM APIs, you'll need to adjust the API call according to their specific requirements.

## Limitations
It's important to note that this is a simulation based on publicly available information about the o1 project. It does not reflect the actual capabilities of o1 or other advanced AI systems by OpenAI. Our implementation uses configurable LLM models to imitate the reasoning process and may not correspond to the exact methods used in o1.

## Contributing
We welcome contributions to the Chain of Thought Simulator! If you have ideas for improving the simulation or you've found a bug, please create an issue or submit a pull request.

## License
This project is distributed under the MIT License. See the LICENSE file for details.

### Disclaimer
This project is not affiliated with OpenAI and does not represent an official implementation of o1 or any other OpenAI product. It is created solely for educational and research purposes.
