## Flask Application Design

### HTML Files

**main.html:**
- Main page of the website.
- Contains two text boxes for user input and a submit button.
- HTML code:
```html
<!DOCTYPE html>
<html>
<head>
  <title>Text Comparison</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container">
    <h1>Text Comparison</h1>
    <form action="/compare" method="post">
      <div class="mb-3">
        <label for="text1" class="form-label">Text 1</label>
        <textarea class="form-control" id="text1" name="text1" rows="5"></textarea>
      </div>
      <div class="mb-3">
        <label for="text2" class="form-label">Text 2</label>
        <textarea class="form-control" id="text2" name="text2" rows="5"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Compare</button>
    </form>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**result.html:**
- Displays the result of the text comparison.
- HTML code:
```html
<!DOCTYPE html>
<html>
<head>
  <title>Comparison Result</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container">
    <h1>Comparison Result</h1>
    <div class="alert alert-success" role="alert">
      Texts are identical.
    </div>
    <div class="alert alert-danger" role="alert">
      Texts are different.
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

### Routes

**app.py:**

```python
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("main.html")

@app.route("/compare", methods=["POST"])
def compare():
    text1 = request.form["text1"]
    text2 = request.form["text2"]
    if text1 == text2:
        return render_template("result.html", result="success")
    else:
        return render_template("result.html", result="danger")

if __name__ == "__main__":
    app.run(debug=True)
```