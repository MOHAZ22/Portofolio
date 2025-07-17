// Smooth scroll effect for nav links
document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    document.querySelector(link.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});

// Simple form submit alert
document.getElementById('contactForm').addEventListener('submit', e => {
  e.preventDefault();
  alert("Thanks for reaching out, I'll reply soon!");
});

// Hire me button scroll to contact
document.getElementById('hireBtn').addEventListener('click', () => {
  document.querySelector('#contact').scrollIntoView({ behavior: 'smooth' });
});
