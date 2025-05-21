from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Endpoint to return a greeting message for the Simple CRM application.
    
    Returns:
        str: A plain text greeting message.
    """
    return "Hello World from Simple CRM!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
