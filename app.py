import os
from flask import Flask, render_template, request, redirect, url_for, flash

try:
	from together import Together
except Exception:
	Together = None


app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-key")


def load_together_api_key() -> str | None:
	"""Return Together API key from env or local together.key file."""
	key = os.environ.get("TOGETHER_API_KEY")
	if key:
		return key
	try:
		with open("together.key", "r", encoding="utf-8") as f:
			return f.read().strip()
	except FileNotFoundError:
		return None


def get_together_client():
	"""Create and return a Together client. Raises if API key is missing."""
	api_key = load_together_api_key()
	if not api_key:
		raise RuntimeError("Together API key not found. Set TOGETHER_API_KEY or add together.key file.")
	if Together is None:
		raise RuntimeError("together package is not available. Install it with: pip install together")
	return Together(api_key=api_key)


def generate_outfit_suggestions(user_question: str) -> str:
	"""Send the user's question to Together AI and return the assistant's reply."""
	client = get_together_client()

	stylist_prompt = (
		"Act as my exclusive personal stylist.\n\n"
		"Scenario:\n"
		"- Weather: Sunny\n"
		"- Temperature: 15°C\n\n"
		"Your Task:\n"
		"Create a complete outfit coordination for this weather condition. Your suggestion should be detailed and include:\n\n"
		"1. Color Palette: Suggest harmonious colors that suit a sunny day.\n"
		"2. Materials: Recommend appropriate fabrics for this temperature.\n"
		"3. Garment Types: Specify the types of clothing items (e.g., layering pieces, outerwear).\n"
		"4. Total Coordination: Combine these elements into a cohesive outfit.\n\n"
		"Please present your recommendation in a clear, structured manner."
	)

	model = "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free"
	response = client.chat.completions.create(
		model=model,
		messages=[
			{"role": "system", "content": stylist_prompt},
			{"role": "user", "content": user_question},
		],
		temperature=0.8,
	)
	return response.choices[0].message.content.strip()


@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
	question = (request.form.get("question") or "").strip()
	if not question:
		flash("Please enter a fashion question.")
		return redirect(url_for("index"))

	try:
		answer = generate_outfit_suggestions(question)
	except Exception as e:
		flash(f"There was an error generating suggestions: {e}")
		return redirect(url_for("index"))

	return render_template("result.html", question=question, answer=answer)


if __name__ == "__main__":
	# Run the Flask development server for Hugging Face Spaces
	app.run(host="0.0.0.0", port=7860, debug=False)
