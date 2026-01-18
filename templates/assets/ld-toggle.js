document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('mode-toggle');
  const body = document.body;

  // 1. Determine initial theme
  const savedTheme = localStorage.getItem('theme');
  const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

  if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
    body.classList.add('dark-mode');
    updateButtonIcon(true);
  }

  // 2. Toggle event listener
  btn.addEventListener('click', () => {
    const isDarkMode = body.classList.toggle('dark-mode');

    // Save preference
    localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');

    updateButtonIcon(isDarkMode);
  });

  function updateButtonIcon(isDark) {
    btn.textContent = isDark ? 'Light Mode' : 'Dark Mode';
  }
});
