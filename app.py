from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    username = request.form.get("username")
    return f"""
    <div style='font-family: Arial; text-align: center; margin-top: 50px;'>
        <h2 style='color: #007bff;'>Hello, {username}! 🎉</h2>
        <p>Welcome to the Flask DevOps Pipeline demo.</p>
        <a href="/" style='text-decoration: none; color: white; background: #007bff; padding: 10px 20px; border-radius: 8px;'>Go Back</a>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)

