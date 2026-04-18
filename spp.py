from flask import Flask, render_template ,request

app = Flask(__name__)

# Dictionary with all track info
tracks = {
    "web": {
        "title": "Web Development",
        "description": "Learn how to build websites from scratch, using HTML, CSS, JavaScript, and modern frameworks.",
        "meaning": "Web development is the process of creating websites and web applications that people use online. It covers both the design (front-end) and the functionality (back-end) of websites.",
        "skills": [
    {"name": "HTML & CSS", "desc": "Build and design the structure and style of websites."},
    {"name": "JavaScript", "desc": "Add interactivity and dynamic behavior to websites."},
    {"name": "Frontend Frameworks", "desc": "Use tools like React to build modern UI interfaces."},
    {"name": "Backend Basics", "desc": "Understand how servers, databases, and APIs work."},
    {"name": "Full Stack Development", "desc": "Combine frontend and backend to build complete applications."}
],
"careers": [
    {"name": "Frontend Developer", "desc": "Builds user interfaces of websites and apps."},
    {"name": "Backend Developer", "desc": "Handles servers, databases, and logic behind apps."},
    {"name": "Full Stack Developer", "desc": "Works on both frontend and backend systems."}
],
    
        "recommendations": [
    {
        "name": "freeCodeCamp Web Development Course",
        "url": "https://www.freecodecamp.org/learn/"
    },
    {
        "name": "MDN Web Docs (HTML, CSS, JS Guide)",
        "url": "https://developer.mozilla.org/en-US/docs/Learn"
    },
    {
        "name": "Codecademy HTML/CSS/JS Course",
        "url": "https://www.codecademy.com/catalog/language/html-css"
    }
]
    },
    "uiux": {
        "title": "UI/UX Design",
        "description": "Learn how to design user-friendly interfaces and experiences for websites and apps.",
        "meaning": "UI/UX Design is about creating visually appealing and user-friendly interfaces, ensuring a smooth and enjoyable experience for users.",
        "skills": [
    {"name": "Wireframing", "desc": "Create basic layouts of digital products."},
    {"name": "Prototyping", "desc": "Build interactive mockups of designs."},
    {"name": "Figma", "desc": "Tool used to design modern interfaces."},
    {"name": "User Research", "desc": "Understand user needs and behavior."},
    {"name": "Visual Design", "desc": "Work with colors, typography, and layout."}
],
"careers": [
    {"name": "UI Designer", "desc": "Designs the visual interface of apps and websites."},
    {"name": "UX Designer", "desc": "Improves user experience and usability."},
    {"name": "Product Designer", "desc": "Combines UI + UX to design full products."}
],
       "recommendations": [
    {"name": "Coursera UI/UX Design Specialization",
     "url": "https://www.coursera.org/specializations/ui-ux-design"},

    {"name": "Figma Learn Resources",
     "url": "https://www.figma.com/resources/learn-design/"},

    {"name": "Interaction Design Foundation Courses",
     "url": "https://www.interaction-design.org/courses"}
]
    },
    "cloud": {
        "title": "Cloud Computing",
        "description": "Understand cloud infrastructure, services, and deployment models for modern applications.",
        "meaning": "Cloud computing is the use of remote servers on the internet to store, manage, and process data, instead of using local servers or personal devices.",
        "skills": [
    {"name": "AWS / Azure / GCP", "desc": "Cloud platforms used to host and manage systems."},
    {"name": "Virtual Machines", "desc": "Run computers inside cloud environments."},
    {"name": "Networking Basics", "desc": "Understand how systems connect over the internet."},
    {"name": "DevOps Basics", "desc": "Automate deployment and system updates."},
    {"name": "Cloud Security", "desc": "Protect data and systems in cloud environments."}
],
"careers": [
    {"name": "Cloud Engineer", "desc": "Builds and manages cloud infrastructure."},
    {"name": "DevOps Engineer", "desc": "Automates deployment and system operations."},
    {"name": "Cloud Architect", "desc": "Designs large-scale cloud systems."}
],
     "recommendations": [
    {
        "name": "AWS Cloud Practitioner Essentials",
        "url": "https://aws.amazon.com/training/learn-about/cloud-practitioner/"
    },
    {
        "name": "Microsoft Azure Fundamentals (Learn)",
        "url": "https://learn.microsoft.com/en-us/training/azure/"
    },
    {
        "name": "Google Cloud Training",
        "url": "https://cloud.google.com/training"
    }
]   
        
    },
    "data": {
        "title": "Data Science",
        "description": "Learn how to analyze data and extract meaningful insights from datasets.",
        "meaning": "Data science is the practice of analyzing and interpreting complex data to discover patterns and insights. It combines statistics, programming, and data visualization.",
        "skills": [
    {"name": "Python", "desc": "Main programming language for data analysis."},
    {"name": "Data Analysis", "desc": "Extract insights from raw data."},
    {"name": "Pandas & NumPy", "desc": "Libraries used for data manipulation."},
    {"name": "Data Visualization", "desc": "Represent data using charts and graphs."},
    {"name": "Machine Learning Basics", "desc": "Train models to make predictions."}
],
"careers": [
    {"name": "Data Analyst", "desc": "Analyzes data to help decision making."},
    {"name": "Data Scientist", "desc": "Builds models and extracts insights from data."},
    {"name": "ML Engineer", "desc": "Creates machine learning systems."}
],
      "recommendations": [
    {
        "name": "Coursera Data Science Specialization",
        "url": "https://www.coursera.org/specializations/jhu-data-science"
    },
    {
        "name": "Kaggle Learn",
        "url": "https://www.kaggle.com/learn"
    },
    {
        "name": "DataCamp Python for Data Science",
        "url": "https://www.datacamp.com/tracks/data-scientist-with-python"
    }
]
    },
    "cyber": {
        "title": "Cybersecurity",
        "description": "Learn how to protect systems and networks from cyber threats.",
        "meaning": "Cybersecurity is the field of protecting computers, networks, and data from unauthorized access, attacks, or damage.",
        "skills": [
            {"name": "Network Security", "desc": "Protect networks from attacks and secure data communication."},
            {"name": "Penetration Testing", "desc": "Test systems for vulnerabilities using ethical hacking."},
            {"name": "Threat Analysis", "desc": "Analyze cyber threats to prevent attacks."},
            {"name": "Firewalls & IDS", "desc": "Monitor and block unauthorized access."},
            {"name": "Security Best Practices", "desc": "Apply essential rules to keep systems safe."}
        ],
        "careers": [
            
            {"name": "Cybersecurity Analyst", "desc": "Monitors systems and protects against cyber threats."},
            {"name": "Security Engineer", "desc": "Designs secure systems and infrastructure."},
            {"name": "Ethical Hacker", "desc": "Finds vulnerabilities before attackers do."}

        ],
       "recommendations": [
    {
        "name": "TryHackMe Beginner Path",
        "url": "https://tryhackme.com/path/outline/presecurity"
    },
    {
        "name": "Cisco Networking Academy Security",
        "url": "https://www.netacad.com/courses/cybersecurity"
    },
    {
        "name": "Cybrary Cybersecurity Basics",
        "url": "https://www.cybrary.it/"
    }
]
    },
    "ai": {
        "title": "AI & Machine Learning",
        "description": "Learn how to create intelligent systems using AI and machine learning techniques.",
        "meaning": "Artificial Intelligence and Machine Learning involve creating computer systems that can learn, make decisions, and solve problems like humans.",
        "skills": [
    {"name": "Python Programming", "desc": "Main language used to build AI and machine learning models."},
    {"name": "Machine Learning Algorithms", "desc": "Algorithms that allow systems to learn from data and improve over time."},
    {"name": "Data Preprocessing", "desc": "Cleaning and preparing data before training models."},
    {"name": "Model Training", "desc": "Teaching models to recognize patterns and make predictions."},
    {"name": "Deep Learning Basics", "desc": "Using neural networks to solve complex problems like image and speech recognition."}
],
"careers": [
    {"name": "Machine Learning Engineer", "desc": "Builds and trains AI models for real-world applications."},
    {"name": "AI Developer", "desc": "Creates intelligent systems that simulate human thinking."},
    {"name": "Data Scientist", "desc": "Analyzes data and builds predictive models using AI techniques."}
],
        "recommendations": [
    {
        "name": "Machine Learning by Andrew Ng (Coursera)",
        "url": "https://www.coursera.org/learn/machine-learning"
    },
    {
        "name": "fast.ai Practical Deep Learning",
        "url": "https://www.fast.ai/"
    },
    {
        "name": "TensorFlow Official Tutorials",
        "url": "https://www.tensorflow.org/learn"
    }
] 
    },
    "mobile": {
        "title": "Mobile Development",
        "description": "Build mobile applications for Android and iOS platforms.",
        "meaning": "Mobile development focuses on building applications for smartphones and tablets, ensuring they run smoothly on platforms like Android and iOS.",
        "skills": [
    {"name": "Kotlin / Swift", "desc": "Languages used for Android and iOS apps."},
    {"name": "Flutter", "desc": "Build apps for both platforms using one codebase."},
    {"name": "UI Design", "desc": "Design mobile-friendly interfaces."},
    {"name": "API Integration", "desc": "Connect apps to backend services."},
    {"name": "App Deployment", "desc": "Publish apps to App Store or Play Store."}
],
"careers": [
    {"name": "Android Developer", "desc": "Builds apps for Android devices."},
    {"name": "iOS Developer", "desc": "Builds apps for Apple devices."},
    {"name": "Mobile Developer", "desc": "Develops cross-platform mobile apps."}
],
        
        "recommendations": [
    {
        "name": "Android Kotlin Course (Udemy)",
        "url": "https://www.udemy.com/course/android-kotlin-developer/"
    },
    {
        "name": "Apple Swift Learning",
        "url": "https://developer.apple.com/swift/"
    },
    {
        "name": "Flutter Official Docs",
        "url": "https://flutter.dev/docs"
    }
]
    },
    "it": {
        "title": "IT Support",
        "description": "Learn how to support and maintain computer systems in organizations.",
        "meaning": "IT Support involves maintaining and troubleshooting computer systems, networks, and software to help users work efficiently.",
        "skills": [
    {"name": "Hardware Troubleshooting", "desc": "Fix physical computer issues."},
    {"name": "Software Support", "desc": "Solve software-related problems."},
    {"name": "Networking Basics", "desc": "Understand and fix network issues."},
    {"name": "System Administration", "desc": "Manage computers and systems."},
    {"name": "Customer Support", "desc": "Help users solve technical problems."}
],
"careers": [
    {"name": "IT Support Specialist", "desc": "Helps users with technical issues."},
    {"name": "Help Desk Technician", "desc": "Provides technical assistance."},
    {"name": "System Administrator", "desc": "Manages IT systems and networks."}
],
        "recommendations": [
    {
        "name": "Google IT Support Certificate",
        "url": "https://www.coursera.org/professional-certificates/google-it-support"
    },
    {
        "name": "CompTIA A+ Certification",
        "url": "https://www.comptia.org/certifications/a"
    },
    {
        "name": "Microsoft IT Fundamentals",
        "url": "https://learn.microsoft.com/en-us/certifications/"
    }
]
    },
    "game": {
        "title": "Game Development",
        "description": "Design and build interactive games using modern tools and programming languages.",
        "meaning": "Game development is the process of designing, creating, and testing interactive games for computers, consoles, or mobile devices.",
        "skills": [
    {"name": "Game Design", "desc": "Plan gameplay and mechanics."},
    {"name": "Unity Engine", "desc": "Popular tool for building games."},
    {"name": "C# Programming", "desc": "Used to script game logic."},
    {"name": "3D Modeling", "desc": "Create game characters and environments."},
    {"name": "Problem Solving", "desc": "Fix gameplay and logic issues."}
],
"careers": [
    {"name": "Game Developer", "desc": "Builds video games."},
    {"name": "Game Designer", "desc": "Designs game mechanics and experience."},
    {"name": "Level Designer", "desc": "Creates game levels and environments."}
],
      "recommendations": [
    {
        "name": "Unity Learn Platform",
        "url": "https://learn.unity.com/"
    },
    {
        "name": "Unreal Engine Learning",
        "url": "https://www.unrealengine.com/en-US/onlinelearning-courses"
    },
    {
        "name": "GameDev.tv Courses",
        "url": "https://www.gamedev.tv/"
    }
]
    },
    "iot": {
        "title": "Internet of Things (IoT)",
        "description": "Learn how to connect devices and create smart systems for everyday life.",
        "meaning": "IoT refers to connecting everyday devices to the internet so they can send and receive data, making them smarter and more automated.",
        "skills": [
    {"name": "Sensors", "desc": "Devices that collect data from environment."},
    {"name": "Arduino", "desc": "Microcontroller used for IoT projects."},
    {"name": "Raspberry Pi", "desc": "Mini computer for smart systems."},
    {"name": "Networking", "desc": "Connect devices to the internet."},
    {"name": "Embedded Systems", "desc": "Systems built into smart devices."}
],
"careers": [
    {"name": "IoT Engineer", "desc": "Builds smart connected devices."},
    {"name": "Embedded Engineer", "desc": "Works on hardware-software systems."},
    {"name": "IoT Architect", "desc": "Designs smart systems and networks."}
],
       "recommendations": [
    {
        "name": "Arduino Official Tutorials",
        "url": "https://www.arduino.cc/en/Tutorial/HomePage"
    },
    {
        "name": "Raspberry Pi Learning",
        "url": "https://www.raspberrypi.com/documentation/"
    },
    {
        "name": "Coursera IoT Specialization",
        "url": "https://www.coursera.org/specializations/internet-of-things"
    }
]
    }
}

# Home route
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html") 

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
@app.route("/result", methods=["POST"])
def result():

    answers = [
        request.form.get("q1"),
        request.form.get("q2"),
        request.form.get("q3"),
        request.form.get("q4"),
        request.form.get("q5"),
        request.form.get("q6"),
        request.form.get("q7"),
        request.form.get("q8"),
        request.form.get("q9"),
        request.form.get("q10"),
    ]

    score = {
        "web": 0,
        "uiux": 0,
        "cloud": 0,
        "data": 0,
        "cyber": 0,
        "ai": 0,
        "mobile": 0,
        "it": 0,
        "game": 0,
        "iot": 0
    }

    for a in answers:
        if a in score:
            score[a] += 1

    best_track = max(score, key=score.get)

    return render_template(
        "track.html",
        name=tracks[best_track]["title"],
        description=tracks[best_track]["description"],
        meaning=tracks[best_track]["meaning"],
        skills=tracks[best_track]["skills"],
        careers=tracks[best_track]["careers"],
        recommendations=tracks[best_track]["recommendations"]
    )   

if __name__ == "__main__":
    app.run(debug=True)

    