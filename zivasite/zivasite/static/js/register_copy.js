const usernameField = document.querySelector("#usernameField");
const feedBackArea = document.querySelector(".invalid_feedback");
const emailField = document.querySelector("#emailField");
const emailFeedBackArea = document.querySelector(".emailFeedbackArea");
const passwordField = document.querySelector("#passwordField");
const validUserInput = document.querySelector(".validUserInput");
const showPasswordToggle = document.querySelector(".showPasswordToggle");
const submitButton = document.querySelector(".submit-btn");


const handleTogglePassword= (e)=>{
    if (showPasswordToggle.textContent == "SHOW"){
        showPasswordToggle.textContent= "HIDE";
        passwordField.setAttribute('type', 'text');
    }else {
        showPasswordToggle.textContent= "SHOW";
        passwordField.setAttribute('type', 'password');
    }
};

showPasswordToggle.addEventListener("click", handleTogglePassword);


emailField.addEventListener("keyup", (e) => {
    const emailVal = e.target.value;

    emailField.classList.remove("is-invalid");
    emailFeedBackArea.style.display = "none";


    if (emailVal.length > 0) {
        fetch("/authentication/validate_email", {
                body: JSON.stringify({ email: emailVal }),
                method: "POST",
            })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);
                if (data.email_error) {
                    submitButton.disabled= true;
                    emailField.classList.add("is-invalid");
                    emailFeedBackArea.style.display = "block";
                    emailFeedBackArea.innerHTML = `<p>${data.email_error}</p>`;
                }else{
                    submitButton.removeAttribute('disabled');
                }

            });
    }
});


usernameField.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;

    validUserInput.style.display="block";
    validUserInput.textContent=(`Checking ${usernameVal}`);

    usernameField.classList.remove("is-invalid");
    feedBackArea.style.display = "none";


    if (usernameVal.length > 0) {
        fetch("/authentication/validate_username", {
                body: JSON.stringify({
                    username: usernameVal
                }),
                method: "POST",
            })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);
                validUserInput.style.display="none";
                if (data.username_error) {
                    submitButton.disabeld= true;
                    usernameField.classList.add("is-invalid");
                    feedBackArea.style.display = "block";
                    feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
                }else{
                    submitButton.removeAttribute('disabled');
                }

            });
    }
});