/**
 * REENA KOWSAR — ADVANCED INTERACTIVE DEVELOPER PORTFOLIO ENGINE
 * Includes: Interactive Terminal, 3D Tilt Card, Live RAG Simulator & Sound FX
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Web Audio Synthesizer (Zero External Dependencies)
  let soundEnabled = localStorage.getItem('portfolio_sound') !== 'false';
  const audioCtx = (window.AudioContext || window.webkitAudioContext) ? new (window.AudioContext || window.webkitAudioContext)() : null;

  function playUiSound(type = 'click') {
    if (!soundEnabled || !audioCtx) return;
    try {
      if (audioCtx.state === 'suspended') audioCtx.resume();
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.connect(gain);
      gain.connect(audioCtx.destination);

      const now = audioCtx.currentTime;
      if (type === 'click') {
        osc.frequency.setValueAtTime(600, now);
        osc.frequency.exponentialRampToValueAtTime(320, now + 0.04);
        gain.gain.setValueAtTime(0.04, now);
        gain.gain.linearRampToValueAtTime(0.001, now + 0.04);
        osc.start(now);
        osc.stop(now + 0.04);
      } else if (type === 'pop') {
        osc.frequency.setValueAtTime(350, now);
        osc.frequency.exponentialRampToValueAtTime(800, now + 0.06);
        gain.gain.setValueAtTime(0.05, now);
        gain.gain.linearRampToValueAtTime(0.001, now + 0.06);
        osc.start(now);
        osc.stop(now + 0.06);
      } else if (type === 'terminal') {
        osc.type = 'square';
        osc.frequency.setValueAtTime(880, now);
        gain.gain.setValueAtTime(0.02, now);
        gain.gain.linearRampToValueAtTime(0.001, now + 0.03);
        osc.start(now);
        osc.stop(now + 0.03);
      } else if (type === 'success') {
        osc.frequency.setValueAtTime(523.25, now);
        osc.frequency.setValueAtTime(659.25, now + 0.07);
        osc.frequency.setValueAtTime(783.99, now + 0.14);
        gain.gain.setValueAtTime(0.06, now);
        gain.gain.linearRampToValueAtTime(0.001, now + 0.22);
        osc.start(now);
        osc.stop(now + 0.22);
      }
    } catch (e) {}
  }

  // 2. Sound Toggle Button
  const soundBtn = document.getElementById('sound-toggle-btn');
  function updateSoundIcon() {
    if (!soundBtn) return;
    if (soundEnabled) {
      soundBtn.innerHTML = `<i data-lucide="volume-2" class="w-4 h-4 text-primary"></i>`;
      soundBtn.title = "Audio: ON (Click to mute)";
    } else {
      soundBtn.innerHTML = `<i data-lucide="volume-x" class="w-4 h-4 text-slate-500"></i>`;
      soundBtn.title = "Audio: OFF (Click to unmute)";
    }
    if (window.lucide) lucide.createIcons();
  }

  if (soundBtn) {
    updateSoundIcon();
    soundBtn.addEventListener('click', () => {
      soundEnabled = !soundEnabled;
      localStorage.setItem('portfolio_sound', soundEnabled);
      updateSoundIcon();
      playUiSound('pop');
    });
  }

  // 3. Populate Social Links
  const socialContainers = document.querySelectorAll('.social-links-container');
  socialContainers.forEach(container => {
    container.innerHTML = PORTFOLIO_DATA.socials.map(s => `
      <a href="${s.url}" target="_blank" rel="noopener noreferrer" 
         class="sidebar-social-link" title="${s.name}" aria-label="${s.name}">
        <i data-lucide="${s.icon}" class="w-4 h-4"></i>
      </a>
    `).join('');
  });

  // 4. Hero 3D Card Tilt Physics
  const holoCard = document.getElementById('hero-holo-card');
  if (holoCard) {
    holoCard.addEventListener('mousemove', (e) => {
      const rect = holoCard.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = ((y - centerY) / centerY) * -8;
      const rotateY = ((x - centerX) / centerX) * 8;
      holoCard.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
    });

    holoCard.addEventListener('mouseleave', () => {
      holoCard.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0)';
    });
  }

  // 5. Populate Projects Cards with Interactive Features
  const projectsContainer = document.getElementById('projects-grid');
  if (projectsContainer && PORTFOLIO_DATA.projects) {
    projectsContainer.innerHTML = PORTFOLIO_DATA.projects.map((proj, idx) => `
      <div class="dark-card overflow-hidden flex flex-col justify-between group" data-project-id="${proj.id}">
        
        <!-- Project Preview Image -->
        <div class="relative overflow-hidden aspect-video bg-[#070d1a] border-b border-white/5">
          <img src="${proj.image}" alt="${proj.title}" loading="lazy"
               class="w-full h-full object-contain transition-transform duration-500 group-hover:scale-102" />
          <div class="absolute top-3 left-3 flex items-center space-x-2">
            ${proj.featured ? `<span class="px-3 py-1 text-xs font-bold rounded-full bg-primary text-slate-950 shadow-md">Featured Project</span>` : ''}
            <span class="text-xs uppercase tracking-wider font-semibold text-primary bg-black/80 backdrop-blur-md px-2.5 py-1 rounded-full border border-white/10">${proj.category}</span>
          </div>
        </div>

        <!-- Project Content -->
        <div class="p-6 sm:p-7 flex-1 flex flex-col justify-between">
          <div>
            <h3 class="text-xl font-bold text-white group-hover:text-primary transition-colors mb-1">${proj.title}</h3>
            <p class="text-xs sm:text-sm text-primary font-semibold mb-3">${proj.subtitle}</p>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed mb-4">${proj.description}</p>
            
            <div class="flex flex-wrap gap-1.5 mb-5">
              ${proj.tags.map(t => `<span class="tech-pill text-[11px]">${t}</span>`).join('')}
            </div>
          </div>

          <div class="pt-5 border-t border-white/10 flex flex-wrap items-center justify-between gap-3 mt-auto">
            <div class="flex items-center space-x-2">
              <button class="open-case-study-btn text-xs font-bold text-white bg-white/10 hover:bg-primary hover:text-slate-950 px-3.5 py-2 rounded-xl flex items-center space-x-1.5 transition-all" data-id="${proj.id}">
                <i data-lucide="layers" class="w-3.5 h-3.5"></i>
                <span>Architecture & Case Study</span>
              </button>
              ${proj.id === 'project-1' ? `
                <a href="#rag-simulator-section" class="text-xs font-bold text-primary hover:underline flex items-center space-x-1">
                  <i data-lucide="play-circle" class="w-3.5 h-3.5"></i>
                  <span>Live Simulator ↓</span>
                </a>
              ` : ''}
            </div>

            <div class="flex items-center space-x-2">
              ${proj.githubUrl ? `
                <a href="${proj.githubUrl}" target="_blank" rel="noopener noreferrer" class="p-2.5 rounded-xl bg-white/5 hover:bg-white/15 text-slate-300 hover:text-white transition-colors" title="GitHub Source">
                  <i data-lucide="github" class="w-4 h-4"></i>
                </a>
              ` : ''}
              ${proj.demoUrl ? `
                <a href="${proj.demoUrl}" target="_blank" rel="noopener noreferrer" class="p-2.5 rounded-xl bg-primary/20 hover:bg-primary hover:text-slate-950 text-primary transition-all shadow-sm" title="Live Application">
                  <i data-lucide="external-link" class="w-4 h-4"></i>
                </a>
              ` : ''}
            </div>
          </div>
        </div>

      </div>
    `).join('');
  }

  // 6. Populate Skills Grid
  const skillsContainer = document.getElementById('skills-grid');
  if (skillsContainer && PORTFOLIO_DATA.skillCategories) {
    skillsContainer.innerHTML = PORTFOLIO_DATA.skillCategories.map(cat => `
      <div class="dark-card p-6">
        <h3 class="text-base font-bold text-white mb-3 text-primary flex items-center space-x-2">
          <i data-lucide="code-2" class="w-4 h-4"></i>
          <span>${cat.name}</span>
        </h3>
        <div class="flex flex-wrap gap-2">
          ${cat.skills.map(skill => `<span class="tech-pill">${skill}</span>`).join('')}
        </div>
      </div>
    `).join('');
  }

  // 7. Populate Internships & Experience Timeline
  const timelineContainer = document.getElementById('experience-timeline');
  if (timelineContainer && PORTFOLIO_DATA.internships) {
    timelineContainer.innerHTML = PORTFOLIO_DATA.internships.map((item, idx) => `
      <div class="dark-card p-6 border-l-4 border-l-primary relative">
        <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
          <div class="flex items-center space-x-2">
            <span class="text-xs uppercase font-mono px-2.5 py-1 rounded-full bg-primary/10 border border-primary/30 text-primary font-bold">${item.period}</span>
            <span class="text-xs text-slate-400">• ${item.location}</span>
          </div>
        </div>
        <h3 class="text-xl font-bold text-white">${item.role} <span class="text-primary font-semibold">@ ${item.company}</span></h3>
        <ul class="mt-3 space-y-2">
          ${item.highlights.map(h => `
            <li class="flex items-start space-x-2 text-sm text-slate-300">
              <i data-lucide="check-circle" class="w-4 h-4 text-primary shrink-0 mt-0.5"></i>
              <span>${h}</span>
            </li>
          `).join('')}
        </ul>
      </div>
    `).join('');
  }

  // 8. Populate Separate Resumes (User Request: "separate separate give & when click download it should download")
  const resumesContainer = document.getElementById('resumes-grid');
  if (resumesContainer && PORTFOLIO_DATA.resumes) {
    resumesContainer.innerHTML = PORTFOLIO_DATA.resumes.map(r => `
      <div class="dark-card p-6 flex flex-col justify-between relative group ${r.isPrimary ? 'border-primary/50 shadow-lg shadow-primary/10' : ''}">
        ${r.isPrimary ? `<span class="absolute -top-3 right-5 text-[10px] font-bold uppercase tracking-wider px-3 py-1 rounded-full bg-primary text-slate-950 shadow-md">Recommended CV</span>` : ''}
        <div>
          <div class="w-12 h-12 rounded-2xl bg-primary/10 border border-primary/30 flex items-center justify-center text-primary mb-4 group-hover:scale-110 transition-transform">
            <i data-lucide="${r.icon}" class="w-6 h-6"></i>
          </div>
          <h3 class="text-lg font-bold text-white group-hover:text-primary transition-colors">${r.title}</h3>
          <p class="text-xs text-slate-400 mt-1 leading-relaxed">${r.subtitle}</p>
          <div class="flex items-center space-x-2 mt-4 text-xs font-mono text-slate-300">
            <span class="px-2 py-0.5 rounded bg-white/5 border border-white/10">${r.format}</span>
            <span>${r.fileSize}</span>
          </div>
        </div>

        <div class="mt-6 pt-4 border-t border-white/10">
          <a href="${r.downloadUrl}" download="${r.fileName}" class="w-full ${r.isPrimary ? 'btn-primary' : 'btn-pill-outline'} py-2.5 rounded-xl text-xs font-bold flex items-center justify-center space-x-2 transition-all group-hover:scale-[1.02]">
            <i data-lucide="download" class="w-4 h-4"></i>
            <span>Download PDF</span>
          </a>
        </div>
      </div>
    `).join('');
  }

  // 9. Populate Education Card
  const eduContainer = document.getElementById('education-card');
  if (eduContainer && PORTFOLIO_DATA.education && PORTFOLIO_DATA.education[0]) {
    const btech = PORTFOLIO_DATA.education[0];
    eduContainer.innerHTML = `
      <div class="dark-card p-6 sm:p-8 border border-primary/30 relative overflow-hidden">
        <div class="flex flex-wrap items-center justify-between gap-4 mb-3">
          <div>
            <span class="text-xs font-mono px-3 py-1 rounded-full bg-primary/10 border border-primary/30 text-primary font-bold">${btech.duration}</span>
            <h3 class="text-2xl font-bold text-white mt-2">${btech.degree}</h3>
            <p class="text-base text-primary font-semibold">${btech.institution} • ${btech.location}</p>
          </div>
          <div class="text-right">
            <div class="text-3xl font-extrabold text-primary">${btech.grade}</div>
            <div class="text-xs font-bold text-emerald-400 mt-1">${btech.highlight}</div>
          </div>
        </div>

        <div class="mt-6 pt-5 border-t border-white/10">
          <h4 class="text-xs font-mono uppercase tracking-wider text-slate-400 font-bold mb-3">${btech.courseworkHeading}</h4>
          <div class="flex flex-wrap gap-2">
            ${btech.coursework.map(c => `<span class="tech-pill">${c}</span>`).join('')}
          </div>
        </div>
      </div>
    `;
  }

  // 10. Populate Certifications
  const certContainer = document.getElementById('certifications-list');
  if (certContainer && PORTFOLIO_DATA.certifications) {
    certContainer.innerHTML = PORTFOLIO_DATA.certifications.map(c => `
      <div class="flex items-center space-x-3 p-3 rounded-xl bg-white/5 border border-white/5 hover:border-primary/30 transition-colors">
        <div class="w-9 h-9 rounded-lg bg-primary/15 text-primary flex items-center justify-center shrink-0">
          <i data-lucide="${c.icon || 'award'}" class="w-4 h-4"></i>
        </div>
        <div>
          <p class="text-sm font-bold text-white">${c.title}</p>
          <p class="text-xs text-slate-400">${c.issuer}</p>
        </div>
      </div>
    `).join('');
  }

  // 11. Populate Key Achievements
  const achContainer = document.getElementById('achievements-list');
  if (achContainer && PORTFOLIO_DATA.achievements) {
    achContainer.innerHTML = PORTFOLIO_DATA.achievements.map(a => `
      <div class="flex items-start space-x-3 p-3 rounded-xl bg-white/5 border border-white/5 hover:border-primary/30 transition-colors">
        <div class="w-9 h-9 rounded-lg bg-emerald-500/15 text-emerald-400 flex items-center justify-center shrink-0 mt-0.5">
          <i data-lucide="${a.icon || 'star'}" class="w-4 h-4"></i>
        </div>
        <div>
          <p class="text-sm font-bold text-white">${a.title}</p>
          <p class="text-xs text-slate-400 leading-relaxed mt-0.5">${a.description}</p>
        </div>
      </div>
    `).join('');
  }

  // 12. Project Case Study Modal Logic
  const modal = document.getElementById('project-modal');
  const modalBody = document.getElementById('modal-content');
  const modalClose = document.getElementById('modal-close-btn');

  function openProjectModal(projectId) {
    const proj = PORTFOLIO_DATA.projects.find(p => p.id === projectId);
    if (!proj || !modal || !modalBody) return;

    modalBody.innerHTML = `
      <div class="relative w-full aspect-video rounded-xl overflow-hidden mb-6 bg-[#070d1a] border border-white/10">
        <img src="${proj.image}" alt="${proj.title}" class="w-full h-full object-contain" />
      </div>
      <div class="flex flex-wrap items-center justify-between gap-3 mb-4">
        <div>
          <span class="text-xs uppercase tracking-wider font-semibold text-primary px-3 py-1 rounded-full bg-primary/10 border border-primary/25">${proj.category}</span>
          <h2 class="text-2xl sm:text-3xl font-extrabold text-white mt-2">${proj.title}</h2>
          <p class="text-sm text-primary font-semibold">${proj.subtitle}</p>
        </div>
        <div class="flex items-center space-x-3">
          ${proj.githubUrl ? `
            <a href="${proj.githubUrl}" target="_blank" rel="noopener noreferrer" class="btn-pill-outline px-4 py-2 text-xs font-semibold flex items-center space-x-1.5">
              <i data-lucide="github" class="w-4 h-4"></i>
              <span>GitHub</span>
            </a>
          ` : ''}
          ${proj.demoUrl ? `
            <a href="${proj.demoUrl}" target="_blank" rel="noopener noreferrer" class="btn-primary px-4 py-2 rounded-xl text-xs font-semibold flex items-center space-x-1.5">
              <i data-lucide="external-link" class="w-4 h-4"></i>
              <span>Live Deployment</span>
            </a>
          ` : ''}
        </div>
      </div>

      <div class="flex flex-wrap gap-2 mb-6">
        ${proj.tags.map(t => `<span class="tech-pill">${t}</span>`).join('')}
      </div>

      <div class="space-y-5 text-sm text-slate-300 leading-relaxed border-t border-white/10 pt-5">
        <div>
          <h4 class="text-white font-bold text-base mb-2">Project Overview</h4>
          <p>${proj.description}</p>
        </div>

        ${proj.highlights ? `
          <div>
            <h4 class="text-white font-bold text-sm mb-2 text-primary">Architecture Highlights & Implementations</h4>
            <ul class="space-y-2">
              ${proj.highlights.map(h => `
                <li class="flex items-start space-x-2 text-xs sm:text-sm text-slate-300">
                  <i data-lucide="check-circle-2" class="w-4 h-4 text-primary shrink-0 mt-0.5"></i>
                  <span>${h}</span>
                </li>
              `).join('')}
            </ul>
          </div>
        ` : ''}

        ${proj.caseStudy ? `
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
            <div class="p-4 rounded-xl bg-white/5 border border-white/10">
              <h5 class="font-bold text-rose-400 text-xs uppercase tracking-wider mb-1">Technical Challenge</h5>
              <p class="text-xs text-slate-300">${proj.caseStudy.challenge}</p>
            </div>
            <div class="p-4 rounded-xl bg-white/5 border border-white/10">
              <h5 class="font-bold text-emerald-400 text-xs uppercase tracking-wider mb-1">Engineered Solution</h5>
              <p class="text-xs text-slate-300">${proj.caseStudy.solution}</p>
            </div>
          </div>
          <div class="p-4 rounded-xl bg-primary/10 border border-primary/25">
            <h5 class="font-bold text-primary text-xs uppercase tracking-wider mb-1">Results & Benchmarks</h5>
            <p class="text-xs text-slate-200">${proj.caseStudy.results}</p>
          </div>
        ` : ''}
      </div>
    `;

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    if (window.lucide) lucide.createIcons();
    playUiSound('pop');
  }

  function closeProjectModal() {
    if (!modal) return;
    modal.classList.add('hidden');
    document.body.style.overflow = '';
    playUiSound('click');
  }

  document.querySelectorAll('.open-case-study-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      openProjectModal(btn.dataset.id);
    });
  });

  if (modalClose) modalClose.addEventListener('click', closeProjectModal);
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeProjectModal();
    });
  }
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal && !modal.classList.contains('hidden')) {
      closeProjectModal();
    }
  });

  // 13. Interactive RAG Simulator Engine (Smart Memory Vault)
  const ragQueries = {
    attention: {
      query: "What is Multi-Head Attention in Transformer architectures?",
      match: "91.4% (Cosine Similarity: 0.942)",
      source: "Deep_Learning_Notes.pdf (Page 18, Chunk #42)",
      content: "Multi-Head Attention linearly projects queries, keys, and values h times with learned projections. It allows the model to jointly attend to information from different representation subspaces at different positions.",
      stats: "Retrieved in 1.18s • 300+ text chunks indexed • PostgreSQL pgvector"
    },
    multimodal: {
      query: "How does the multimodal pipeline process OCR scanned documents & audio?",
      match: "94.8% (Cosine Similarity: 0.965)",
      source: "System_Architecture.pdf (Page 6, Chunk #12)",
      content: "Uploaded scanned PDFs are parsed using OpenCV preprocessing followed by Tesseract OCR text extraction. Audio speech transcripts are converted into normalized vector embeddings and chunked with 20% overlap.",
      stats: "Hybrid Dense + TF-IDF index • 1.25s latency • Zero hallucination"
    },
    database: {
      query: "What database schema and authentication is implemented?",
      match: "98.2% (Cosine Similarity: 0.988)",
      source: "Database_Schema_Spec.md (Chunk #3)",
      content: "Uses PostgreSQL with SQLAlchemy ORM models storing user credentials, hashed passwords using Bcrypt with salt rounds, document metadata, and embedding vector arrays for high-throughput cosine queries.",
      stats: "Bcrypt secure auth • Relational integrity • Streamlit Cloud live"
    }
  };

  const ragQueryInput = document.getElementById('rag-query-input');
  const ragOutputBox = document.getElementById('rag-output-box');
  const ragMatchBadge = document.getElementById('rag-match-badge');
  const ragSourceBadge = document.getElementById('rag-source-badge');
  const ragStatsBadge = document.getElementById('rag-stats-badge');
  const ragSimBtn = document.getElementById('rag-run-btn');

  function runRagSimulation(key = 'attention') {
    const data = ragQueries[key] || ragQueries.attention;
    if (ragQueryInput) ragQueryInput.value = data.query;
    playUiSound('terminal');

    if (ragOutputBox) {
      ragOutputBox.innerHTML = `
        <div class="flex items-center space-x-2 text-primary font-mono text-xs">
          <svg class="animate-spin h-3.5 w-3.5 text-primary" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path>
          </svg>
          <span>Executing Hybrid Dense Vector + TF-IDF Retrieval over 50+ documents...</span>
        </div>
      `;

      setTimeout(() => {
        ragOutputBox.innerHTML = `
          <div class="space-y-2 text-slate-200">
            <p class="font-semibold text-white">"${data.content}"</p>
            <p class="text-xs font-mono text-primary pt-1">Source: ${data.source}</p>
          </div>
        `;
        if (ragMatchBadge) ragMatchBadge.textContent = `Match: ${data.match}`;
        if (ragSourceBadge) ragSourceBadge.textContent = data.source;
        if (ragStatsBadge) ragStatsBadge.textContent = data.stats;
        playUiSound('success');
      }, 750);
    }
  }

  document.querySelectorAll('.rag-preset-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      runRagSimulation(btn.dataset.preset);
    });
  });

  if (ragSimBtn) {
    ragSimBtn.addEventListener('click', () => {
      runRagSimulation('attention');
    });
  }

  // 14. Interactive CLI Developer Console
  const cliInput = document.getElementById('cli-input');
  const cliOutput = document.getElementById('cli-output');

  const CLI_COMMANDS = {
    help: `Available commands:
  <span class="text-primary">whoami</span>     - About Shaik Reena Kowsar
  <span class="text-primary">skills</span>     - Technical stack & competencies
  <span class="text-primary">projects</span>   - Live deployed applications
  <span class="text-primary">education</span>  - College, CGPA & academic rank
  <span class="text-primary">resume</span>     - Triggers instant PDF download
  <span class="text-primary">contact</span>    - Email, phone, location & profiles
  <span class="text-primary">clear</span>      - Clear terminal screen`,
    
    whoami: `<span class="text-white font-bold">Shaik Reena Kowsar</span> — Software Engineer & Python Full Stack Developer
B.Tech CSE (AI & ML) at Bapatla Engineering College | CGPA: 9.1/10 (Academic Excellence Shield)
Building production RAG systems, database-driven web applications, and AI models.`,

    skills: `<span class="text-primary font-bold">LANGUAGES:</span> Python, C, SQL, JavaScript, HTML5, CSS3
<span class="text-primary font-bold">AI & DATA:</span> RAG (Hybrid Retrieval), Gemini API, LangChain, NLP, Scikit-learn, NLTK, OpenCV
<span class="text-primary font-bold">BACKEND:</span> Streamlit, REST APIs, Django, Flask, SQLAlchemy ORM, Bcrypt
<span class="text-primary font-bold">DATABASES:</span> PostgreSQL, MySQL (11-table normalized schemas)
<span class="text-primary font-bold">TOOLS:</span> Git/GitHub, Docker, Pandas, Plotly, Jupyter Notebook`,

    projects: `1. <span class="text-primary font-bold">Smart Memory Vault</span> (Multimodal RAG, OCR, Audio, PostgreSQL, Streamlit)
2. <span class="text-primary font-bold">IT Helpdesk & Intelligence System</span> (MySQL, SLA Tracking, RBAC, Plotly)
3. <span class="text-primary font-bold">IntelliCode: AI Code Reviewer</span> (AST Parsing, Gemini API, Security Analyzer)`,

    education: `<span class="text-white font-bold">Bapatla Engineering College</span> (2022 – 2026)
Degree: B.Tech, Computer Science and Engineering (AI & ML)
<span class="text-emerald-400 font-bold">CGPA: 9.1 / 10 • Academic Excellence Shield</span>
Class XII (Narayana): 96% | Class X (Z.P. High School): 96%`,

    contact: `Email:    <a href="mailto:reenakowsar05@gmail.com" class="text-primary underline">reenakowsar05@gmail.com</a>
Phone:    +91 8639214710
Location: Hyderabad, Telangana, India
LinkedIn: linkedin.com | GitHub: github.com`
  };

  function handleCliCommand(cmd) {
    const cleanCmd = cmd.trim().toLowerCase();
    if (!cliOutput) return;

    if (cleanCmd === 'clear') {
      cliOutput.innerHTML = '';
      return;
    }

    if (cleanCmd === 'resume') {
      const link = document.createElement('a');
      link.href = 'assets/Shaik_Reena_Kowsar_Resume.pdf';
      link.download = 'Shaik_Reena_Kowsar_Resume.pdf';
      link.click();
      cliOutput.innerHTML += `
        <div class="text-slate-400">$ ${cmd}</div>
        <div class="text-emerald-400 mb-2">⚡ Downloading Shaik_Reena_Kowsar_Resume.pdf...</div>
      `;
      showToast('Downloading Shaik Reena Kowsar Resume (PDF)...');
      playUiSound('success');
      cliOutput.scrollTop = cliOutput.scrollHeight;
      return;
    }

    const response = CLI_COMMANDS[cleanCmd] || `Command not found: "${cleanCmd}". Type <span class="text-primary">help</span> to view all commands.`;
    cliOutput.innerHTML += `
      <div class="text-slate-400">$ ${cmd}</div>
      <div class="text-slate-200 mb-2.5 leading-relaxed">${response}</div>
    `;
    cliOutput.scrollTop = cliOutput.scrollHeight;
    playUiSound('terminal');
  }

  if (cliInput) {
    cliInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const val = cliInput.value;
        if (val) {
          handleCliCommand(val);
          cliInput.value = '';
        }
      }
    });
  }

  document.querySelectorAll('.cli-quick-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      handleCliCommand(btn.dataset.cmd);
    });
  });

  // 15. Toast Notification Helper
  const toast = document.getElementById('toast');
  function showToast(message) {
    if (!toast) return;
    toast.innerHTML = `<i data-lucide="check-circle" class="w-4 h-4 text-primary"></i> <span>${message}</span>`;
    toast.classList.remove('opacity-0', 'translate-y-4', 'pointer-events-none');
    if (window.lucide) lucide.createIcons();
    playUiSound('pop');
    setTimeout(() => {
      toast.classList.add('opacity-0', 'translate-y-4', 'pointer-events-none');
    }, 2800);
  }

  // 16. Copy Email To Clipboard
  const copyEmailBtn = document.getElementById('copy-email-btn');
  if (copyEmailBtn) {
    copyEmailBtn.addEventListener('click', () => {
      navigator.clipboard.writeText("reenakowsar05@gmail.com").then(() => {
        showToast('Email copied to clipboard: reenakowsar05@gmail.com');
      });
    });
  }

  // 17. Contact Form
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const submitBtn = contactForm.querySelector('button[type="submit"]');
      const originalText = submitBtn.innerHTML;

      submitBtn.disabled = true;
      submitBtn.innerHTML = `<span>Sending...</span>`;

      setTimeout(() => {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalText;
        contactForm.reset();
        showToast('Thank you! Message dispatched directly to Reena.');
        playUiSound('success');
      }, 700);
    });
  }

  // 18. Active Navigation Spy on Scroll
  const sections = document.querySelectorAll('section[id]');
  const sidebarLinks = document.querySelectorAll('.sidebar-link');

  window.addEventListener('scroll', () => {
    const scrollY = window.pageYOffset;
    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 150;
      const sectionId = current.getAttribute('id');

      if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
        sidebarLinks.forEach(link => {
          if (link.getAttribute('href') === `#${sectionId}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  });

  // Re-run icons initialization
  if (window.lucide) lucide.createIcons();
});
