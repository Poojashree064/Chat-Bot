from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = "Use your actual OpenAI API key"  
# Define the default route to render the index.html
@app.route("/")
def index():
    return render_template("index.html")

# API route to handle POST requests from the frontend
@app.route("/api", methods=["POST"])
def api():
    # Get the user message from the request
    message = request.json.get("message")

    # Send the message to OpenAI's API and receive the response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use appropriate model
            messages=[
                {"role": "user", "content": message}
            ]
        )
        completion = response.choices[0].message.get("content", "")
        return jsonify({"content": completion})
    except Exception as e:
        return jsonify({"content": "Failed to generate response."})

if __name__ == "__main__":
    app.run(debug=True)  # Run with debugging enabled for easier error tracking

