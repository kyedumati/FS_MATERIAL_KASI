export async function loadProducts(url) {
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`HTTP ${res.status}`);
  }
  return res.json();
}

// Django side reminder: install django-cors-headers and allow Vite origin.
