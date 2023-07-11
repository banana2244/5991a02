from flask import Flask, jsonify, request
import random

app = Flask(__name__)

jokes = [
    "What do you call a fake noodle? An impasta!",
    "What do you call an alligator in a vest? An investigator!",
    "What do you call a pile of cats? A meowtain!",
    "What do you call a pig that does karate? A pork chop!",
    "What do you call a funny mountain? Hill-arious!",
    "What do you call a cow with no legs? Ground beef!",
    "What do you call a cow with two legs? Lean beef!",
    "What do you call a cow with all of its legs? High steaks!",
    "What do you call a cow that plays an instrument? A moo-sician!",
    "What do you call a cow that just had a baby? Decalfinated!",
    "What do you call a chicken staring at a piece of lettuce? A chicken sees-a salad!",
    "What do you call a cow eating grass? A lawn moo-er!",
    "What do you call a cow with a twitch? Beef jerky!",
]

@app.route('/joke/', methods=['GET'])
def le_funny():
    num = int(request.args.get('num', 1))
    return jsonify({"Joke": random.sample(jokes, num)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
