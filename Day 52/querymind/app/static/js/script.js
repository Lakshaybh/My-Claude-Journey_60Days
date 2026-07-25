const schemaInput = document.getElementById("schema-input");
const questionInput = document.getElementById("question-input");
const generateBtn = document.getElementById("generate-btn");
const errorMessage = document.getElementById("error-message");
const resultSection = document.getElementById("result-section");
const sqlOutput = document.getElementById("sql-output");
const explanationOutput = document.getElementById("explanation-output");
const warningOutput = document.getElementById("warning-output");
const copyBtn = document.getElementById("copy-btn");
const copyConfirmation = document.getElementById("copy-confirmation");

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

generateBtn.addEventListener("click", async () => {
  const schemaText = schemaInput.value.trim();
  const question = questionInput.value.trim();

  clearError();
  resultSection.style.display = "none";

  if (!schemaText) {
    showError("Please paste a schema first.");
    return;
  }
  if (!question) {
    showError("Please type a question first.");
    return;
  }

  generateBtn.disabled = true;
  generateBtn.textContent = "Generating...";

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
  } catch (err) {
    showError("Could not reach the server. Please try again.");
  } finally {
    generateBtn.disabled = false;
    generateBtn.textContent = "Generate SQL";
  }
});

copyBtn.addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(sqlOutput.textContent);
    copyConfirmation.style.display = "block";
    setTimeout(() => {
      copyConfirmation.style.display = "none";
    }, 1500);
  } catch (err) {
    showError("Could not copy to clipboard.");
  }
});
