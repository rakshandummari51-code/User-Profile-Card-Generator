from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    profile = None

    if request.method == 'POST':
        profile = {
            'name': request.form['name'],
            'bio': request.form['bio'],
            'image': request.form['image']
        }

    return render_template('index.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)