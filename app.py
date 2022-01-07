# Import Utilities
from Utilities import get_body_statistics, get_subject_statistics
import flask
from flask_cors import CORS

app = flask.Flask(__name__)
# app.config["DEBUG"] = True
CORS(app)


@app.route("/")
def hello_world():
    return "Hello world!"

# Submit an email Body and Subject and it'll analyze
@app.route('/email_analysis', methods=['POST'])
def email_analyzer():
    request_data = flask.request.get_json()
    if "body" not in request_data.keys():
        message = {
            'status': 400,
            'message': "You must include a 'body' object in the request"
        }
        resp = flask.jsonify(message)
        resp.status_code = 400
        return resp

    if "subject" not in request_data.keys():
        message = {
            'status': 400,
            'message': "You must include a 'subject' object in the request"
        }
        resp = flask.jsonify(message)
        resp.status_code = 400
        return resp

    if request_data["body"] == "":
        body_statistics = {
            "empty": True
        }
    else:
        body_statistics = get_body_statistics(request_data["body"])
    # If subject doesn't exist
    if request_data["subject"] == "":
        subject_statistics = {
            "empty": True
        }
    else:
        subject_statistics = get_subject_statistics(request_data["subject"])

    email_statistics = {
        "body_statistics": body_statistics,
        "subject_statistics": subject_statistics
    }

    message = {
        'status': 200,
        'message': 'OK',
        'email_statistics': email_statistics
    }

    resp = flask.jsonify(message)
    resp.status_code = 200
    return resp


if __name__ == '__main__':
    app.run()
