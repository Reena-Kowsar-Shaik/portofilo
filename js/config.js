/**
 * PORTFOLIO CONFIGURATION DATA
 * SHAIK REENA KOWSAR — Python Full Stack Developer & AI/ML Engineer
 */

const PORTFOLIO_DATA = {
  // Personal Info
  personal: {
    name: "Shaik Reena Kowsar",
    preferredName: "Reena",
    role: "Python Full Stack Developer & AI/ML Engineer",
    tagline: "B.Tech CSE (AI & ML) graduate from Bapatla Engineering College (CGPA: 9.1/10). Building end-to-end database-driven web applications, RAG multimodal systems, and intelligent analytics dashboards.",
    typingRoles: [
      "Python Full Stack Developer",
      "AI / ML & LLM Engineer",
      "RAG & Multimodal Systems Builder",
      "Streamlit & Django/Flask Developer",
      "Database & Analytics Specialist"
    ],
    status: {
      available: true,
      text: "Actively seeking Python Full Stack Developer & AI/ML Engineer Roles (Batch 2022–2026)"
    },
    location: "Hyderabad, Telangana, India",
    email: "reenakowsar05@gmail.com",
    phone: "+91 8639214710",
    avatar: "assets/reena_photo.jpeg",
    bio: [
      "I am a B.Tech Computer Science and Engineering (AI & ML) student at Bapatla Engineering College with an outstanding CGPA of 9.1/10 and recipient of the Academic Shield of Excellence.",
      "As a Python Full Stack trainee and AI/ML enthusiast, I build complete, database-driven applications featuring role-based authentication, relational schemas, REST-style workflows, and analytics dashboards. I have designed and deployed live production applications including an IT Helpdesk & Support Intelligence System and Smart Memory Vault (Multimodal RAG)."
    ],
    stats: [
      { label: "B.Tech CGPA", value: "9.1 / 10", number: 9.1 },
      { label: "Class XII & X", value: "96%", number: 96 },
      { label: "LeetCode & DSA", value: "100+ Solved", number: 100 },
      { label: "HackerRank", value: "4-Star Python", number: 4 }
    ]
  },

  // Separate Resume Download Options
  resumes: [
    {
      title: "Comprehensive Resume",
      subtitle: "Full technical resume with detailed projects, internships, RAG architectures, and academic metrics",
      format: "PDF (Full CV)",
      fileSize: "185 KB",
      icon: "file-text",
      downloadUrl: "assets/Shaik_Reena_Kowsar_Resume.pdf",
      fileName: "Shaik_Reena_Kowsar_Resume.pdf",
      isPrimary: true
    },
    {
      title: "ATS-Optimized 1-Page Resume",
      subtitle: "Single-page machine-readable resume calibrated for automated Applicant Tracking Systems",
      format: "PDF (1-Page ATS)",
      fileSize: "140 KB",
      icon: "check-circle-2",
      downloadUrl: "assets/Shaik_Reena_Kowsar_ATS_Resume.pdf",
      fileName: "Shaik_Reena_Kowsar_ATS_Resume.pdf",
      isPrimary: false
    },
    {
      title: "Academic & Certification Dossier",
      subtitle: "Includes college ranking, Bapatla Engineering College credentials, and IBM/Cisco certifications",
      format: "PDF (Academic)",
      fileSize: "210 KB",
      icon: "graduation-cap",
      downloadUrl: "assets/Shaik_Reena_Kowsar_Academic_Profile.pdf",
      fileName: "Shaik_Reena_Kowsar_Academic_Profile.pdf",
      isPrimary: false
    }
  ],

  // Academic Education (From Resume)
  education: [
    {
      degree: "B.Tech, Computer Science and Engineering (AI & ML)",
      institution: "Bapatla Engineering College",
      duration: "2022 – 2026",
      location: "Andhra Pradesh / Telangana, India",
      grade: "CGPA: 9.1 / 10",
      highlight: "Academic Excellence Shield • Outstanding Performance",
      courseworkHeading: "Core Competencies & AI/ML Coursework:",
      coursework: [
        "Artificial Intelligence & Machine Learning",
        "Natural Language Processing (NLP)",
        "Retrieval-Augmented Generation (RAG)",
        "Data Structures & Algorithms",
        "Database Management Systems (MySQL/PostgreSQL)",
        "Object-Oriented Programming (Python)",
        "Computer Vision & CNN",
        "REST APIs & Web Architectures",
        "Operating Systems & Computer Networks"
      ]
    },
    {
      degree: "Intermediate (Class XII)",
      institution: "Narayana Junior College",
      duration: "2020 – 2022",
      location: "India",
      grade: "Score: 96%",
      highlight: "State Board Merit",
      coursework: ["Mathematics", "Physics", "Chemistry"]
    },
    {
      degree: "Secondary School Certificate (Class X)",
      institution: "Z.P. High School",
      duration: "Passed 2020",
      location: "India",
      grade: "Score: 96%",
      highlight: "School Topper",
      coursework: ["General Sciences", "Mathematics", "Social Studies"]
    }
  ],

  // Projects (From Resume)
  projects: [
    {
      id: "project-1",
      title: "Smart Memory Vault: AI-Powered Multimodal Knowledge System",
      subtitle: "RAG & LLM multimodal document intelligence platform",
      category: "ai",
      featured: true,
      image: "assets/smart_memory_vault_mockup.svg",
      tags: ["Python", "Streamlit", "PostgreSQL", "SQLAlchemy", "RAG", "NLP", "OCR", "Bcrypt"],
      demoUrl: "https://example.com/demo",
      githubUrl: "https://github.com",
      description: "An AI-powered multimodal knowledge management platform that ingests and processes PDFs, images via OCR, YouTube video transcripts, and audio notes supporting 50+ documents and 300+ text chunks.",
      highlights: [
        "Implemented hybrid TF-IDF and embedding-based retrieval using cosine similarity, source citations, and confidence scoring, achieving 91% top-3 accuracy across 50+ test queries.",
        "Engineered NLP features (summarization, sentiment analysis, flashcards, quizzes) with NLTK and Scikit-learn.",
        "Integrated secure Bcrypt authentication and deployed live on Streamlit Cloud for 25+ users with a 1.2s average response time."
      ],
      caseStudy: {
        challenge: "Handling unstructured data across multiple modalities (text, scanned PDF OCR, audio transcripts) with fast, hallucination-free retrieval.",
        solution: "Engineered a hybrid retrieval pipeline pairing semantic dense embeddings with lexical TF-IDF matching, providing direct source citation snippets and confidence scoring.",
        results: "91% top-3 retrieval accuracy, sub-1.2s response latency, deployed live on Streamlit Cloud for 25+ active users."
      }
    },
    {
      id: "project-2",
      title: "IT Helpdesk & Support Intelligence System",
      subtitle: "Full stack ticketing platform with automated SLA tracking & analytics",
      category: "fullstack",
      featured: true,
      image: "assets/it_helpdesk_mockup.svg",
      tags: ["Python", "Streamlit", "SQLAlchemy", "MySQL", "Plotly", "Pandas", "Bcrypt"],
      demoUrl: "https://example.com/demo",
      githubUrl: "https://github.com",
      description: "A complete, production-grade IT support ticketing platform featuring role-based access control (RBAC), workload-aware ticket distribution, and interactive executive analytics dashboards.",
      highlights: [
        "Designed an 11-table normalized relational MySQL schema with SQLAlchemy ORM.",
        "Implemented automated SLA tracking algorithms and workload-aware assignment to balance team capacity and proactively flag SLA breaches.",
        "Built interactive Plotly and Pandas dashboards for real-time ticket status monitoring, resolution compliance, and support KPIs."
      ],
      caseStudy: {
        challenge: "Legacy ticketing systems suffered from unfair engineer workload distribution and delayed SLA breach detection.",
        solution: "Architected an 11-table relational schema with SQLAlchemy ORM coupled with an automated workload-balancing queue algorithm.",
        results: "Zero unassigned ticket bottlenecks, proactive SLA alerts, and full visibility through real-time Plotly executive dashboards."
      }
    },
    {
      id: "project-3",
      title: "IntelliCode: AI-Powered Code Reviewer & Bug Analyzer",
      subtitle: "Automated static AST analysis, vulnerability detection & LLM refactoring engine",
      category: "ai",
      featured: true,
      image: "assets/ai_code_reviewer_mockup.svg",
      tags: ["Python", "Streamlit", "Gemini API", "AST", "Static Analysis", "Pylint", "SQLAlchemy"],
      demoUrl: "https://example.com/demo",
      githubUrl: "https://github.com",
      description: "An intelligent automated code review tool that analyzes code submissions, detects syntax bugs, security vulnerabilities (SQL injections, unsafe eval), performance bottlenecks, and generates optimized PEP 8 refactorings with time complexity metrics.",
      highlights: [
        "Integrated Python Abstract Syntax Tree (AST) parsing with Gemini API to inspect code quality, detect security antipatterns, and calculate cyclomatic complexity.",
        "Provided interactive side-by-side diff comparisons with line-by-line recommendations and automatic unit test generation.",
        "Built a responsive Streamlit UI supporting Python, SQL, and JavaScript with instantaneous feedback delivered in under 1.8s."
      ],
      caseStudy: {
        challenge: "Manual code reviews in fast-paced development cycles cause delayed feedback loops and allow edge-case security bugs to escape into production.",
        solution: "Engineered a hybrid analysis engine: deterministic static AST linting to flag code antipatterns combined with Gemini LLM reasoning for architectural optimization.",
        results: "95%+ precision on common security flaws, reducing developer debugging iterations by over 65% with sub-2s analysis turnaround."
      }
    }
  ],

  // Internships (From Resume)
  internships: [
    {
      period: "Jun 2025 – Jul 2025",
      role: "AI/ML Intern",
      company: "IBM SkillsBuild",
      location: "Virtual / Hybrid",
      highlights: [
        "Preprocessed diverse datasets with Python and Scikit-learn, covering data cleaning, missing-value handling, and feature preparation.",
        "Trained and evaluated supervised and unsupervised models using accuracy, precision, recall, and F1-score, benchmarking performance across algorithms."
      ]
    },
    {
      period: "Jan 2025 – Mar 2025",
      role: "Python Intern",
      company: "VaultofCodes",
      location: "Virtual / Hybrid",
      highlights: [
        "Developed modular Python scripts for file handling, data processing, and task automation utilizing functions and object-oriented programming (OOP).",
        "Debugged programs, validated inputs, and handled runtime errors, substantially improving overall code reliability."
      ]
    }
  ],

  // Technical Skills (Categorized from Resume)
  skillCategories: [
    {
      name: "Programming Languages",
      skills: ["Python", "C", "SQL", "JavaScript", "HTML5", "CSS3"]
    },
    {
      name: "AI, GenAI & Data Science",
      skills: ["Generative AI (Gemini API)", "RAG (Retrieval-Augmented Generation)", "LLM Applications", "NLP", "Machine Learning", "Scikit-Learn", "NLTK", "OpenCV", "CNN", "Embeddings"]
    },
    {
      name: "Backend, Web & APIs",
      skills: ["REST APIs", "Streamlit", "Django", "Flask", "SQLAlchemy ORM", "Bcrypt Authentication"]
    },
    {
      name: "Databases & Storage",
      skills: ["MySQL (Relational Schemas)", "PostgreSQL", "Database Design", "SQL Queries"]
    },
    {
      name: "Developer Tools & Libraries",
      skills: ["Git & GitHub", "Jupyter Notebook", "Google Colab", "Pandas", "Plotly", "NumPy"]
    }
  ],

  // Certifications (From Resume)
  certifications: [
    {
      title: "Python Essentials",
      issuer: "Cisco Networking Academy",
      icon: "code"
    },
    {
      title: "AI Fundamentals",
      issuer: "IBM SkillsBuild",
      icon: "sparkles"
    },
    {
      title: "Introduction to AI & ML Fundamentals",
      issuer: "Infosys Springboard",
      icon: "cpu"
    },
    {
      title: "Python Programming",
      issuer: "HackerRank",
      icon: "terminal"
    }
  ],

  // Key Achievements (From Resume)
  achievements: [
    {
      title: "Academic Shield of Excellence & College Honors",
      description: "Received a prestigious shield for academic excellence at Bapatla Engineering College with an outstanding 9.1/10 CGPA.",
      icon: "award"
    },
    {
      title: "4-Star Python on HackerRank & 100+ LeetCode Solved",
      description: "Demonstrated strong algorithmic problem solving by achieving a 4-star Python badge on HackerRank and solving 100+ Data Structures & Algorithms problems on LeetCode.",
      icon: "star"
    },
    {
      title: "Technical Presentations & College Tech Events",
      description: "Actively presented technical papers on AI/ML applications and participated in state-level coding and innovation symposiums.",
      icon: "presentation"
    }
  ],

  // Social & Professional Profiles (From Resume)
  socials: [
    { name: "LinkedIn", url: "https://linkedin.com", icon: "linkedin" },
    { name: "GitHub", url: "https://github.com", icon: "github" },
    { name: "LeetCode", url: "https://leetcode.com", icon: "code-2" },
    { name: "HackerRank", url: "https://hackerrank.com", icon: "terminal" },
    { name: "Email", url: "mailto:reenakowsar05@gmail.com", icon: "mail" }
  ]
};
