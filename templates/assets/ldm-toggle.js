document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('mode-toggle-container');
  const pyramid = document.getElementById('pyramid');
  const body = document.body;
  const modes = ['light', 'dark', 'mono'];

  // Initial State
  const savedTheme = localStorage.getItem('theme') ||
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');

  body.setAttribute('data-theme', savedTheme);

  // Set initial rotation based on theme
  const rotations = { 'light': 0, 'dark': -120, 'mono': -240 };
  let currentRotation = rotations[savedTheme];
  pyramid.style.transform = `rotateY(${currentRotation}deg)`;

  container.addEventListener('click', () => {
    currentRotation -= 120;
    pyramid.style.transform = `rotateY(${currentRotation}deg)`;

    // Determine next theme
    const index = modes.indexOf(body.getAttribute('data-theme'));
    const nextTheme = modes[(index + 1) % modes.length];

    body.setAttribute('data-theme', nextTheme);
    localStorage.setItem('theme', nextTheme);
  });
});
