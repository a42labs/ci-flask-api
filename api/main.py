
from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)

    @app.route('/health')
    def health():
        return jsonify(status="Up")

    @app.route('/restaurantClassifier', methods = ['GET'])
    def restaurantClassifier():

        data = request.json

        if not data:
            res = {"errorMessage": "No data found"}
            return jsonify(res)

        if "restaurantName" not in data:
            res = {"errorMessage": "'restaurantName' key/value not found"}
            return jsonify(res)

        if data["restaurantName"] is None or data["restaurantName"] == "":
            res = {"errorMessage": "'restaurantName' key/value not found"}
            return jsonify(res)


        firstLetterLower = data['restaurantName'][:1].lower()
        res = {"restaurantName": data['restaurantName'], "firstLetterLower": firstLetterLower}

        if firstLetterLower in ('r','s','t','l','n','e'):
            res["score"] = 1.0
        else:
            res["score"] = 0.0

        return jsonify(res)

    return app

if __name__ == '__main__':
    app = create_app()
    # app.run(debug=True)
