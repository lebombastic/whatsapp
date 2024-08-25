from flask import Flask, request
import os

app = Flask(__name__)

registered_users = []
waiting_list = []

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.form.get('Body', '').lower()
    user_number = request.form.get('From')

    if 'register me' in incoming_msg:
        if len(registered_users) < 10:
            if user_number not in registered_users:
                registered_users.append(user_number)
                return f"Seat #{len(registered_users)} registered."
            return "You're already registered."
        elif len(waiting_list) < 5:
            if user_number not in waiting_list:
                waiting_list.append(user_number)
                return f"Waiting list position #{len(waiting_list)}."
            return "You're already on the waiting list."
        return "Registration full."

    return "Invalid command."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))