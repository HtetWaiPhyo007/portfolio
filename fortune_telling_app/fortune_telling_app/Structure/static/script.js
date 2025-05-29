document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("fortune-form");
    const result = document.getElementById("fortune-result");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();
        
        const name = document.getElementById("name").value;
        const birthday = document.getElementById("birthday").value;
        const sex = document.getElementById("sex").value;

        result.textContent = "Reading your fortune... 🔮";
        
        const response = await fetch("/fortune", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name, birthday, sex })
        });

        const data = await response.json();

        result.innerHTML = `<strong>${data.name}</strong>, born on ${data.birthday},<br> your fortune: <em>${data.fortune}</em><br> ⏰ ${data.timestamp}`;
    });
});
