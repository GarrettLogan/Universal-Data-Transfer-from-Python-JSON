import json

FILENAME = "my_data.json"
TRANSFERRABLE_ACCOUNTS = {
    1: {"name": 'Garrett', "age": 23, "skills": ["Software Engineering", "Web Development", "Integration Engineering"]},
    2: {"name": 'John', "age": 19, "skills": ["Software Engineering", "Web Development"]},
    3: {"name": 'Abel', "age": 26, "skills": ["Technician", "Industrial Production"]},
}

def save_to_json(filename="output.json", **variables):
    # Default Variable save in case filename unprovided aswell as helper for later use to save
    with open(filename, "w") as f:
        json.dump(variables, f, indent=4)

def load_from_json(filename="output.json"):
    # Load variables back from a JSON file into a dictionary.
    with open(filename, "r") as f:
        return json.load(f)

class Profile:
    def __init__(self, id, name, age, skills):
        self.id = id
        self.name = name
        self.age = age
        self.skills = skills

    def __repr__(self):
        return f"Profile(id={self.id}, name={self.name}, age={self.age}, skills={self.skills})"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "skills": self.skills,
        }

profiles = [Profile(id, info["name"], info["age"], info["skills"]) for id, info in TRANSFERRABLE_ACCOUNTS.items()]

# Save variables
save_to_json(FILENAME, profiles=[p.to_dict() for p in profiles])

# Load saved values fromjson created file
data = load_from_json(FILENAME)

# Call from data file
for profile in data["profiles"]:
    print(profile)
    print(profile["name"])
    print(profile["age"])
    print(profile["skills"])

# Call from data file variables
for profile in data["profiles"]:
    profile = profile
    id = profile["id"]
    name = profile["name"]
    age = profile["age"]
    skills = profile["skills"]
    print(id, name, age, skills)
    # From here do what you wish with each individual user profile
