from flask import Flask

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

app = Flask(__name__)

@app.route('/')
def car():
    return 'Welcome to Flatiron Cars'


@app.route('/<model>')
def make(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No model called {model} exists in our catalog."
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)