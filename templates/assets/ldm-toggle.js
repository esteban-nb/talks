document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('mode-toggle-container');
  const themes = ['light', 'dark', 'mono'];

  container.addEventListener('click', () => {
    const currentTheme = document.body.getAttribute('data-theme');
    const currentIndex = themes.indexOf(currentTheme);
    const nextIndex = (currentIndex + 1) % themes.length;
    const nextTheme = themes[nextIndex];

    document.body.setAttribute('data-theme', nextTheme);
    localStorage.setItem('theme', nextTheme); // Save preference
  });

  const saved = localStorage.getItem('theme');
  if (saved) document.body.setAttribute('data-theme', saved);
});
