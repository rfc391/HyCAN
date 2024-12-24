
import logging

logging.basicConfig(filename='audit.log', level=logging.INFO)

def log_user_action(action, user_id):
    logging.info(f"User {user_id} performed action: {action}")
