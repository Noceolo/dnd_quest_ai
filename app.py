from flask import Flask, render_template, request
import openai

app = Flask (__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    # Get data from the form
    num_players = int(request.form["num_players"])
    average_level = int(request.form["average_level"])

    # AI prompt
    prompt = f"""
    You are a Dungeon Master AI for Dungeons and Dragons. Generate an adventure for a group of {num_players} players with an average level of {average_level}.
    Include:
    - A short quest description.
    - An NPC who gives the quest, including their name, role, and personality.
    - An enemy to fight, scaled to their level.
    - Loot rewards appropriate for their level and the quest.
    """

    # Call OpenAI API
    openai.api_key = "YOUR_API_KEY_HERE"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use a GPT-3.5 or GPT-4 engine
        prompt=prompt,
        max_tokens=300,  # Adjust as needed
        temperature=0.7
    )

    # Parse the AI-generated text
    generated_text = response.choices[0].text.strip()

    # Display the content
    return f"""
        <h1>Generated Adventure</h1>
        <pre>{generated_text}</pre>
    """

if __name__ == "__main__":
    app.run(debug=True)
