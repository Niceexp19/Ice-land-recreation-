from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reserve', methods=['POST'])
def reserve():
    name = request.form.get('name')
    phone = request.form.get('phone')
    date = request.form.get('date')
    time = request.form.get('time')
    guests = request.form.get('guests')
    package = request.form.get('package')
    requests_ = request.form.get('requests', '')

    # Save to file
    with open('reservations.txt', 'a') as f:
        f.write('================================\n')
        f.write(f'Date Booked: {datetime.now()}\n')
        f.write(f'Name: {name}\n')
        f.write(f'Phone: {phone}\n')
        f.write(f'Visit Date: {date}\n')
        f.write(f'Time: {time}\n')
        f.write(f'Guests: {guests}\n')
        f.write(f'Package: {package}\n')
        f.write(f'Requests: {requests_}\n')

    return render_template('index.html', success=True)

if __name__ == '__main__':
    app.run()
