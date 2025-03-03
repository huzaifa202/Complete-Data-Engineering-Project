from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static')
@app.route('/')  # Corrected route for the home page
def home():
    return render_template('index.html')  # Assumes your HTML file is named index.html

@app.route('/save_data', methods=['GET'])
def save_data():
    regno = request.args.get('regno')  # Use .get() to avoid KeyError
    name = request.args.get('name')    # Use .get() and correct the key to 'name'
    standard = request.args.get('class') # Correct key to 'class'
    math = request.args.get('math')
    science = request.args.get('science')
    computer = request.args.get('computer')

    print(regno, name, standard, math, science, computer)

    return redirect(url_for('home'))  # Redirect back to the home page

if __name__ == '__main__':
    app.run(debug=True)  # debug=True for easier development
