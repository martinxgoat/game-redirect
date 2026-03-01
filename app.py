from flask import Flask, render_template, request, jsonify
from vercel_kv import KV

app = Flask(__name__)
kv = KV()

# 15+ Questions
QUESTIONS = [
    {"q": "Have spaghetti for hair", "o": "Have broccoli for ears"},
    {"q": "Be able to fly", "o": "Be invisible"},
    {"q": "Always have to shout", "o": "Always have to whisper"},
    {"q": "Live in a treehouse", "o": "Live in a castle"},
    {"q": "Be a famous actor", "o": "Be a famous singer"},
    {"q": "Travel to the past", "o": "Travel to the future"},
    {"q": "Never eat pizza again", "o": "Never eat burgers again"},
    {"q": "Have a pet dragon", "o": "Have a pet unicorn"},
    {"q": "Only eat sweet food", "o": "Only eat salty food"},
    {"q": "Be the smartest person", "o": "Be the funniest person"},
    {"q": "Always be 10m late", "o": "Always be 20m early"},
    {"q": "Control the weather", "o": "Talk to animals"},
    {"q": "Live without music", "o": "Live without movies"},
    {"q": "Have 10 siblings", "o": "Be an only child"},
    {"q": "Explore the deep ocean", "o": "Explore outer space"}
]

@app.route('/')
def index():
    return render_template('index.html', questions=QUESTIONS)

@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.json
    name = data.get('name', 'Anonymous')
    score = data.get('score', 0)
    # Save to Vercel KV
    kv.zadd('leaderboard', {name: score})
    return jsonify({"status": "success"})

@app.route('/leaderboard')
def get_leaderboard():
    # Get top 15 players
    scores = kv.zrange('leaderboard', 0, 14, desc=True, withscores=True)
    return jsonify(scores)
