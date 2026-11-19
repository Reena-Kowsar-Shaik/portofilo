import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def build_pdf(filename, title_tag="COMPREHENSIVE RESUME"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0f172a'),
        alignment=1 # Center
    )

    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#334155'),
        alignment=1 # Center
    )

    sec_title = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=3,
        spaceBefore=8
    )

    body = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#1e293b')
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#0f172a')
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=body,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=2
    )

    elements = []

    # Header
    elements.append(Paragraph("SHAIK REENA KOWSAR", name_style))
    elements.append(Paragraph("Hyderabad, Telangana, India &nbsp;|&nbsp; +91 8639214710 &nbsp;|&nbsp; reenakowsar05@gmail.com", contact_style))
    elements.append(Paragraph("<b>LinkedIn:</b> linkedin.com &nbsp;|&nbsp; <b>GitHub:</b> github.com &nbsp;|&nbsp; <b>LeetCode:</b> leetcode.com &nbsp;|&nbsp; <b>HackerRank:</b> hackerrank.com", contact_style))
    elements.append(Spacer(1, 4))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#475569'), spaceBefore=2, spaceAfter=6))

    # Career Objective
    elements.append(Paragraph("CAREER OBJECTIVE", sec_title))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cbd5e1'), spaceBefore=1, spaceAfter=4))
    elements.append(Paragraph(
        "B.Tech CSE graduate (AI & ML) and Python Full Stack trainee who builds complete, database-driven applications with role-based authentication, relational schemas, REST-style workflows, and analytics dashboards, backed by hands-on AI/ML experience in RAG, NLP, Scikit-learn, and OCR. Deployed live applications using Python, Streamlit, SQLAlchemy, MySQL, and PostgreSQL. Seeking Python Full Stack Developer and AI/ML Engineer roles in a product-driven team.",
        body
    ))
    elements.append(Spacer(1, 4))

    # Technical Skills
    elements.append(Paragraph("TECHNICAL SKILLS", sec_title))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cbd5e1'), spaceBefore=1, spaceAfter=4))
    skills_text = (
        "<b>Languages:</b> Python, C, SQL, JavaScript, HTML, CSS<br/>"
        "<b>AI / LLM:</b> Generative AI (Gemini API), LLM Applications, RAG (Retrieval-Augmented Generation), Embeddings, NLP, Machine Learning, Scikit-learn, NLTK, OpenCV, CNN<br/>"
        "<b>Backend & APIs:</b> REST APIs, Django, Flask, Streamlit, SQLAlchemy ORM, Bcrypt Authentication<br/>"
        "<b>Databases:</b> MySQL (Relational Schemas), PostgreSQL<br/>"
        "<b>Tools & Libraries:</b> Git, GitHub, Jupyter Notebook, Google Colab, Pandas, Plotly, NumPy, AST"
    )
    elements.append(Paragraph(skills_text, body))
    elements.append(Spacer(1, 4))

    # Projects
    elements.append(Paragraph("PROJECTS", sec_title))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cbd5e1'), spaceBefore=1, spaceAfter=4))
    
    # Project 1: IT Helpdesk
    elements.append(Paragraph("<b>IT Helpdesk & Support Intelligence System</b> &nbsp;|&nbsp; <i>Python, Streamlit, SQLAlchemy, MySQL, Plotly, Pandas, Bcrypt</i>", body_bold))
    elements.append(Paragraph("• Built a ticketing platform with role-based access control and secure Bcrypt password hashing; deployed live on Streamlit Cloud.", bullet_style))
    elements.append(Paragraph("• Implemented automated SLA tracking and workload-aware ticket assignment to balance support-team load and proactively flag SLA breaches.", bullet_style))
    elements.append(Paragraph("• Designed an 11-table relational MySQL schema with SQLAlchemy ORM and built dashboards for ticket status, SLA compliance and KPIs.", bullet_style))
    elements.append(Spacer(1, 3))

    # Project 2: Smart Memory Vault
    elements.append(Paragraph("<b>Smart Memory Vault: AI-Powered Multimodal Knowledge System</b> &nbsp;|&nbsp; <i>Python, Streamlit, PostgreSQL, SQLAlchemy, RAG, NLP, OCR</i>", body_bold))
    elements.append(Paragraph("• Built an AI-powered RAG-based knowledge management platform that processes PDFs, images (OCR), YouTube transcripts and audio notes, supporting 50+ documents and 300+ text chunks.", bullet_style))
    elements.append(Paragraph("• Implemented hybrid TF-IDF and embedding-based retrieval using cosine similarity, source citations and confidence scoring, achieving 91% top-3 accuracy across 50+ test queries.", bullet_style))
    elements.append(Paragraph("• Developed NLP features (summarization, sentiment analysis, flashcards, quizzes) with NLTK and Scikit-learn; integrated Bcrypt authentication and deployed on Streamlit Cloud for 25+ users at 1.2s average response time.", bullet_style))
    elements.append(Spacer(1, 3))

    # Project 3: AI Code Reviewer
    elements.append(Paragraph("<b>IntelliCode: AI-Powered Code Reviewer & Bug Analyzer</b> &nbsp;|&nbsp; <i>Python, Streamlit, Gemini API, AST, Static Analysis, Pylint</i>", body_bold))
    elements.append(Paragraph("• Built an automated code analysis tool using Python AST parsing and Gemini LLM reasoning to evaluate code quality, security vulnerabilities (SQL injection, unsafe eval), and cyclomatic complexity.", bullet_style))
    elements.append(Paragraph("• Implemented interactive side-by-side diff comparisons with line-by-line recommendations and automatic unit test generation with sub-1.8s analysis turnaround.", bullet_style))
    elements.append(Spacer(1, 4))

    # Internships
    elements.append(Paragraph("INTERNSHIPS", sec_title))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cbd5e1'), spaceBefore=1, spaceAfter=4))
    elements.append(Paragraph("<b>AI/ML Intern</b> — IBM SkillsBuild &nbsp;|&nbsp; <i>Jun 2025 – Jul 2025</i>", body_bold))
    elements.append(Paragraph("• Preprocessed datasets with Python and Scikit-learn, covering data cleaning, missing-value handling and feature preparation.", bullet_style))
    elements.append(Paragraph("• Trained and evaluated supervised and unsupervised models using accuracy, precision, recall and F1-score, comparing model performance.", bullet_style))
    elements.append(Spacer(1, 2))
    elements.append(Paragraph("<b>Python Intern</b> — VaultofCodes &nbsp;|&nbsp; <i>Jan 2025 – Mar 2025</i>", body_bold))
    elements.append(Paragraph("• Developed Python scripts for file handling, data processing and task automation using functions and object-oriented programming.", bullet_style))
    elements.append(Paragraph("• Debugged programs, validated inputs and handled runtime errors, improving code reliability.", bullet_style))
    elements.append(Spacer(1, 4))

    # Education
    elements.append(Paragraph("EDUCATION", sec_title))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cbd5e1'), spaceBefore=1, spaceAfter=4))
    elements.append(Paragraph("<b>B.Tech, Computer Science and Engineering (AI & ML)</b> — Bapatla Engineering College &nbsp;|&nbsp; <i>2022 – 2026</i> &nbsp;|&nbsp; <b>CGPA: 9.1 / 10</b>", body_bold))
    elements.append(Paragraph("<b>Intermediate (Class XII)</b> — Narayana Junior College &nbsp;|&nbsp; <i>2022</i> &nbsp;|&nbsp; <b>Score: 96%</b>", body))
    elements.append(Paragraph("<b>SSC (Class X)</b> — Z.P. High School &nbsp;|&nbsp; <i>2020</i> &nbsp;|&nbsp; <b>Score: 96%</b>", body))
    elements.append(Spacer(1, 4))

    # Certifications & Achievements
    elements.append(Paragraph("CERTIFICATIONS & ACHIEVEMENTS", sec_title))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cbd5e1'), spaceBefore=1, spaceAfter=4))
    elements.append(Paragraph("• <b>Certifications:</b> Python Essentials (Cisco), AI Fundamentals (IBM SkillsBuild), Intro to AI & ML Fundamentals (Infosys Springboard), Python Programming (HackerRank)", bullet_style))
    elements.append(Paragraph("• <b>Academic Excellence:</b> Received a prestigious shield for academic excellence at Bapatla Engineering College (CGPA: 9.1/10).", bullet_style))
    elements.append(Paragraph("• <b>Coding Recognition:</b> Earned a 4-star Python badge on HackerRank and solved 100+ DSA problems on LeetCode.", bullet_style))
    elements.append(Paragraph("• <b>Technical Presentations:</b> Actively participated and presented technical papers in university engineering symposiums.", bullet_style))

    doc.build(elements)
    print(f"Successfully created: {filename}")

if __name__ == '__main__':
    build_pdf("assets/Shaik_Reena_Kowsar_Resume.pdf", "Comprehensive Technical Resume")
    build_pdf("assets/Shaik_Reena_Kowsar_ATS_Resume.pdf", "ATS-Optimized Resume")
    build_pdf("assets/Shaik_Reena_Kowsar_Academic_Profile.pdf", "Academic & Certification Dossier")
