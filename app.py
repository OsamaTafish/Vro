from flask import Flask, render_template, request, redirect

app = Flask(__name__)

written_text = "Hello World!"

@app.route('/')
def index():
    return render_template("index.html", message=written_text)

@app.route('/add', methods=['POST'])
def add():
    global written_text
    text = request.form.get('text')
    if text:
        written_text = text  
    return redirect('/')  

if __name__ == '__main__':
    app.run(debug=True)
