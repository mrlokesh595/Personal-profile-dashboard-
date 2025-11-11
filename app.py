from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    user = {
        "name": "John Doe",
        "bio": "Software Developer passionate about AI, Web Development, and Open Source.",
        "skills": ["Python", "Flask", "React", "Machine Learning"],
        "email": "john@example.com",
        "location": "New York, USA",
        "profile_pic": "https://via.placeholder.com/150"
    }
    return render_template("index.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)
