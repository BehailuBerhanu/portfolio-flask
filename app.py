from flask import Flask, render_template, request, flash, redirect, url_for


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages


student = {
    "name": "Behailu",
    "role": "Python Developer",
    "bio": "Python Developer & UI Designer. 🚀 I build high-performance web applications using Flask and Python, wrapped in responsive Bootstrap layouts and designed with a meticulous eye for UI/UX.",
    "skills": ["Python", "Flask", "HTML/CSS", "UI Design", "bootstrap", "figma"],
    "email": "behailuberhanu2025@gmail.com",
    "github": "https://github.com/BehailuBerhanu",
    "projects": [
        {
            "title": "Libray Management System",
            "description": "A web application to manage library resources, including book inventory, user accounts, and borrowing history.",
            "tech": ["python", "OOP", "JSON"],
            "github": "https://github.com/BehailuBerhanu/SLMS"
        },
        
        {
            "title": "Professional Portfolio",
            "description": "A modern, responsive personal portfolio built to showcase my development and design work. Features a dark-themed UI, custom CSS animations, and a Flask-powered backend.",
            "tech": ["Python", "Flask", "Bootstrap", "UI Design"],
            "github": "https://github.com/BehailuBerhanu/portfolio-flask" 
        },
    ]
}

#Routing
@app.route("/")
def home():
    return render_template("index.html", student=student)

@app.route("/projects")
def projects():
    return render_template("projects.html", student=student)

@app.route("/contact")
def show_contact():
    return render_template("contact.html", student=student)

@app.route("/contact/submit", methods=["POST"])
def contact():
    name = request.form["name"]
    message = request.form["message"]
    # Process the contact form data (e.g., send an email, save to database)
    print(f"Message from {name}: {message}")
    flash("Thank you for your message! We will get back to you soon.", "success")

    return redirect(url_for("show_contact"))

@app.route("/learning")
def learning():
    return render_template("learning.html", student=student)

# RUN
if __name__ == "__main__":
    app.run(debug=True)