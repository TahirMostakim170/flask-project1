from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Rangpur, Bangladesh',
    'salary': 'Tk. 10,00,000'
}, {
    'id': 2,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Tk. 12,00,000'
}, {
    'id': 3,
    'title': 'Data Analyst',
    'location': 'Rangpur, Bangladesh',
    'salary': 'Tk. 10,00,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'New Y York, USA',
    'salary': '$12000'
}]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
