/**
 * Interactive Particle / Constellation Canvas Background
 */

(function initCanvas() {
  const canvas = document.getElementById('bg-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let animationFrameId;
  let width, height;
  let particles = [];
  
  // Mouse position tracker
  const mouse = {
    x: null,
    y: null,
    radius: 140
  };

  window.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
  });

  window.addEventListener('mouseout', () => {
    mouse.x = null;
    mouse.y = null;
  });

  function getThemeColors() {
    return {
      particle: 'rgba(56, 189, 248, 0.4)',
      line: 'rgba(56, 189, 248, 0.1)',
      accent: 'rgba(56, 189, 248, 0.8)'
    };
  }

  function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
    createParticles();
  }

  class Particle {
    constructor() {
      this.x = Math.random() * width;
      this.y = Math.random() * height;
      this.size = Math.random() * 2 + 1;
      this.baseX = this.x;
      this.baseY = this.y;
      this.speedX = (Math.random() - 0.5) * 0.8;
      this.speedY = (Math.random() - 0.5) * 0.8;
      this.density = Math.random() * 20 + 5;
    }

    draw(colors) {
      ctx.fillStyle = colors.particle;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.closePath();
      ctx.fill();
    }

    update() {
      // Normal wandering
      this.x += this.speedX;
      this.y += this.speedY;

      // Screen edge bouncing
      if (this.x < 0 || this.x > width) this.speedX = -this.speedX;
      if (this.y < 0 || this.y > height) this.speedY = -this.speedY;

      // Mouse interactivity (subtle push away)
      if (mouse.x !== null && mouse.y !== null) {
        const dx = mouse.x - this.x;
        const dy = mouse.y - this.y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < mouse.radius) {
          const forceDirectionX = dx / distance;
          const forceDirectionY = dy / distance;
          const maxDistance = mouse.radius;
          const force = (maxDistance - distance) / maxDistance;
          const directionX = forceDirectionX * force * this.density * 0.4;
          const directionY = forceDirectionY * force * this.density * 0.4;

          this.x -= directionX;
          this.y -= directionY;
        }
      }
    }
  }

  function createParticles() {
    particles = [];
    // Adjust density based on screen resolution
    const particleCount = Math.floor((width * height) / 12000);
    const count = Math.min(Math.max(particleCount, 40), 120);

    for (let i = 0; i < count; i++) {
      particles.push(new Particle());
    }
  }

  function connect(colors) {
    const maxDist = 130;
    const maxDistSq = maxDist * maxDist;

    for (let a = 0; a < particles.length; a++) {
      for (let b = a + 1; b < particles.length; b++) {
        const dx = particles[a].x - particles[b].x;
        const dy = particles[a].y - particles[b].y;
        const distSq = dx * dx + dy * dy;

        if (distSq < maxDistSq) {
          const opacity = 1 - (distSq / maxDistSq);
          ctx.strokeStyle = colors.line.replace(/[\d\.]+\)$/, `${opacity * 0.22})`);
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(particles[a].x, particles[a].y);
          ctx.lineTo(particles[b].x, particles[b].y);
          ctx.stroke();
        }
      }
    }
  }

  function animate() {
    ctx.clearRect(0, 0, width, height);
    const colors = getThemeColors();

    for (let i = 0; i < particles.length; i++) {
      particles[i].update();
      particles[i].draw(colors);
    }
    connect(colors);

    animationFrameId = requestAnimationFrame(animate);
  }

  window.addEventListener('resize', () => {
    cancelAnimationFrame(animationFrameId);
    resize();
    animate();
  });

  // Pause when tab is inactive to preserve battery
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      cancelAnimationFrame(animationFrameId);
    } else {
      animate();
    }
  });

  resize();
  animate();
})();
