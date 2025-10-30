from flask import Flask, render_template,request,redirect,url_for
import smtplib
import  os
from dotenv import load_dotenv
load_dotenv()
my_mail=os.environ.get("my_mail")

password=os.environ.get("password")


app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact')
def contact():
    return render_template("contact.html", title='Contact')


@app.route("/submitted", methods=["POST"])
def submitted():
    name=request.form["name"]
    phone=request.form["number"]
    email=request.form["email"]
    message=request.form["message"]

    email_sender(name=name,phone=phone,email_=email,message=message)
    return redirect(url_for('contact'))

def email_sender(name,phone,email_,message):
    global my_mail,password
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_mail, password=password)
        email_body = (f"Subject: Contact\n"
                     f"\n"
                     f"Name: {name}\n"
                     f"Email: {email_}\n"
                     f"Contact: {phone}\n"
                     f"Message: {message}\n")
        connection.sendmail(from_addr=my_mail, to_addrs=os.environ.get("to_address"), msg=email_body)
if __name__ == '__main__':
    app.run(debug=True)