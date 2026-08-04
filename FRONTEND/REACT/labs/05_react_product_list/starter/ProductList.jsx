import { useEffect, useState } from "react";

export default function ProductList() {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    // TODO: fetch http://127.0.0.1:8000/api/products/
    // TODO: setProducts on success; setError on failure
  }, []);

  if (error) return <p role="alert">{error}</p>;

  return (
    <ul>
      {/* TODO: map products to <li> with name and price */}
    </ul>
  );
}
