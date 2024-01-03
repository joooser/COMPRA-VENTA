# main.py
from questions import function_from_questions_buyer
from seller_answers import function_from_seller_answers
from buyer_answers import function_from_questions_seller
from transform_answers import function_from_transform_answers
from create_pdf import create_pdf

def main():
    function_from_questions_buyer()
    function_from_questions_seller()
    function_from_seller_answers()
    function_from_transform_answers()
    create_pdf("output.pdf")

if __name__ == "__main__":
    main()