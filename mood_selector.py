import json

def load_mood_templates(path="mood_templates.json"):
    with open(path, "r") as file:
        return json.load(file)

def format_prompt(mood, question, templates):
    template = templates.get(mood.lower(), templates["smart"])
    return template.replace("{question}", question)
