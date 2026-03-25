from flask import Flask, render_template

app = Flask(__name__)

# CV Data
cv_data = {
    "name": "RUCHIT DONGA",
    "title": "Backend Developer | Django • REST APIs • AI Integration",
    "email": "ruchitdonga@gmail.com",
    "linkedin": "www.linkedin.com/in/ruchit-donga",
    "github": "https://github.com/ruchitdonga",
    "phone": "+91-8976767976",
    "location": "India",
    "summary": "Backend-focused software developer specializing in Django and REST API architecture with experience building AI-integrated systems. Strong emphasis on structured backend design, API contracts, and scalable service architecture. Experienced working in collaborative environments alongside frontend and ML engineers to deliver production-ready applications.",
    "skills": {
        "Languages": ["Python", "Java", "SQL", "JavaScript (basic)"],
        "Backend": ["Django", "Django REST Framework (DRF)", "REST API Design"],
        "AI/Data": ["ML integration workflows", "Rule-based decision systems", "Local LLM integration concepts"],
        "Web": ["HTML", "CSS", "Flask (basic full-stack apps)"],
        "Big Data": ["Hadoop", "HDFS", "MapReduce", "Hive"],
        "Tools": ["Git", "GitHub", "Swagger/OpenAPI", "Docker (basic)", "VS Code"],
        "Databases": ["SQLite", "PostgreSQL (conceptual)"],
        "Environment": ["Windows", "Linux CLI", "Miniconda"]
    },
    "projects": [
        {
            "name": "AI-Based Crop Recommendation System",
            "role": "Backend Architect",
            "tech": ["Django", "DRF", "Python", "Swagger"],
            "description": [
                "Designed scalable backend architecture for AI-powered crop prediction.",
                "Built high-performance REST APIs tailored for ML model integration.",
                "Implemented robust rule-based decision engine as a fallback mechanism.",
                "Established strict API contracts ensuring seamless frontend-backend communication."
            ],
                "live": "https://ai-crop-advisor-three.vercel.app",
            "highlight": True
        },
        
        {
            "name": "Construction Site Material Tracker",
            "role": "Full-Stack Developer",
            "tech": ["Flask", "SQLite", "JavaScript", "Bootstrap"],
            "description": [
                "Built an inventory and materials tracking system for construction sites.",
                "Implemented CRUD workflows for materials, suppliers, and site assignments.",
                "Added reporting and low-stock alerts to streamline procurement."
            ],
            "live": "https://sahajajanand.firebaseapp.com/",
            "highlight": False
        }
    ],
    "experience": [
        {
            "company": "Cognifyz Technologies",
            "role": "Machine Learning Intern",
            "duration": "(July 2024 – July 2024)",
            "details": [
                "Worked on machine learning workflows including data preprocessing, feature engineering, and model experimentation.",
                "Built and evaluated ML models using Python libraries.",
                "Cleaned and analyzed datasets to improve model performance and accuracy.",
                "Gained hands-on exposure to real-world ML project pipelines and collaboration practices."
            ]
        }
    ],
    "education": [
        {
            "degree": "Bachelor’s Degree in Computer Science / IT",
            "institution": "Atlas SkillTech University",
            "year": "Expected Graduation: 2028"
        }
    ],
    "certificates": [
        "Goldman Sachs — Software Engineering Job Simulation Certificate",
        "MyCaptain — C++ Programming Course Certificate",
        "Big Data Analytics (Hadoop & MapReduce)",
        "Backend Development with Django REST Framework"
    ],
    "strengths": [
        "Backend system design and API structuring",
        "Clear separation between backend, ML, and frontend responsibilities",
        "Problem decomposition and structured development workflow",
        "Strong debugging and integration skills"
    ]
}

@app.route('/')
def home():
    return render_template('index.html', cv=cv_data)


@app.route('/contact')
def contact():
    return render_template('contact.html', cv=cv_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
