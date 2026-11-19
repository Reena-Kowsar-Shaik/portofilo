import os

def create_smart_memory_vault_svg():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1329"/>
      <stop offset="100%" stop-color="#050a17"/>
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141f36"/>
      <stop offset="100%" stop-color="#0e172a"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="800" height="450" fill="url(#bgGrad)"/>
  
  <!-- Subtle Grid Lines -->
  <g stroke="#1e293b" stroke-width="0.5" opacity="0.4">
    <line x1="0" y1="90" x2="800" y2="90"/>
    <line x1="0" y1="180" x2="800" y2="180"/>
    <line x1="0" y1="270" x2="800" y2="270"/>
    <line x1="0" y1="360" x2="800" y2="360"/>
    <line x1="200" y1="0" x2="200" y2="450"/>
    <line x1="400" y1="0" x2="400" y2="450"/>
    <line x1="600" y1="0" x2="600" y2="450"/>
  </g>

  <!-- Top App Navigation Bar -->
  <rect x="30" y="25" width="740" height="50" rx="10" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <circle cx="55" cy="50" r="6" fill="#ef4444"/>
  <circle cx="75" cy="50" r="6" fill="#f59e0b"/>
  <circle cx="95" cy="50" r="6" fill="#10b981"/>
  
  <text x="120" y="55" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="14">Smart Memory Vault</text>
  <text x="270" y="55" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11">RAG Multimodal Knowledge System</text>

  <!-- Status Pill -->
  <rect x="645" y="38" width="110" height="24" rx="12" fill="#0284c7" fill-opacity="0.2" stroke="#38bdf8" stroke-width="1"/>
  <circle cx="658" cy="50" r="3.5" fill="#38bdf8"/>
  <text x="668" y="54" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="10">LIVE STREAMLIT</text>

  <!-- Left Sidebar Ingestion Sources -->
  <rect x="30" y="90" width="220" height="330" rx="12" fill="url(#cardGrad)" stroke="#1e293b" stroke-width="1"/>
  <text x="50" y="120" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="11" letter-spacing="1">MULTIMODAL SOURCES</text>

  <!-- Ingestion Badges -->
  <g transform="translate(48, 135)">
    <!-- PDF -->
    <rect x="0" y="0" width="184" height="38" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="0.8"/>
    <text x="35" y="24" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="600">PDF Documents (50+)</text>
    <circle cx="18" cy="19" r="6" fill="#ef4444" fill-opacity="0.8"/>

    <!-- Images OCR -->
    <rect x="0" y="48" width="184" height="38" rx="8" fill="#1e293b" stroke="#334155" stroke-width="0.8"/>
    <text x="35" y="72" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="600">Scanned OCR Images</text>
    <circle cx="18" cy="67" r="6" fill="#38bdf8" fill-opacity="0.8"/>

    <!-- YouTube Transcripts -->
    <rect x="0" y="96" width="184" height="38" rx="8" fill="#1e293b" stroke="#334155" stroke-width="0.8"/>
    <text x="35" y="120" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="600">YouTube Audio Video</text>
    <circle cx="18" cy="115" r="6" fill="#f59e0b" fill-opacity="0.8"/>

    <!-- Voice Notes -->
    <rect x="0" y="144" width="184" height="38" rx="8" fill="#1e293b" stroke="#334155" stroke-width="0.8"/>
    <text x="35" y="168" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="600">Audio Speech Transcripts</text>
    <circle cx="18" cy="163" r="6" fill="#10b981" fill-opacity="0.8"/>
  </g>

  <!-- Database & Vector Index Stats -->
  <rect x="48" y="340" width="184" height="60" rx="8" fill="#0f172a" stroke="#1e293b"/>
  <text x="60" y="362" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">PostgreSQL + SQLAlchemy</text>
  <text x="60" y="385" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">Indexed: 300+ Chunks • 1.2s Latency</text>

  <!-- Right Main Area: Hybrid Search & RAG Result -->
  <rect x="265" y="90" width="505" height="330" rx="12" fill="url(#cardGrad)" stroke="#1e293b" stroke-width="1"/>

  <!-- Search Input Bar -->
  <rect x="285" y="110" width="465" height="42" rx="8" fill="#0b1329" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="310" y="136" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="12">What are Transformer Attention Heads in LLMs?</text>
  <rect x="685" y="116" width="55" height="30" rx="6" fill="url(#cyanGrad)"/>
  <text x="702" y="136" fill="#030712" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="11">RAG</text>

  <!-- Retrieval Metrics Bar -->
  <g transform="translate(285, 165)">
    <rect x="0" y="0" width="150" height="26" rx="13" fill="#0f172a" stroke="#10b981" stroke-width="0.8"/>
    <text x="12" y="17" fill="#10b981" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold">Top-3 Accuracy: 91%</text>

    <rect x="160" y="0" width="145" height="26" rx="13" fill="#0f172a" stroke="#38bdf8" stroke-width="0.8"/>
    <text x="172" y="17" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold">Cosine Similarity: 0.94</text>

    <rect x="315" y="0" width="150" height="26" rx="13" fill="#0f172a" stroke="#f59e0b" stroke-width="0.8"/>
    <text x="327" y="17" fill="#f59e0b" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold">Hybrid Dense + TF-IDF</text>
  </g>

  <!-- Extracted Knowledge Output Card -->
  <rect x="285" y="205" width="465" height="145" rx="10" fill="#0b1329" stroke="#1e293b" stroke-width="1"/>
  <text x="305" y="230" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">SOURCE CITATION: ML_Lecture_Notes.pdf (Page 18, Chunk #42)</text>
  <text x="305" y="255" fill="#f8fafc" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="500">"Multi-Head Attention projects queries, keys, and values h times with linear</text>
  <text x="305" y="275" fill="#f8fafc" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="500">projections, allowing the model to jointly attend to information from different</text>
  <text x="305" y="295" fill="#f8fafc" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="500">representation subspaces across multimodal text and transcription vectors."</text>
  
  <text x="305" y="330" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="10">NLP Engine: NLTK • Scikit-Learn • Bcrypt Auth • Streamlit Cloud</text>

  <!-- Interactive Action Tabs Bottom -->
  <g transform="translate(285, 365)">
    <rect x="0" y="0" width="105" height="32" rx="6" fill="#1e293b" stroke="#334155"/>
    <text x="18" y="20" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">📝 Summarize</text>

    <rect x="115" y="0" width="105" height="32" rx="6" fill="#1e293b" stroke="#334155"/>
    <text x="130" y="20" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">🎴 Flashcards</text>

    <rect x="230" y="0" width="105" height="32" rx="6" fill="#1e293b" stroke="#334155"/>
    <text x="248" y="20" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">⚡ AI Quiz</text>

    <rect x="345" y="0" width="120" height="32" rx="6" fill="url(#cyanGrad)"/>
    <text x="357" y="20" fill="#030712" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">🚀 Export Insights</text>
  </g>
</svg>"""
    with open("assets/smart_memory_vault_mockup.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Created: assets/smart_memory_vault_mockup.svg")

def create_it_helpdesk_svg():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="helpdeskBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1329"/>
      <stop offset="100%" stop-color="#050a17"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2563eb"/>
      <stop offset="100%" stop-color="#38bdf8"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#helpdeskBg)"/>

  <!-- Top App Navigation Bar -->
  <rect x="30" y="25" width="740" height="50" rx="10" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <circle cx="55" cy="50" r="6" fill="#ef4444"/>
  <circle cx="75" cy="50" r="6" fill="#f59e0b"/>
  <circle cx="95" cy="50" r="6" fill="#10b981"/>
  <text x="120" y="55" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="14">IT Helpdesk &amp; Support Intelligence</text>
  <text x="390" y="55" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11">SLA Tracking &amp; Analytics Dashboard</text>

  <!-- Metric KPI Cards -->
  <g transform="translate(30, 90)">
    <rect x="0" y="0" width="170" height="80" rx="10" fill="#0f172a" stroke="#1e293b"/>
    <text x="18" y="28" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">ACTIVE TICKETS</text>
    <text x="18" y="60" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="bold">142</text>
    <text x="75" y="60" fill="#10b981" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">↓ 8% load</text>

    <rect x="190" y="0" width="170" height="80" rx="10" fill="#0f172a" stroke="#1e293b"/>
    <text x="208" y="28" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">SLA COMPLIANCE</text>
    <text x="208" y="60" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="bold">98.4%</text>
    <text x="290" y="60" fill="#10b981" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">On Target</text>

    <rect x="380" y="0" width="170" height="80" rx="10" fill="#0f172a" stroke="#1e293b"/>
    <text x="398" y="28" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">AVG RESOLUTION</text>
    <text x="398" y="60" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="bold">1.4h</text>
    <text x="460" y="60" fill="#10b981" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">-32m faster</text>

    <rect x="570" y="0" width="170" height="80" rx="10" fill="#0f172a" stroke="#1e293b"/>
    <text x="588" y="28" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">RELATIONAL TABLES</text>
    <text x="588" y="60" fill="#f59e0b" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="bold">11 Tables</text>
    <text x="690" y="60" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="10">MySQL</text>
  </g>

  <!-- Relational Ticket Queue Table -->
  <rect x="30" y="190" width="460" height="230" rx="10" fill="#0f172a" stroke="#1e293b"/>
  <text x="50" y="220" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="13">Live Ticket Dispatch Queue (RBAC)</text>

  <!-- Table rows -->
  <g transform="translate(50, 240)">
    <!-- Row 1 -->
    <rect x="0" y="0" width="420" height="34" rx="6" fill="#1e293b"/>
    <text x="12" y="22" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11">#TK-8942</text>
    <text x="85" y="22" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">Production DB Replica Out of Sync</text>
    <rect x="340" y="7" width="70" height="20" rx="10" fill="#ef4444" fill-opacity="0.2"/>
    <text x="352" y="21" fill="#ef4444" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold">CRITICAL</text>

    <!-- Row 2 -->
    <rect x="0" y="42" width="420" height="34" rx="6" fill="#141f36"/>
    <text x="12" y="64" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11">#TK-8941</text>
    <text x="85" y="64" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">VPN Gateway Auth Latency Breach</text>
    <rect x="340" y="49" width="70" height="20" rx="10" fill="#f59e0b" fill-opacity="0.2"/>
    <text x="355" y="63" fill="#f59e0b" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold">HIGH SLA</text>

    <!-- Row 3 -->
    <rect x="0" y="84" width="420" height="34" rx="6" fill="#1e293b"/>
    <text x="12" y="106" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11">#TK-8940</text>
    <text x="85" y="106" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">Bcrypt Hash Salt Rotation Policy</text>
    <rect x="340" y="91" width="70" height="20" rx="10" fill="#10b981" fill-opacity="0.2"/>
    <text x="350" y="105" fill="#10b981" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold">RESOLVED</text>

    <!-- Row 4 -->
    <rect x="0" y="126" width="420" height="34" rx="6" fill="#141f36"/>
    <text x="12" y="148" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11">#TK-8939</text>
    <text x="85" y="148" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">SQLAlchemy ORM Connection Pool</text>
    <rect x="340" y="133" width="70" height="20" rx="10" fill="#38bdf8" fill-opacity="0.2"/>
    <text x="348" y="147" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold">IN REVIEW</text>
  </g>

  <!-- Right Chart: Plotly SLA Analytics -->
  <rect x="510" y="190" width="260" height="230" rx="10" fill="#0f172a" stroke="#1e293b"/>
  <text x="530" y="220" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="13">Plotly SLA Trajectory</text>
  
  <!-- Mini Bar Chart -->
  <g transform="translate(530, 240)">
    <rect x="10" y="80" width="22" height="60" rx="3" fill="#38bdf8"/>
    <rect x="45" y="40" width="22" height="100" rx="3" fill="#38bdf8"/>
    <rect x="80" y="20" width="22" height="120" rx="3" fill="#2563eb"/>
    <rect x="115" y="55" width="22" height="85" rx="3" fill="#38bdf8"/>
    <rect x="150" y="15" width="22" height="125" rx="3" fill="#10b981"/>
    <rect x="185" y="30" width="22" height="110" rx="3" fill="#38bdf8"/>
    <line x1="0" y1="140" x2="220" y2="140" stroke="#334155" stroke-width="1"/>
    <text x="10" y="156" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9">Mon</text>
    <text x="45" y="156" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9">Tue</text>
    <text x="80" y="156" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9">Wed</text>
    <text x="115" y="156" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9">Thu</text>
    <text x="150" y="156" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9">Fri</text>
    <text x="185" y="156" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9">Sat</text>
  </g>
</svg>"""
    with open("assets/it_helpdesk_mockup.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Created: assets/it_helpdesk_mockup.svg")

def create_ai_code_reviewer_svg():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="codeBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1329"/>
      <stop offset="100%" stop-color="#050a17"/>
    </linearGradient>
    <linearGradient id="cyanAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#60a5fa"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#codeBg)"/>

  <!-- Top App Navigation Bar -->
  <rect x="30" y="25" width="740" height="50" rx="10" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <circle cx="55" cy="50" r="6" fill="#ef4444"/>
  <circle cx="75" cy="50" r="6" fill="#f59e0b"/>
  <circle cx="95" cy="50" r="6" fill="#10b981"/>
  <text x="120" y="55" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="14">IntelliCode: AI Code Reviewer &amp; Bug Analyzer</text>
  <text x="470" y="55" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11">AST Engine + Gemini API</text>

  <!-- Left: Original Code with AST Flags -->
  <rect x="30" y="90" width="360" height="330" rx="10" fill="#0f172a" stroke="#1e293b"/>
  <text x="50" y="120" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">SOURCE CODE (VULNERABILITIES FOUND)</text>

  <g transform="translate(50, 140)" font-family="'JetBrains Mono', monospace" font-size="11">
    <text x="0" y="20" fill="#94a3b8">1</text>
    <text x="25" y="20" fill="#60a5fa">def</text>
    <text x="55" y="20" fill="#38bdf8">fetch_user_records</text>
    <text x="185" y="20" fill="#e2e8f0">(user_id):</text>

    <text x="0" y="45" fill="#94a3b8">2</text>
    <text x="25" y="45" fill="#e2e8f0">&nbsp;&nbsp;&nbsp;&nbsp;query =</text>
    <text x="120" y="45" fill="#f87171">f"SELECT * FROM users"</text>

    <!-- Bug line highlighted -->
    <rect x="-10" y="55" width="340" height="28" rx="4" fill="#ef4444" fill-opacity="0.15" stroke="#ef4444" stroke-width="0.8"/>
    <text x="0" y="74" fill="#f87171">3</text>
    <text x="25" y="74" fill="#fca5a5">&nbsp;&nbsp;&nbsp;&nbsp;query += f" WHERE id={user_id}"</text>

    <text x="0" y="105" fill="#94a3b8">4</text>
    <text x="25" y="105" fill="#e2e8f0">&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(query)</text>

    <text x="0" y="130" fill="#94a3b8">5</text>
    <text x="25" y="130" fill="#60a5fa">&nbsp;&nbsp;&nbsp;&nbsp;return</text>
    <text x="80" y="130" fill="#e2e8f0">cursor.fetchall()</text>
  </g>

  <!-- Vulnerability Card Warning -->
  <rect x="50" y="300" width="320" height="100" rx="8" fill="#1e1b2e" stroke="#ef4444" stroke-width="1"/>
  <text x="65" y="325" fill="#ef4444" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="11">⚠️ AST SECURITY TRAP DETECTED</text>
  <text x="65" y="348" fill="#fca5a5" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">CWE-89: SQL Injection Vulnerability</text>
  <text x="65" y="370" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">Unsanitized f-string formatting in raw SQL query.</text>
  <text x="65" y="388" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="10">Severity: CRITICAL • Complexity: O(1)</text>

  <!-- Right: AI Refactored Code with Gemini -->
  <rect x="410" y="90" width="360" height="330" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
  <text x="430" y="120" fill="#10b981" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">AI REFACTORED (PEP 8 &amp; SECURE)</text>

  <g transform="translate(430, 140)" font-family="'JetBrains Mono', monospace" font-size="11">
    <text x="0" y="20" fill="#94a3b8">1</text>
    <text x="25" y="20" fill="#60a5fa">def</text>
    <text x="55" y="20" fill="#38bdf8">fetch_user_records</text>
    <text x="185" y="20" fill="#e2e8f0">(user_id: int):</text>

    <text x="0" y="45" fill="#94a3b8">2</text>
    <text x="25" y="45" fill="#94a3b8">&nbsp;&nbsp;&nbsp;&nbsp;&quot;&quot;&quot;Parameterized safe execution&quot;&quot;&quot;</text>

    <!-- Refactored line highlighted -->
    <rect x="-10" y="55" width="340" height="28" rx="4" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-width="0.8"/>
    <text x="0" y="74" fill="#34d399">3</text>
    <text x="25" y="74" fill="#6ee7b7">&nbsp;&nbsp;&nbsp;&nbsp;stmt = "SELECT * FROM users WHERE id=%s"</text>

    <text x="0" y="105" fill="#94a3b8">4</text>
    <text x="25" y="105" fill="#e2e8f0">&nbsp;&nbsp;&nbsp;&nbsp;cursor.execute(stmt, (user_id,))</text>

    <text x="0" y="130" fill="#94a3b8">5</text>
    <text x="25" y="130" fill="#60a5fa">&nbsp;&nbsp;&nbsp;&nbsp;return</text>
    <text x="80" y="130" fill="#e2e8f0">cursor.fetchall()</text>
  </g>

  <!-- AI Optimization Card -->
  <rect x="430" y="300" width="320" height="100" rx="8" fill="#062e24" stroke="#10b981" stroke-width="1"/>
  <text x="445" y="325" fill="#10b981" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="11">✅ GEMINI LLM REFACTORING COMPLETE</text>
  <text x="445" y="348" fill="#a7f3d0" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">Applied Parameterized SQL Execution</text>
  <text x="445" y="370" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">Automated unit test generated in 1.4s.</text>
  <text x="445" y="388" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="10">Pylint Score: 10.0 / 10 • Clean Code</text>
</svg>"""
    with open("assets/ai_code_reviewer_mockup.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Created: assets/ai_code_reviewer_mockup.svg")

if __name__ == '__main__':
    create_smart_memory_vault_svg()
    create_it_helpdesk_svg()
    create_ai_code_reviewer_svg()
