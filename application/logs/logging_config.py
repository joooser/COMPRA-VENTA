# logging_config.py
import logging

def setup_logging():
    logging.basicConfig(filename='application/logs/app.log', level=logging.INFO)

    # You can add more configuration here if needed

# You can also set up the logger directly in the module scope if you prefer
# logging.basicConfig(filename='app.log', level=logging.INFO)