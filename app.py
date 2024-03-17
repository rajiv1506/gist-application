from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('gists.html')

@app.route('/gists', methods=['POST'])
def get_gists_for_user():
    github_username = request.form.get('github_username')
    return redirect(url_for('get_gists', username=github_username))

@app.route('/gists/<username>')
def get_gists(username):
    api_url = f'https://api.github.com/users/{username}/gists'

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        gists = response.json()

        for i in gists:
            print(i.keys())

        formatted_gists = [{'id': gist['id'], 'description': gist['description']} for gist in gists]

        return render_template('details.html', github_username=username, gists=formatted_gists)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error fetching Gists: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
