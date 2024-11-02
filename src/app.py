from flask import *
from gpiozero import Servo
from time import sleep

app = Flask(__name__)

# Define GPIO Pins for LEDs
servo = Servo(18)

# Render the HTML page with control interface
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/moveServo", methods=["POST"])
def moveServo():
    pos = request.form.get("pos")

    if (pos == "left"):
        servo.min()
    elif (pos == "center"):
        servo.mid()
    elif (pos == "right"):
        servo.max()

    return "Servo: " + pos

if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=8080)