import os
from flask import Flask, request, render_template

def get_project_root() -> str:
    current_directory = os.path.dirname(os.path.abspath(__file__))
    while current_directory != os.path.abspath(os.path.sep):
        if '.project_root_marker' in os.listdir(current_directory):
            return current_directory
        current_directory = os.path.dirname(current_directory)
    return None  # If no marker file is found, return None or raise an exception

project_root = get_project_root()

webpage_template_dir = os.path.join(project_root, 'templates')

app = Flask(__name__, template_folder=webpage_template_dir)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        return render_template("index.html", user_input=user_input)
    return render_template("index.html", user_input="")

if __name__ == "__main__":
    app.run(debug=True)
    
