export async function loadProducts(url) {
  // Bug 1: missing await
  const res = fetch(url);
  // Bug 2: assuming OK
  return res.json();
}
