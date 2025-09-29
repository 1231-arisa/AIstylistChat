from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Configure OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_stylist():
    user_question = request.form['question']
    
    try:
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Falls back to gpt-3.5-turbo if not available
            messages=[
                {"role": "system", "content": "You are a friendly fashion assistant called AIstylist. Provide helpful, practical outfit suggestions. Keep responses conversational and encouraging. Include specific clothing items and styling tips."},
                {"role": "user", "content": user_question}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        
    except Exception as e:
        ai_response = f"I'm sorry, I'm having trouble connecting right now. Please try again later. Error: {str(e)}"
    
    return render_template('result.html', question=user_question, response=ai_response)

if __name__ == '__main__':
    app.run(debug=True)
