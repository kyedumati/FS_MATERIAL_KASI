document.querySelector("form").onsubmit = () => {
  // Bug 1: no preventDefault — page reloads
  const email = document.querySelector("#email").value;
  // Bug 2: weak check
  if (email) alert("ok");
};
