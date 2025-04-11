from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        number = int(request.form.get("number"))
        result = f"🔢 Square of {number} is {number**2}"
    return render_template_string("""
    <h2>🧠 Smart Flask Calculator</h2>
    <form method="post">
        Enter a number: <input name="number" type="number" required>
        <input type="submit" value="Calculate">
    </form>
    {% if result %}
      <p><strong>{{ result }}</strong></p>
    {% endif %}
    """ , result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
