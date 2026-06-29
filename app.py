from flask import Flask, render_template
import socket
from datetime import datetime
import platform

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        current_time=datetime.now().strftime("%d %B %Y | %I:%M:%S %p"),
        os_name=platform.system(),
        python_version=platform.python_version(),
        version="v1.0.1",
        environment="Production",
        status="LIVE"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)