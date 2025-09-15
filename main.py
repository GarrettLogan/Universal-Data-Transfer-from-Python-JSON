import json

def save_to_json(filename="output.json", **variables):
    # Save provided variables into a JSON file.
    with open(filename, "w") as f:
        json.dump(variables, f, indent=4)

def load_from_json(filename="output.json"):
    # Load variables from a JSON file into a dictionary.
    with open(filename, "r") as f:
        return json.load(f)

# Example usage
name = "Garrett"
age = 23
skills = ["Software Engineering", "Web Development", "Integration Engineering"]

# Save variables
save_to_json("my_data.json", name=name, age=age, skills=skills)

# Load saved values fromjson created file
data = load_from_json("my_data.json")

# Call from data variable
print(data["name"])     # Garrett
print(data["age"])      # 23
print(data["skills"])   # ['Python', 'Web Dev', 'AI']

# Save data to individual variables
data_name = data["name"]
print(data_name)
data_age = data["age"]
print(data_age)
data_skills = data["skills"]
print(data_skills)