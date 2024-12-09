from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the HTML form
    return render_template_string(open('base.html').read())

@app.route('/fetch', methods=['POST'])
def fetch():
    url = request.form.get('url')
    try:
        # Fetch the content of the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        content = response.text
        return f"<h1>Content of {url}</h1><pre>{content}</pre>"
    except requests.exceptions.RequestException as e:
        return f"<h1>Error fetching the webpage</h1><p>{str(e)}</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
