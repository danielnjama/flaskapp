from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
application = app
# Configure your Flask app and Mail settings
app.config['SECRET_KEY'] = 'heythereerere'  # for flashing messages
app.config['MAIL_SERVER'] = 'rbx115.truehost.cloud'  # Or any other SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'test@dtechnologys.com'  # Your email
app.config['MAIL_PASSWORD'] = '&OIn[[1{H*0u'  # Your email password or app password
app.config['MAIL_DEFAULT_SENDER'] = 'test@dtechnologys.com'

# Initialize Flask-Mail
mail = Mail(app)







@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        if not name or not email or not message:
            flash('All fields are required!', 'danger')
            return redirect(url_for('contact'))

        try:
            # Create the message
            msg = Message(subject=f"New Contact Us Message from {name}",
                          recipients=['admin@dtechnologys.com'],
                          body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

            # Send the email
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact'))

        except Exception as e:
            flash(f'Error sending email: {str(e)}', 'danger')
            return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
