from flask import Flask, render_template

app = Flask(__name__)

# Dictionary with all track info
tracks = {
    "web": {
        "title": "Web Development",
        "description": "Learn how to build websites from scratch, using HTML, CSS, JavaScript, and modern frameworks.",
        "meaning": "Web development is the process of creating websites and web applications that people use online. It covers both the design (front-end) and the functionality (back-end) of websites.",
        "skills": [
            "HTML & CSS",
            "JavaScript",
            "Front-End Frameworks",
            "Back-End Basics",
            "Full-Stack Development"
        ],
        "careers": [
            "Front-End Developer",
            "Back-End Developer",
            "Full-Stack Developer"
        ],
        "recommendations" :[
            "freecodecamp web development course",
            "Codecademy HTML/CSS/JS",
        "MDN Web Docs Tutorials"
        ]
    },
    "uiux": {
        "title": "UI/UX Design",
        "description": "Learn how to design user-friendly interfaces and experiences for websites and apps.",
        "meaning": "UI/UX Design is about creating visually appealing and user-friendly interfaces, ensuring a smooth and enjoyable experience for users.",
        "skills": [
            "Wireframing & Prototyping",
            "User Research",
            "Adobe XD / Figma",
            "Visual Design Principles",
            "Usability Testing"
        ],
        "careers": [
            "UI Designer",
            "UX Designer",
            "Product Designer"
        ],
        "recommendations": [
        "Coursera UI/UX Design Specialization",
        "Figma Learn Resources",
        "Interaction Design Foundation Courses"
    ]
    },
    "cloud": {
        "title": "Cloud Computing",
        "description": "Understand cloud infrastructure, services, and deployment models for modern applications.",
        "meaning": "Cloud computing is the use of remote servers on the internet to store, manage, and process data, instead of using local servers or personal devices.",
        "skills": [
            "AWS / Azure / GCP",
            "Virtualization",
            "Containers & Kubernetes",
            "Serverless Architecture",
            "Cloud Security Basics"
        ],
        "careers": [
            "Cloud Engineer",
            "DevOps Engineer",
            "Cloud Solutions Architect"
        ],
        "recommendations": [
        "AWS Training & Certification",
        "Microsoft Learn Azure Fundamentals",
        "Google Cloud Training"
    ]
    },
    "data": {
        "title": "Data Science",
        "description": "Learn how to analyze data and extract meaningful insights from datasets.",
        "meaning": "Data science is the practice of analyzing and interpreting complex data to discover patterns and insights. It combines statistics, programming, and data visualization.",
        "skills": [
            "Python Programming",
            "Data Analysis",
            "Pandas & NumPy",
            "Data Visualization",
            "Machine Learning Basics"
        ],
        "careers": [
            "Data Analyst",
            "Data Scientist",
            "Machine Learning Engineer"
        ],
          "recommendations": [
        "Coursera Data Science Specialization",
        "Kaggle Learn Python & Data Analysis",
        "DataCamp Data Science Courses"
    ]
    },
    "cyber": {
        "title": "Cybersecurity",
        "description": "Learn how to protect systems and networks from cyber threats.",
        "meaning": "Cybersecurity is the field of protecting computers, networks, and data from unauthorized access, attacks, or damage.",
        "skills": [
            "Network Security",
            "Penetration Testing",
            "Threat Analysis",
            "Firewalls & IDS",
            "Security Best Practices"
        ],
        "careers": [
            "Cybersecurity Analyst",
            "Security Engineer",
            "Ethical Hacker"
        ],
         "recommendations": [
        "Cybrary Cybersecurity Fundamentals",
        "TryHackMe Beginner Paths",
        "Cisco Networking Academy Security Courses"
    ]
    },
    "ai": {
        "title": "AI & Machine Learning",
        "description": "Learn how to create intelligent systems using AI and machine learning techniques.",
        "meaning": "Artificial Intelligence and Machine Learning involve creating computer systems that can learn, make decisions, and solve problems like humans.",
        "skills": [
            "Machine Learning Algorithms",
            "Python & Libraries (Scikit-Learn, TensorFlow)",
            "Data Preprocessing",
            "Model Training & Evaluation",
            "AI Problem Solving"
        ],
        "careers": [
            "Machine Learning Engineer",
            "AI Developer",
            "Data Scientist"
        ],
         "recommendations": [
        "Coursera Machine Learning by Andrew Ng",
        "fast.ai Practical Deep Learning",
        "TensorFlow Official Tutorials"
    ]
    },
    "mobile": {
        "title": "Mobile Development",
        "description": "Build mobile applications for Android and iOS platforms.",
        "meaning": "Mobile development focuses on building applications for smartphones and tablets, ensuring they run smoothly on platforms like Android and iOS.",
        "skills": [
            "Kotlin / Java (Android)",
            "Swift (iOS)",
            "Flutter / React Native",
            "Mobile UI Design",
            "App Deployment"
        ],
        "careers": [
            "Android Developer",
            "iOS Developer",
            "Mobile App Developer"
        ],
         "recommendations": [
        "Udemy Android Development with Kotlin",
        "Udemy iOS Development with Swift",
        "Flutter & React Native Official Docs"
    ]
    },
    "it": {
        "title": "IT Support",
        "description": "Learn how to support and maintain computer systems in organizations.",
        "meaning": "IT Support involves maintaining and troubleshooting computer systems, networks, and software to help users work efficiently.",
        "skills": [
            "Hardware & Software Troubleshooting",
            "Network Support",
            "System Administration",
            "Help Desk Skills",
            "IT Customer Support"
        ],
        "careers": [
            "IT Support Specialist",
            "Help Desk Technician",
            "System Administrator"
        ],
         "recommendations": [
        "Google IT Support Professional Certificate",
        "CompTIA A+ Certification Training",
        "Microsoft Learn IT Fundamentals"
    ]
    },
    "game": {
        "title": "Game Development",
        "description": "Design and build interactive games using modern tools and programming languages.",
        "meaning": "Game development is the process of designing, creating, and testing interactive games for computers, consoles, or mobile devices.",
        "skills": [
            "Game Design Fundamentals",
            "Unity / Unreal Engine",
            "C# Programming",
            "2D & 3D Game Development",
            "Problem Solving & Logic"
        ],
        "careers": [
            "Game Developer",
            "Game Designer",
            "Level Designer",
            "AR/VR Developer"
        ],
         "recommendations": [
        "Unity Learn Platform",
        "Unreal Engine Online Learning",
        "Udemy Game Development Courses"
    ]
    },
    "iot": {
        "title": "Internet of Things (IoT)",
        "description": "Learn how to connect devices and create smart systems for everyday life.",
        "meaning": "IoT refers to connecting everyday devices to the internet so they can send and receive data, making them smarter and more automated.",
        "skills": [
            "Sensors & Microcontrollers",
            "Arduino / Raspberry Pi",
            "Networking Basics",
            "IoT Protocols",
            "Embedded Systems"
        ],
        "careers": [
            "IoT Engineer",
            "Embedded Systems Engineer",
            "IoT Solutions Architect"
        ],
        "recommendations": [
        "Arduino Official Tutorials",
        "Raspberry Pi Learning Resources",
        "Coursera IoT Specialization"
    ]
    }
}

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Track route
@app.route("/track/<name>")
def track(name):
    if name in tracks:
        return render_template(
            "track.html",
            name=tracks[name]["title"],
            description=tracks[name]["description"],
             meaning=tracks[name]["meaning"],
            skills=tracks[name]["skills"],
            careers=tracks[name]["careers"],
             recommendations=tracks[name]["recommendations"],
        )
        
    else:
        return "Track not found"

if __name__ == "__main__":
    app.run(debug=True)