Task: Build an App, it will write a legal contract of a car sale between 2 persons, it will recieve identification from the 2 persons, the data about the car that it is being sold, the price and the currency, the the app is going to make insertions in a pre-written model contract, the result is a fully complete car-sale contract in pdf.
users: we are goinig to have 2 type of users, regular user that will pay per document, and power user that pays a monthly fee for unlimited documents.
workflow: 
    1. frontend: 
    1.1. will have user sign up/user login page, profile,  dashboard page, create a new contract page, and a paywall.
        1.1.1. dashboard will have the information about the user, his made documents. 
        1.1.2. the create a new contract page will collect inforation about the contract, legal information from the buyer, the seller, the car, the price of the car and the way the payment is made.
        1.1.3. profile web page will have all the information about the user, email, password prreferences etc.
        1.1.4. signup page will collect the information about the user.
        1.1.5. pay wall will have a form where the user can input the payment information for the document.
    2. backend: 
        2.1. will store all the data collected by the frontend. and it will write the contract with the data provided.
        2.2. it will verify the payment data using selenium to go to banck account to see if the payment was made.
        2.3. it will write the document with the information provided for the user and the draft stored in the backend.
        2.4. it is going to send to the front end dashboard a hyperlink to the pdf copy of the document.


considerations: 
    1. there is no payment processor online at the moment in Venezuela, the paywall will ask to the user the transaction id of the payment, and maybe using selenium or something the app is going to check the veracity of the payment.
    2. all the frontend and UI will be in Spanish.
    3. all the process in the backend must be divided in modules. a module for writing data base, a module for checking payment, a module for create the document, a module for creating the pdf version, and a module for send the response to the backend.
    4. the result pdf document must be a plain pdf, it cannot be editable.
