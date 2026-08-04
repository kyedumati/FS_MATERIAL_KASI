import { useEffect, useState } from "react";

export default function ProductList() {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    let cancelled = false;
    async function load() {
      try {
        const res = await fetch("http://127.0.0.1:8000/api/products/");
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();
        if (!cancelled) setProducts(data);
      } catch (e) {
        if (!cancelled) setError(String(e.message || e));
      }
    }
    load();
    return () => {
      cancelled = true;
    };
  }, []);

  if (error) return <p role="alert">{error}</p>;

  return (
    <ul>
      {products.map((p) => (
        <li key={p.id}>
          {p.name} — ₹{p.price}
        </li>
      ))}
    </ul>
  );
}
