
    document.addEventListener('DOMContentLoaded', function() {
        document.querySelector('form').addEventListener('submit', function(e) {
            let isValid = true;

            function validateLength(fieldId, minLength, maxLength) {
                const fieldValue = document.getElementById(fieldId).value;
                if (fieldValue.length < minLength || fieldValue.length > maxLength) {
                    isValid = false;
                }
            }

            validateLength('seller_name', 2, 40);
            validateLength('seller_nationality', 1, 50);
            validateLength('seller_id', 2, 10);
            validateLength('seller_address', 1, 100);
            validateLength('vehicle_title_number', 1, 20);
            validateLength('vehicle_form_number', 1, 20);
            validateLength('notary_name', 1, 50);
            validateLength('document_authentication_number', 1, 5);
            validateLength('seller_spouse_name', 1, 40);
            validateLength('seller_spouse_nationality', 1, 50);
            validateLength('seller_spouse_id', 1, 10);
            validateLength('seller_spouse_address', 1, 100);
            validateLength('buyer_name', 1, 40);
            validateLength('buyer_nationality', 1, 50);
            validateLength('buyer_id', 1, 10);
            validateLength('buyer_address', 1, 100);
            validateLength('car_brand', 1, 50);
            validateLength('car_model', 1, 50);
            validateLength('car_plate', 1, 10);
            validateLength('car_engine_serial', 1, 20);
            validateLength('car_chassis_serial', 1, 20);
            validateLength('car_type', 1, 50);
            validateLength('car_color', 1, 20);
            validateLength('car_class', 1, 50);
            validateLength('car_use', 1, 50);
            validateLength('transaction_currency', 1, 20);
            validateLength('payment_instrument', 1, 50);

            // Validate vehicle_price (assuming a positive number is required)
            const vehiclePrice = document.getElementById('vehicle_price').value;
            if (isNaN(vehiclePrice) || parseFloat(vehiclePrice) <= 0) {
                isValid = false;
            }

            // Validate car_year (assuming it's a reasonable year range)
            const carYear = document.getElementById('car_year').value;
            const currentYear = new Date().getFullYear();
            if (isNaN(carYear) || carYear < 1672 || carYear > currentYear) {
                isValid = false;
            }

            if (!isValid) {
                e.preventDefault();
                alert('Some fields do not meet the validation criteria.');
            }
        });
    });