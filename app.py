from flask import Flask, request, jsonify

app = Flask(__name__)

# Serve the webpage (the button) at the root URL
@app.route('/')
def index():
    # This could be an HTML file on disk, but let’s just inline it for example’s sake
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Web Page</title>
    </head>
    <body>
        <h1>Click Button to Run Code on the Server</h1>
        <!-- When the button is clicked, send a POST request to /run-code -->
        <button onclick="runCode()">Run Code</button>
        
        <script>
        function runCode() {
            fetch('/run-code', {
                method: 'POST'
            })
            .then(response => response.json())
            .then(data => {
                alert('Server response: ' + data.status);
            })
            .catch(error => console.error('Error:', error));
        }
        </script>
    </body>
    </html>
    """

# This endpoint is called via POST when you click the button
@app.route('/run-code', methods=['POST'])
def run_code():
    # This is where your local code runs.
    # Do anything you want here: read files, run scripts, call functions, etc.
    # For demonstration, we’ll just log something to the console and respond with JSON.
    print("The server just ran some code locally!")
    return jsonify({"status": "Server code was executed!"})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
