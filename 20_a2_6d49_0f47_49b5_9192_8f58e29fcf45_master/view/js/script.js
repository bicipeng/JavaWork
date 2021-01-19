// JS code goes here
const textForm = document.querySelector("#textForm")
const tableList = document.querySelector("#summaryTable")
if (textForm !== null) {
    textForm.addEventListener("submit", function (e) {
        e.preventDefatult()

        let name = document.querySelector("#name")
        let number = document.querySelector("#mobile")
        let email = document.querySelector("#email")

        if (name.value !== "" && number.value !== "" && email.value !== "") {
            const trElement = document.createElement("tr")
            const nameInput = document.createElement("td")
            const numberInput = document.createElement("td")
            const emailInput = document.createElement("td")

            nameInput.textContent = name.value;
            numberInput.textContent = number.value;
            emailInput.textContent = email.value;

            trElement.appendChild(nameInput)
            trElement.appendChild(numberInput)
            trElement.appendChild(emailInput)
            list.appendChild(trElement)


        }
    })
}