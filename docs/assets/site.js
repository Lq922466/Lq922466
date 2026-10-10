(() => {
  const select = document.getElementById('theme');
  const apply = value => {
    if (value === 'system') document.documentElement.removeAttribute('data-theme');
    else document.documentElement.dataset.theme = value;
  };
  let saved = 'system';
  try { saved = localStorage.getItem('innnx-theme') || 'system'; } catch (_) {}
  if (!['system', 'light', 'dark'].includes(saved)) saved = 'system';
  apply(saved);
  if (select) {
    select.value = saved;
    select.addEventListener('change', () => {
      apply(select.value);
      try { localStorage.setItem('innnx-theme', select.value); } catch (_) {}
    });
  }
  try {
    localStorage.setItem('innnx-language', document.documentElement.lang.startsWith('zh') ? 'zh' : document.documentElement.lang);
  } catch (_) {}
})();
