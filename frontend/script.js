const form = document.getElementById("creditForm");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const income = document.getElementById("income").value;
    const debt = document.getElementById("debt").value;
    const creditScore = document.getElementById("creditScore").value;

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                income: income,
                debt: debt,
                credit_score: creditScore
            })
        });

        const data = await response.json();

        resultDiv.innerHTML = data.result;

    } catch (error) {
        console.error(error);

        resultDiv.innerHTML =
            "❌ Error connecting to server";
    }
});