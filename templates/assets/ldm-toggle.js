document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('mode-toggle-container');
  const themes = ['light', 'mono', 'dark'];

  container.addEventListener('click', () => {
    // 1. Trigger animation
    container.classList.add('animate');

    // 2. Cycle theme
    const currentTheme = document.body.getAttribute('data-theme') || 'light';
    const nextTheme = themes[(themes.indexOf(currentTheme) + 1) % themes.length];

    document.body.setAttribute('data-theme', nextTheme);
    localStorage.setItem('theme', nextTheme);

    // 3. Reset animation
    setTimeout(() => {
      container.classList.remove('animate');
    }, 500); // 0.4s transition + 0.1s max delay
  });

  // Load saved theme
  const saved = localStorage.getItem('theme');
  if (saved) document.body.setAttribute('data-theme', saved);
});
