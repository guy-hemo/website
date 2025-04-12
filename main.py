from flask import Flask, render_template, request
import datetime
import random
import json

app = Flask(__name__)

# --- Data Store (Simple In-Memory for Demonstration) ---
visitors = {}
projects = [
    {
        "id": 1,
        "title": "Personal Portfolio Website",
        "description": "A responsive website showcasing my skills, projects, and resume.",
        "technologies": ["Flask", "HTML", "CSS", "JavaScript"],
        "live_demo": "https://your-portfolio-url.com",
        "github": "https://github.com/guy-hemo/guy-hemo",
        "image": "static/img/portfolio.png"  # Add placeholder image
    },
    {
        "id": 2,
        "title": "Data Analysis Dashboard",
        "description": "A dashboard visualizing sales data using Python libraries.",
        "technologies": ["Django", "Pandas", "Matplotlib", "Seaborn"],
        "live_demo": None,
        "github": "https://github-activity-graph.vercel.app/graph?username=guy-hemo&theme=github-compact",
        "image": "static/img/dashboard.png"  # Add placeholder image
    },
    # Add more projects here
]
skills = [
    {"name": "Python", "level": 90},
    {"name": "Flask", "level": 85},
    {"name": "Django", "level": 75},
    {"name": "JavaScript", "level": 80},
    {"name": "HTML", "level": 95},
    {"name": "CSS", "level": 90},
    {"name": "SQL", "level": 80},
    {"name": "Git", "level": 90},
    # Add more skills
]
testimonials = [
    {"name": "John Doe", "title": "Manager at Tech Inc.", "quote": "Exceptional problem-solving skills and a strong understanding of web development."},
    {"name": "Jane Smith", "title": "Team Lead at Software Ltd.", "quote": "A highly motivated and quick learner with excellent communication skills."},
    # Add more testimonials
]
experience = [
    {
        "title": "Software Engineer Intern",
        "company": "Acme Corp",
        "years": "Summer 2024",
        "description": "Developed and maintained features for the company's flagship product using Python and Django."
    },
    {
        "title": "Freelance Web Developer",
        "company": "Self-Employed",
        "years": "2023 - Present",
        "description": "Designed and built responsive websites for various clients using Flask and front-end technologies."
    },
    # Add more experience
]

# --- Helper Functions ---
def get_visitor_count():
    return len(visitors)

def record_visitor():
    ip_address = request.remote_addr
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    visitors[ip_address] = timestamp

# --- Routes ---
@app.route('/')
def index():
    record_visitor()
    return render_template('index.html',
                           visitor_count=get_visitor_count(),
                           projects=projects,
                           skills=skills,
                           testimonials=testimonials,
                           experience=experience,
                           datetime=datetime)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    if project:
        return render_template('project_detail.html', project=project)
    return render_template('404.html'), 404

@app.route('/skills')
def skills_page():
    return render_template('skills.html', skills=skills, datetime=datetime)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # In a real application, you would send this data via email
        print(f"New message from: {name} <{email}> - {message}")
        return render_template('contact_success.html', name=name, datetime=datetime)
    return render_template('contact.html', datetime=datetime)

@app.route('/admin/stats')
def admin_stats():
    # Basic authentication for demonstration purposes - DO NOT USE IN PRODUCTION
    auth = request.authorization
    if not auth or not (auth.username == 'admin' and auth.password == 'password123'):
        return 'Authentication required!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'}
    return render_template('admin_stats.html', visitor_count=get_visitor_count(), visitors=visitors)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
