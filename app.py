from flask import Flask, render_template, redirect
import subprocess
import threading

app = Flask(__name__)

# Track if Streamlit has started
streamlit_started = False

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start')
def start_streamlit():
    global streamlit_started
    if not streamlit_started:
        threading.Thread(target=launch_streamlit).start()
        streamlit_started = True
    return redirect("http://localhost:8501", code=302)

def launch_streamlit():
    subprocess.Popen(["streamlit", "run", "Final_UI.py"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

