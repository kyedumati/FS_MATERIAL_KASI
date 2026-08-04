export function isValidEmail(email) {
  return typeof email === "string" && email.includes("@") && email.includes(".");
}

export function validate(name, email) {
  const errors = [];
  if (!name.trim()) errors.push("Name is required");
  if (!isValidEmail(email)) errors.push("Enter a valid email");
  return errors;
}

const form = document.querySelector("#contact");
const out = document.querySelector("#errors");
if (form) {
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const name = document.querySelector("#name").value;
    const email = document.querySelector("#email").value;
    const errors = validate(name, email);
    out.textContent = errors.join(". ");
    if (!errors.length) out.textContent = "Looks good (demo — not sent).";
  });
}
