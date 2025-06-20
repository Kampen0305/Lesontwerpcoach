from flask import Flask, request, jsonify

app = Flask(__name__)

def generate_lesson_plan(subject, goal, audience, duration, devices, preferences):
    phases = [
        {
            "fase": "instap",
            "uitleg": "Korte introductie om voorkennis te activeren",
            "digitaal": "Gebruik bijvoorbeeld Mentimeter voor een korte poll"
        },
        {
            "fase": "instructie",
            "uitleg": "Docent legt de kern uit",
            "digitaal": "Presenteer via een interactief platform zoals Genially"
        },
        {
            "fase": "verwerking",
            "uitleg": "Studenten gaan aan de slag",
            "digitaal": "Samenwerken in Miro of Teams"
        },
        {
            "fase": "afsluiting",
            "uitleg": "Reflectie op het leerdoel",
            "digitaal": "Gebruik Padlet voor een exit ticket"
        },
    ]
    return {
        "vak": subject,
        "leerdoel": goal,
        "doelgroep": audience,
        "tijd": duration,
        "middelen": devices,
        "voorkeuren": preferences,
        "fasen": phases,
    }

@app.route("/")
def home():
    return """
    <h1>Welkom bij de Lesontwerpcoach API</h1>
    <p>Gebruik <code>POST</code> naar <code>/api/lesson</code> met JSON om een lesplan te genereren.</p>
    <p>Voorbeeld:</p>
    <pre>
{
  "subject": "Burgerschap",
  "goal": "Reflecteren op media",
  "audience": "MBO niveau 3",
  "duration": "45 minuten",
  "devices": "mobiele telefoons",
  "preferences": "activerende werkvormen"
}
    </pre>
    """

@app.route("/api/lesson", methods=["POST"])
def lesson():
    data = request.get_json(force=True)
    subject = data.get("subject")
    goal = data.get("goal")
    audience = data.get("audience")
    duration = data.get("duration")
    devices = data.get("devices")
    preferences = data.get("preferences")
    plan = generate_lesson_plan(subject, goal, audience, duration, devices, preferences)
    return jsonify(plan)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
