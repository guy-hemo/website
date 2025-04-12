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
        "image": "img/portfolio.png"  # Corrected path relative to static
    },
    {
        "id": 2,
        "title": "Data Analysis Dashboard",
        "description": "A dashboard visualizing sales data using Python libraries.",
        "technologies": ["Django", "Pandas", "Matplotlib", "Seaborn"],
        "live_demo": None,
        "github": "https://github-activity-graph.vercel.app/graph?username=guy-hemo&theme=github-compact",
        "image": "img/dashboard.png"  # Corrected path relative to static
    },
    # Add more projects here
]
skills = [
    {"name": "Python", "level": 90},
    {"name": "Flask", "level": 85},
    {"name": "AWS", "level": 75},
    {"name": "Docker", "level": 80},
    {"name": "Kubernetes", "level": 95},
    {"name": "Terraform", "level": 90},
    {"name": "Ansible", "level": 80},
    {"name": "Jenkins", "level": 90},
    {"name": "Git", "level": 90},
    {"name": "PowerShell", "level": 90},
    {"name": "Bash", "level": 90},
    {"name": "Groov", "level": 90},
    {"name": "Elaseticsearch", "level": 90},
    {"name": "Kibana", "level": 90},
    {"name": "Prometheus", "level": 90},
    {"name": "Grafana", "level": 90},
    {"name": "CloudFlare", "level": 90},
    {"name": "Networking", "level": 90},
    {"name": "MySQL", "level": 90},
    {"name": "PostreSQL", "level": 90},
    {"name": "MongoDB", "level": 90},
    {"name": "Windows", "level": 90},
    {"name": "Linux", "level": 90},
    # Add more skills
]
experience = [
    {
        "title": "DevOps",
        "company": "Leverate",
        "years": "2023 TO PRESENT",
        "description": "Designed and maintained CI/CD pipelines in Jenkins,reducing deployment time by 30%. Build and manage Docker containers for microservicesarchitecture.Administer Kubernetes (EKS) environments, handlingPods, PVCs, and Service configurations. Automate infrastructure tasks using Ansible andTerraform.Manage AWS cloud services, including EC2, S3, IAM, andAuto Scaling.Implement monitoring solutions with ELK, Prometheus,and CloudTrail.Enhance security through CloudFlare, TLS encryption, and DDoS mitigation."
    },
    {
        "title": "DevOps",
        "company": "Ministry of Health",
        "years": "2021 TO 2023",
        "description": "Managed Linux and Windows-based environments,ensuring optimal uptime and performance.Deployed and maintained Kubernetes (EKS)workloads and Docker images.Automated operational processes using Bash,Python, and PowerShell.Monitored infrastructure using SCOM, Kibana,vROps, and Grafana.Configured F5 and NGINX load balancers forapplication traffic management.Administered network protocols, including TCP,UDP, SSH, and FTP.Integrated LDAP and SSO authentication for secureaccess control."
    },
    {
        "title": "System Administrator",
        "company": "Kan 11 Local TV",
        "years": "2019 TO 2020",
        "description": "Managed a hybrid infrastructure of Linux andWindows servers (300-500 machines).Configured and maintained VMware vSphereenvironments for optimal performance.Provided Linux-based server support (Ubuntu,CentOS) and troubleshooting.Secured network environments with Cisco switches,VLANs, and firewalls (Fortigate, Checkpoint).Automated administrative tasks with PowerShell and Bash scripting.Deployed enterprise software solutions to supportbroadcast operations."
    },
    {
        "title": "System Administrator",
        "company": "Intel Corp",
        "years": "2017 TO 2019",
        "description": "Oversaw a high-scale environment with 1000+ Linux and Windows servers. Created and maintained VMware-based infrastructure and automated provisioning. Developed PowerShell scripts for server automation and maintenance. Managed Linux package repositories and troubleshooting. Configured and optimized NGINX, load balancers, and network protocols. Collaborated with the NoC team for incident management and monitoring alert response."
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