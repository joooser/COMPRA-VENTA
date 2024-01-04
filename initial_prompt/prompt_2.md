Task: Build an App, it will write a legal contract of a car sale between 2 persons, it will recieve identification from the 2 persons, the data about the car that it is being sold, the price and the currency, the the app is going to make insertions in a pre-written model contract, the result is a fully complete car-sale contract.
worflow:
    1. the frontend will collect the information about the contractors, the vehicle, the price and the car tittle. this can be done with manual input or uploading photo from the documents (car tittle, sellr id card, buyer id card).
    2. the user it is going to be conducted to the paywall, after payment:
    3. the frontend will send the information to the backend.
    4. on the backend we are going to have running 2 process:
    4.1. the backend will store the data in a database.
    4.2. the backend will insert all the information collected on a document draft, then a draft copy of the document is gonna be showed to the user.
    4.3 after payment the backend will insert a qr code pointing to an url where the pdf document is gonna be stored. And it will create a the new document that is gonna inserted in another database that can be downloadable from the user account in the frontend.

considerations: 
    1. there is no payment processor online at the moment in Venezuela, the paywall will ask to the user the transaction id of the payment, and maybe using selenium or something the app is going to check the veracity of the payment.
    2. all the frontend and UI will be in Spanish.
    3. all the process in the backend must be divided in modules. a module for writing data base, a module for checking payment, a module for create the document, a module for creating the pdf version, and a module for send the response to the backend.
    4. the result pdf document must be a plain pdf, it cannot be editable.
