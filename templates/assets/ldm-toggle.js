document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('mode-toggle-container');

  // Custom theme order: Light -> Mono -> Dark
  const themes = ['light', 'mono', 'dark'];

  container.addEventListener('click', () => {
    // Get current theme from body, default to light
    const currentTheme = document.body.getAttribute('data-theme') || 'light';

    // Find index and calculate next (with wrap-around)
    const currentIndex = themes.indexOf(currentTheme);
    const nextIndex = (currentIndex + 1) % themes.length;
    const nextTheme = themes[nextIndex];

    // Apply new theme
    document.body.setAttribute('data-theme', nextTheme);
    localStorage.setItem('theme', nextTheme);

    console.log(`Theme switched to: ${nextTheme}`);
  });

  // Persist preference on page load
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme && themes.includes(savedTheme)) {
    document.body.setAttribute('data-theme', savedTheme);
  }
});
