import { useEffect, useState } from "react";

export default function ProductList() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/products/")
      .then((r) => r.json())
      .then(setProducts);
    // Bug: no error handling; CORS may fail silently in UI
  }, []);

  return (
    <ul>
      {products.map((p) => (
        // Bug: missing key
        <li>
          {p.name} — ₹{p.price}
        </li>
      ))}
    </ul>
  );
}
