document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('mode-toggle-container');
  const themes = ['light', 'mono', 'dark']; // Light -> Mono -> Dark

  container.addEventListener('click', () => {
    // 1. Reset and trigger animation
    container.classList.remove('clicked');
    void container.offsetWidth;
    container.classList.add('clicked');

    // 2. Cycle theme logic
    const currentTheme = document.body.getAttribute('data-theme') || 'light';
    const nextTheme = themes[(themes.indexOf(currentTheme) + 1) % themes.length];

    document.body.setAttribute('data-theme', nextTheme);
    localStorage.setItem('theme', nextTheme);
  });

  // Load saved preference
  const saved = localStorage.getItem('theme');
  if (saved) document.body.setAttribute('data-theme', saved);
});
