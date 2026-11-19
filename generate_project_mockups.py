import os

def create_fusion_video_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="vidBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080e1d"/>
      <stop offset="100%" stop-color="#040711"/>
    </linearGradient>
    <linearGradient id="redGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#f97316"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#vidBg)"/>

  <!-- Top App Navigation -->
  <rect x="30" y="20" width="740" height="48" rx="10" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <circle cx="55" cy="44" r="6" fill="#ef4444"/>
  <circle cx="75" cy="44" r="6" fill="#f59e0b"/>
  <circle cx="95" cy="44" r="6" fill="#10b981"/>
  <text x="120" y="49" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="13">YouTube Video Summarization &amp; Multimodal Fusion</text>
  <rect x="630" y="32" width="125" height="24" rx="12" fill="#ef4444" fill-opacity="0.2" stroke="#ef4444" stroke-width="0.8"/>
  <text x="645" y="48" fill="#f87171" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold">NLP + OpenCV</text>

  <!-- Left: Video Ingestion & Keyframe Timeline -->
  <rect x="30" y="80" width="430" height="345" rx="12" fill="#0b1329" stroke="#1e293b" stroke-width="1"/>
  <text x="50" y="110" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">VIDEO INPUT &amp; KEYFRAME EXTRACTION</text>

  <!-- Video Player Preview -->
  <rect x="50" y="125" width="390" height="175" rx="8" fill="#020617" stroke="#334155" stroke-width="0.8"/>
  <circle cx="245" cy="212" r="26" fill="#ef4444" fill-opacity="0.9"/>
  <polygon points="240,202 256,212 240,222" fill="#ffffff"/>
  <text x="65" y="150" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">Deep Learning Lecture: Attention Mechanism.mp4</text>
  <text x="65" y="170" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="10">Duration: 42:15 • 1080p 60fps • Multimodal Audio Track</text>

  <!-- Timeline Keyframes -->
  <g transform="translate(50, 315)">
    <text x="0" y="15" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold">EXTRACTED KEYFRAMES (SCENE CHANGE DETECTION)</text>
    <rect x="0" y="25" width="85" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="0.8"/>
    <text x="15" y="58" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="9">[02:14]</text>
    
    <rect x="100" y="25" width="85" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="0.8"/>
    <text x="115" y="58" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="9">[14:32]</text>

    <rect x="200" y="25" width="85" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="0.8"/>
    <text x="215" y="58" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="9">[28:45]</text>

    <rect x="300" y="25" width="90" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="0.8"/>
    <text x="315" y="58" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="9">[39:10]</text>
  </g>

  <!-- Right: Multimodal Fusion & Generated Summary -->
  <rect x="480" y="80" width="290" height="345" rx="12" fill="#0b1329" stroke="#1e293b" stroke-width="1"/>
  <text x="500" y="110" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">AI FUSION &amp; EXECUTIVE SUMMARY</text>

  <!-- Compression Metric Card -->
  <rect x="500" y="125" width="250" height="60" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="0.8"/>
  <text x="515" y="148" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-size="18" font-weight="bold">78% Reduction</text>
  <text x="515" y="168" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">42m video summarized in 2.4 min read</text>

  <!-- Bullet Summaries -->
  <g transform="translate(500, 205)" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">
    <rect x="0" y="0" width="250" height="48" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="10" y="20" fill="#e2e8f0" font-weight="600">• Attention Mechanisms</text>
    <text x="10" y="36" fill="#94a3b8" font-size="9">Key equations at [14:32], query-key dot product.</text>

    <rect x="0" y="56" width="250" height="48" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="10" y="76" fill="#e2e8f0" font-weight="600">• Transformer Architecture</text>
    <text x="10" y="92" fill="#94a3b8" font-size="9">Positional encoding &amp; multi-head breakdown.</text>

    <rect x="0" y="112" width="250" height="48" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="10" y="132" fill="#e2e8f0" font-weight="600">• SOTA Benchmarks</text>
    <text x="10" y="148" fill="#94a3b8" font-size="9">BLEU scores on WMT 2014 translation test.</text>

    <rect x="0" y="170" width="250" height="35" rx="6" fill="url(#cyanGrad)"/>
    <text x="40" y="192" fill="#030712" font-weight="bold" font-size="11">⚡ Export Structured Notes</text>
  </g>
</svg>'''
    with open('assets/fusion_video_summarizer_mockup.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def create_brain_tumor_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="mriBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060b18"/>
      <stop offset="100%" stop-color="#02050e"/>
    </linearGradient>
    <linearGradient id="heatmap" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="50%" stop-color="#10b981"/>
      <stop offset="80%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#ef4444"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#mriBg)"/>

  <!-- Top App Navigation -->
  <rect x="30" y="20" width="740" height="48" rx="10" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <circle cx="55" cy="44" r="6" fill="#ef4444"/>
  <circle cx="75" cy="44" r="6" fill="#f59e0b"/>
  <circle cx="95" cy="44" r="6" fill="#10b981"/>
  <text x="120" y="49" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="13">Brain Tumor MRI Classification &amp; Grad-CAM Localization</text>
  <rect x="615" y="32" width="140" height="24" rx="12" fill="#10b981" fill-opacity="0.18" stroke="#10b981" stroke-width="0.8"/>
  <text x="630" y="48" fill="#34d399" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold">CNN Accuracy: 98.4%</text>

  <!-- Left: MRI Scan Preprocessing & Grad-CAM Heatmap -->
  <rect x="30" y="80" width="430" height="345" rx="12" fill="#0b1329" stroke="#1e293b" stroke-width="1"/>
  <text x="50" y="110" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">MRI T2 AXIAL SCAN &amp; GRAD-CAM ATTENTION</text>

  <!-- Dual Image Containers -->
  <g transform="translate(50, 125)">
    <!-- Original MRI Simulation -->
    <rect x="0" y="0" width="185" height="200" rx="8" fill="#020617" stroke="#334155"/>
    <circle cx="92" cy="100" r="65" fill="#1e293b" opacity="0.6"/>
    <path d="M50,100 C50,60 134,60 134,100 C134,140 50,140 50,100" fill="#334155" opacity="0.5"/>
    <circle cx="115" cy="85" r="16" fill="#cbd5e1" opacity="0.85"/>
    <text x="15" y="22" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="10">Original MRI (256x256)</text>
    <text x="55" y="190" fill="#64748b" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">Axial View Slice #18</text>

    <!-- Grad-CAM Heatmap -->
    <rect x="205" y="0" width="185" height="200" rx="8" fill="#020617" stroke="#ef4444" stroke-width="1"/>
    <circle cx="297" cy="100" r="65" fill="#1e293b" opacity="0.4"/>
    <!-- Heatmap Overlay Highlight -->
    <circle cx="320" cy="85" r="28" fill="#ef4444" fill-opacity="0.45"/>
    <circle cx="320" cy="85" r="18" fill="#f59e0b" fill-opacity="0.65"/>
    <circle cx="320" cy="85" r="8" fill="#ffffff" fill-opacity="0.9"/>
    <text x="215" y="22" fill="#f87171" font-family="'JetBrains Mono', monospace" font-size="10">Grad-CAM Layer 4 CAM</text>
    <text x="240" y="190" fill="#f87171" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">Region of Interest (ROI)</text>
  </g>

  <!-- Heatmap scale bar -->
  <g transform="translate(50, 345)">
    <text x="0" y="15" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">Activation Confidence Gradient:</text>
    <rect x="165" y="5" width="225" height="12" rx="6" fill="url(#heatmap)"/>
    <text x="165" y="30" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="9">Low (0.0)</text>
    <text x="345" y="30" fill="#ef4444" font-family="'JetBrains Mono', monospace" font-size="9">High (0.98)</text>
  </g>

  <!-- Right: Class Predictions & Probability Distribution -->
  <rect x="480" y="80" width="290" height="345" rx="12" fill="#0b1329" stroke="#1e293b" stroke-width="1"/>
  <text x="500" y="110" fill="#10b981" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">DIAGNOSTIC CLASSIFICATION</text>

  <!-- Predicted Class Banner -->
  <rect x="500" y="125" width="250" height="55" rx="8" fill="#062e24" stroke="#10b981" stroke-width="1"/>
  <text x="515" y="148" fill="#34d399" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="bold">Meningioma Detected</text>
  <text x="515" y="166" fill="#a7f3d0" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">Probability: 98.42% • Sub-150ms Inference</text>

  <!-- Probability Bars -->
  <g transform="translate(500, 195)" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">
    <text x="0" y="15" fill="#ffffff" font-weight="600">Meningioma</text>
    <text x="215" y="15" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="10">98.4%</text>
    <rect x="0" y="22" width="250" height="8" rx="4" fill="#1e293b"/>
    <rect x="0" y="22" width="246" height="8" rx="4" fill="#10b981"/>

    <text x="0" y="50" fill="#cbd5e1">Glioma</text>
    <text x="225" y="50" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="10">1.1%</text>
    <rect x="0" y="57" width="250" height="8" rx="4" fill="#1e293b"/>
    <rect x="0" y="57" width="8" height="8" rx="4" fill="#64748b"/>

    <text x="0" y="85" fill="#cbd5e1">Pituitary</text>
    <text x="225" y="85" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="10">0.4%</text>
    <rect x="0" y="92" width="250" height="8" rx="4" fill="#1e293b"/>
    <rect x="0" y="92" width="4" height="8" rx="4" fill="#64748b"/>

    <text x="0" y="120" fill="#cbd5e1">No Tumor (Healthy)</text>
    <text x="225" y="120" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="10">0.1%</text>
    <rect x="0" y="127" width="250" height="8" rx="4" fill="#1e293b"/>
    <rect x="0" y="127" width="2" height="8" rx="4" fill="#64748b"/>
  </g>

  <!-- Model metadata -->
  <rect x="500" y="350" width="250" height="55" rx="8" fill="#0f172a" stroke="#1e293b"/>
  <text x="515" y="372" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold">CNN Architecture: ResNet-50</text>
  <text x="515" y="392" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="9">OpenCV • Data Augmentation • Cross-Entropy</text>
</svg>'''
    with open('assets/brain_tumor_mri_mockup.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def create_resume_generator_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="resBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080f22"/>
      <stop offset="100%" stop-color="#030713"/>
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#818cf8"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#resBg)"/>

  <!-- Top App Navigation -->
  <rect x="30" y="20" width="740" height="48" rx="10" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <circle cx="55" cy="44" r="6" fill="#ef4444"/>
  <circle cx="75" cy="44" r="6" fill="#f59e0b"/>
  <circle cx="95" cy="44" r="6" fill="#10b981"/>
  <text x="120" y="49" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="13">Resume Generator Web Application &amp; ATS Optimizer</text>
  <rect x="610" y="32" width="145" height="24" rx="12" fill="#818cf8" fill-opacity="0.18" stroke="#818cf8" stroke-width="0.8"/>
  <text x="625" y="48" fill="#a5b4fc" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold">ATS Score: 95/100</text>

  <!-- Left: Interactive Form Controls -->
  <rect x="30" y="80" width="380" height="345" rx="12" fill="#0b1329" stroke="#1e293b" stroke-width="1"/>
  <text x="50" y="110" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">DYNAMIC RESUME BUILDER CONTROLS</text>

  <g transform="translate(50, 125)" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">
    <text x="0" y="15" fill="#cbd5e1">Candidate Name &amp; Contact</text>
    <rect x="0" y="22" width="340" height="32" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="12" y="43" fill="#ffffff" font-size="11">Shaik Reena Kowsar | reenakowsar05@gmail.com</text>

    <text x="0" y="75" fill="#cbd5e1">Target Role / Job Title</text>
    <rect x="0" y="82" width="340" height="32" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="12" y="103" fill="#38bdf8" font-size="11">Python Full Stack Developer &amp; AI/ML Engineer</text>

    <text x="0" y="135" fill="#cbd5e1">Skills &amp; Technologies (Auto-tagging)</text>
    <rect x="0" y="142" width="340" height="40" rx="6" fill="#0f172a" stroke="#334155"/>
    <text x="12" y="166" fill="#a5b4fc" font-size="10">[Python] [SQL] [Streamlit] [Machine Learning] [OpenCV]</text>

    <text x="0" y="205" fill="#cbd5e1">Template Layout Format</text>
    <rect x="0" y="212" width="105" height="30" rx="6" fill="url(#purpleGrad)"/>
    <text x="18" y="231" fill="#030712" font-weight="bold" font-size="11">Modern Clean</text>
    <rect x="115" y="212" width="105" height="30" rx="6" fill="#1e293b" stroke="#334155"/>
    <text x="135" y="231" fill="#cbd5e1" font-size="11">1-Page ATS</text>
    <rect x="230" y="212" width="110" height="30" rx="6" fill="#1e293b" stroke="#334155"/>
    <text x="245" y="231" fill="#cbd5e1" font-size="11">Academic CV</text>
  </g>

  <!-- Right: Real-time Rendered PDF Preview -->
  <rect x="430" y="80" width="340" height="345" rx="12" fill="#0b1329" stroke="#1e293b" stroke-width="1"/>
  <text x="450" y="110" fill="#a5b4fc" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">LIVE ATS-PARSED PDF RENDER</text>

  <!-- Mini White Resume Page -->
  <rect x="450" y="125" width="300" height="245" rx="4" fill="#ffffff" stroke="#e2e8f0"/>
  <rect x="470" y="145" width="260" height="18" fill="#0f172a"/>
  <text x="475" y="158" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="bold">SHAIK REENA KOWSAR — PYTHON DEVELOPER</text>
  <line x1="470" y1="168" x2="730" y2="168" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="470" y="178" width="260" height="6" fill="#94a3b8"/>
  <rect x="470" y="188" width="240" height="5" fill="#cbd5e1"/>
  <rect x="470" y="200" width="80" height="10" fill="#0284c7"/>
  <rect x="470" y="215" width="260" height="5" fill="#94a3b8"/>
  <rect x="470" y="225" width="250" height="5" fill="#cbd5e1"/>
  <rect x="470" y="235" width="210" height="5" fill="#cbd5e1"/>
  
  <rect x="470" y="250" width="100" height="10" fill="#0284c7"/>
  <rect x="470" y="265" width="260" height="5" fill="#94a3b8"/>
  <rect x="470" y="275" width="230" height="5" fill="#cbd5e1"/>

  <!-- Bottom Instant Download Button -->
  <rect x="450" y="380" width="300" height="35" rx="8" fill="url(#purpleGrad)"/>
  <text x="520" y="402" fill="#030712" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="12">Instant Export to PDF</text>
</svg>'''
    with open('assets/resume_generator_mockup.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def create_weather_forecast_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="skyBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#08162d"/>
      <stop offset="100%" stop-color="#030914"/>
    </linearGradient>
    <linearGradient id="sunGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#ef4444"/>
    </linearGradient>
  </defs>

  <rect width="800" height="450" fill="url(#skyBg)"/>

  <!-- Top App Navigation -->
  <rect x="30" y="20" width="740" height="48" rx="10" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>
  <circle cx="55" cy="44" r="6" fill="#ef4444"/>
  <circle cx="75" cy="44" r="6" fill="#f59e0b"/>
  <circle cx="95" cy="44" r="6" fill="#10b981"/>
  <text x="120" y="49" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-weight="bold" font-size="13">Live Meteorological Forecast &amp; Climate Analytics</text>
  <rect x="615" y="32" width="140" height="24" rx="12" fill="#0284c7" fill-opacity="0.2" stroke="#38bdf8" stroke-width="0.8"/>
  <text x="630" y="48" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold">REST Weather API</text>

  <!-- Left: Main City Weather Card -->
  <rect x="30" y="80" width="400" height="345" rx="12" fill="#0b1329" stroke="#1e293b" stroke-width="1"/>
  
  <!-- Search input -->
  <rect x="50" y="100" width="360" height="36" rx="8" fill="#020617" stroke="#334155"/>
  <text x="70" y="123" fill="#e2e8f0" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">Hyderabad, Telangana, India</text>
  <text x="340" y="123" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">Search</text>

  <!-- Temperature & Weather Icon -->
  <g transform="translate(50, 155)">
    <text x="0" y="30" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="bold">Hyderabad</text>
    <text x="0" y="50" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">Scattered Clouds • Humidity 42% • Wind 12 km/h</text>

    <!-- Big Temp -->
    <text x="0" y="125" fill="#38bdf8" font-family="'Space Grotesk', sans-serif" font-size="64" font-weight="bold">28°C</text>
    <circle cx="270" cy="85" r="32" fill="url(#sunGrad)"/>
    <path d="M240,110 Q260,95 285,110 T330,110 A15,15 0 0,0 240,110 Z" fill="#cbd5e1" opacity="0.85"/>
  </g>

  <!-- Metrics Grid -->
  <g transform="translate(50, 310)" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">
    <rect x="0" y="0" width="110" height="50" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="10" y="18" fill="#94a3b8">Pressure</text>
    <text x="10" y="38" fill="#ffffff" font-weight="bold" font-size="12">1012 hPa</text>

    <rect x="125" y="0" width="110" height="50" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="135" y="18" fill="#94a3b8">Visibility</text>
    <text x="135" y="38" fill="#ffffff" font-weight="bold" font-size="12">10 km</text>

    <rect x="250" y="0" width="110" height="50" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="260" y="18" fill="#94a3b8">UV Index</text>
    <text x="260" y="38" fill="#ffffff" font-weight="bold" font-size="12">6 (Moderate)</text>
  </g>

  <!-- Right: 5-Day Forecast -->
  <rect x="450" y="80" width="320" height="345" rx="12" fill="#0b1329" stroke="#1e293b" stroke-width="1"/>
  <text x="470" y="110" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold">5-DAY WEATHER OUTLOOK</text>

  <g transform="translate(470, 130)" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">
    <rect x="0" y="0" width="280" height="44" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="15" y="27" fill="#ffffff" font-weight="600">Tomorrow</text>
    <text x="110" y="27" fill="#94a3b8">Sunny</text>
    <text x="215" y="27" fill="#38bdf8" font-weight="bold">31° / 20°</text>

    <rect x="0" y="54" width="280" height="44" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="15" y="81" fill="#ffffff" font-weight="600">Wednesday</text>
    <text x="110" y="81" fill="#94a3b8">Cloudy</text>
    <text x="215" y="81" fill="#38bdf8" font-weight="bold">29° / 19°</text>

    <rect x="0" y="108" width="280" height="44" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="15" y="135" fill="#ffffff" font-weight="600">Thursday</text>
    <text x="110" y="135" fill="#94a3b8">Light Rain</text>
    <text x="215" y="135" fill="#38bdf8" font-weight="bold">26° / 18°</text>

    <rect x="0" y="162" width="280" height="44" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="15" y="189" fill="#ffffff" font-weight="600">Friday</text>
    <text x="110" y="189" fill="#94a3b8">Thunderstorm</text>
    <text x="215" y="189" fill="#38bdf8" font-weight="bold">24° / 17°</text>

    <rect x="0" y="216" width="280" height="44" rx="6" fill="#0f172a" stroke="#1e293b"/>
    <text x="15" y="243" fill="#ffffff" font-weight="600">Saturday</text>
    <text x="110" y="243" fill="#94a3b8">Clear Sky</text>
    <text x="215" y="243" fill="#38bdf8" font-weight="bold">30° / 19°</text>
  </g>
</svg>'''
    with open('assets/weather_forecast_mockup.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

create_fusion_video_svg()
create_brain_tumor_svg()
create_resume_generator_svg()
create_weather_forecast_svg()
print("All mockups generated successfully!")
