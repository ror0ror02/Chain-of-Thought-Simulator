import os
import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
from tenacity import retry, stop_after_attempt, wait_exponential
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder=os.path.abspath('templates'))
CORS(app)

# OpenAI API setup
openai.api_key = os.getenv("OPENAI_API_KEY")

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def generate_content_with_retry(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating content: {e}")
        raise

def think_and_respond(question, context=""):
    try:
        thoughts = []
        for i in range(10):
            prompt = f"""
            Context: {context}
            Question: {question}
            Current thoughts: {json.dumps(thoughts, ensure_ascii=False)}
            Write in first person.
            You are an advanced AI model that carefully considers questions. Your task is to deeply analyze the question and context.
            
            1. Break down the problem into subtasks.
            2. Consider various aspects and perspectives.
            3. Analyze possible consequences and implications.
            4. Think about potential counterarguments.
            5. Synthesize information for a comprehensive understanding.
            
            Continue your thoughts, developing and deepening previous ideas. If you think you've analyzed the question sufficiently and are ready to give a final answer with a solution, write 'Done'. If you want to continue, don't write this.
            ATTENTION! THE FINAL ANSWER SHOULD ALWAYS BE COMPLETE WITH A FULL RESPONSE TO THE QUESTION! write in the language of the question Try to keep your answers simple and short for routine questions.
            Current thinking step {i+1}/10 (If it's step 1, try to work out a plan for subsequent reflections):
            """
            thought = generate_content_with_retry(prompt)
            thoughts.append(thought)
            if 'Done' in thought:
                break
        
        final_prompt = f"""
        Context: {context}
        Question: {question}
        Thoughts: {json.dumps(thoughts, ensure_ascii=False)}
        
        Based on the analysis and reflections, give a concise, well-reasoned, and accurate answer to the original question. 
        Ensure your answer takes into account all important aspects considered during the thinking process.
        Structure your answer logically, using subheadings or numbering if appropriate. Try to keep your answers simple and short for routine questions.
        """
        answer = generate_content_with_retry(final_prompt)
        
        return {
            "think": True,
            "thoughts": thoughts,
            "answer": answer
        }
    except Exception as e:
        return {
            "error": str(e),
            "think": False,
            "thoughts": [],
            "answer": "Sorry, an error occurred while processing your request."
        }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('message')
    response = think_and_respond(question)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
