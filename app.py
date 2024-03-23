from flask import Flask, render_template, request, redirect, url_for, session
import csv
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Function to save user data to CSV file
def save_to_csv(data):
    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Function to read user data from CSV file
def read_from_csv():
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        users = [row for row in reader]
    return users

@app.route('/')
def home():
    return render_template('home.html')

role = ""
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # name = request.form['name']
        # email = request.form['email']
        # hobbies = request.form['hobbies']
        # location = request.form['location']
        role = request.form['role']
        print(role)
        # save_to_csv([name, email, hobbies, location, role])
        if role == "caregiver":
            return redirect(url_for('caretaker'))
        else:
            return redirect(url_for("caretaker"))
    return render_template('signup.html')

@app.route('/caretaker', methods=['GET', 'POST'])
def caretaker():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        hobbies = request.form['hobbies']
        location = request.form['location']
        # role = request.form['role']
        save_to_csv([name, email, hobbies, location, "caretaker"])
        return redirect(url_for('login'))
    return render_template('caretaker.html')










@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        # Check if user exists in CSV file
        users = read_from_csv()
        for user in users:
            if user[1] == email:  # Assuming email is stored at index 1
                # Set session variables
                session['name'] = user[0]  # Assuming name is stored at index 0
                session['email'] = user[1]
                session['role'] = user[4]   # Assuming role is stored at index 4
                return redirect(url_for('matches'))
        # If user not found, redirect back to login page with a message
        return render_template('login.html', message='Invalid email. Please try again.')
    return render_template('login.html')

@app.route('/matches')
def matches():
    if 'email' not in session:
        return redirect(url_for('login'))
    users = read_from_csv()
    # Implement matching algorithm here
    # For simplicity, let's just pass all users to the template
    return render_template('matches.html', users=users)

@app.route('/chat/<recipient_email>')
def chat(recipient_email):
    if 'email' not in session:
        return redirect(url_for('login'))
    recipient_name = None
    users = read_from_csv()
    for user in users:
        if user[1] == recipient_email:
            recipient_name = user[0]
            break
    return render_template('chat.html', recipient_name=recipient_name, recipient_email=recipient_email)

@socketio.on('send_message')
def handle_message(data):
    sender_email = session['email']
    recipient_email = data['recipient_email']
    message = data['message']
    # You can implement message handling logic here, such as saving to database
    emit('receive_message', {'sender_email': sender_email, 'message': message}, room=recipient_email)
    # Also, let's send the message to the sender as well
    emit('receive_message', {'sender_email': sender_email, 'message': message}, room=sender_email)

if __name__ == '__main__':
    socketio.run(app, debug=True)
