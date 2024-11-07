from flask import Flask, render_template, url_for

app = Flask(__name__)

# Route for page 1
@app.route('/')
def page1():
    return render_template('index.html')

# Route for page 2
@app.route('/scnd')
def page2():
    return render_template('scnd.html')

@app.route('/third')
def page3():
    return render_template('third.html')

if __name__ == "__main__":
    app.run(debug=True)
