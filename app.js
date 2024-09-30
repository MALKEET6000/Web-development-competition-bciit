// Handle user registration
document
  .getElementById("registerForm")
  .addEventListener("submit", async (e) => {
    e.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:5000/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    const result = await response.json();
    alert(result.message);
  });

// Handle adding a student
document.getElementById("studentForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const name = document.getElementById("studentName").value;

  const response = await fetch("http://127.0.0.1:5000/add_student", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name }),
  });

  const result = await response.json();
  alert(result.message);
});

// Handle adding a grade
document.getElementById("gradeForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const studentId = document.getElementById("studentId").value;
  const score = document.getElementById("score").value;

  const response = await fetch("http://127.0.0.1:5000/add_grade", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ student_id: studentId, score }),
  });

  const result = await response.json();
  alert(result.message);
});

// Handle viewing grades
document
  .getElementById("viewGradesButton")
  .addEventListener("click", async () => {
    const studentId = document.getElementById("viewStudentId").value;

    const response = await fetch(`http://127.0.0.1:5000/grades/${studentId}`);
    const grades = await response.json();

    const gradesList = document.getElementById("gradesList");
    gradesList.innerHTML = ""; // Clear previous grades
    grades.forEach((grade) => {
      const li = document.createElement("li");
      li.textContent = `Grade ID: ${grade.id}, Score: ${grade.score}`;
      gradesList.appendChild(li);
    });
  });
