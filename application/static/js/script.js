document.addEventListener("DOMContentLoaded", function () {
    const demoElement = document.getElementById("demo");
    const myButton = document.getElementById("myButton");
    const userInfoForm = document.getElementById("userInfoForm");

    // Function to handle button click
    myButton.addEventListener("click", function () {
        // Hide the button and show the first input field (Name)
        myButton.style.display = "none";
        document.getElementById("userInfoForm").style.display = "block";
        document.getElementById("userName").style.display = "block";
        document.getElementById("nextButton1").style.display = "block";
    });

    // Function to handle Next button 1 click (Name to Last Name)
    document.getElementById("nextButton1").addEventListener("click", function () {
        // Hide the Name input and show the Last Name input
        document.getElementById("userName").style.display = "none";
        document.getElementById("nextButton1").style.display = "none";

        document.getElementById("userLastName").style.display = "block";
        document.getElementById("nextButton2").style.display = "block";
    });

    // Function to handle Next button 2 click (Last Name to Date of Birth)
    document.getElementById("nextButton2").addEventListener("click", function () {
        // Hide the Last Name input and show the Date of Birth input
        document.getElementById("userLastName").style.display = "none";
        document.getElementById("nextButton2").style.display = "none";

        document.getElementById("userDOB").style.display = "block";
        document.getElementById("submitButton").style.display = "block";
    });

    // Function to handle form submission
    userInfoForm.addEventListener("submit", function (event) {
        event.preventDefault();
        const userName = document.getElementById("userName").value;
        const userLastName = document.getElementById("userLastName").value;
        const userDOB = document.getElementById("userDOB").value;

        // Validate and format the date of birth
        const dateOfBirth = new Date(userDOB);
        if (!isNaN(dateOfBirth.getTime())) {
            // Display the collected information
            demoElement.textContent = `Name: ${userName}, Last Name: ${userLastName}, Date of Birth: ${userDOB}`;
        } else {
            demoElement.textContent = "Invalid date of birth format.";
        }
    });
});
