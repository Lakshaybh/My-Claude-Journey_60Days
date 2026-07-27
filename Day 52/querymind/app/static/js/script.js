const schemaInput = document.getElementById("schema-input");
const questionInput = document.getElementById("question-input");
const generateBtn = document.getElementById("generate-btn");
const btnLabel = generateBtn.querySelector(".btn-label");
const errorMessage = document.getElementById("error-message");
const resultSection = document.getElementById("result-section");
const sqlOutput = document.getElementById("sql-output");
const explanationOutput = document.getElementById("explanation-output");
const warningOutput = document.getElementById("warning-output");
const copyBtn = document.getElementById("copy-btn");
const copyBtnLabel = document.getElementById("copy-btn-label");

function showError(message) {
  errorMessage.textContent = message;
  errorMessage.style.display = "block";
}

function clearError() {
  errorMessage.textContent = "";
  errorMessage.style.display = "none";
}

function showResult(sql, explanation, warning) {
  sqlOutput.textContent = sql;
  explanationOutput.textContent = explanation;

  if (warning) {
    warningOutput.textContent = warning;
    warningOutput.style.display = "block";
  } else {
    warningOutput.textContent = "";
    warningOutput.style.display = "none";
  }

  resultSection.style.display = "block";
}

function setLoading(isLoading) {
  generateBtn.disabled = isLoading;
  generateBtn.setAttribute("aria-busy", isLoading ? "true" : "false");
  generateBtn.classList.toggle("is-loading", isLoading);
  btnLabel.textContent = isLoading ? "Generating..." : "Generate SQL";
}

generateBtn.addEventListener("click", async () => {
  const schemaText = schemaInput.value.trim();
  const question = questionInput.value.trim();

  clearError();
  resultSection.style.display = "none";

  if (!schemaText) {
    showError("Please paste a schema first.");
    schemaInput.focus();
    return;
  }
  if (!question) {
    showError("Please type a question first.");
    questionInput.focus();
    return;
  }

  setLoading(true);

  try {
    const res = await fetch("/api/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ schema_text: schemaText, question: question }),
    });

    const data = await res.json();

    if (!res.ok) {
      showError(data.detail || "Something went wrong. Please try again.");
      return;
    }

    showResult(data.sql, data.explanation, data.warning);
    resultSection.scrollIntoView({ behavior: "smooth", block: "nearest" });
  } catch (err) {
    showError("Could not reach the server. Please check your connection and try again.");
  } finally {
    setLoading(false);
  }
});

copyBtn.addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(sqlOutput.textContent);
    copyBtnLabel.textContent = "Copied!";
    copyBtn.classList.add("copied");
    setTimeout(() => {
      copyBtnLabel.textContent = "Copy SQL";
      copyBtn.classList.remove("copied");
    }, 1500);
  } catch (err) {
    showError("Could not copy to clipboard. Please select and copy the text manually.");
  }
});

questionInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    generateBtn.click();
  }
});
