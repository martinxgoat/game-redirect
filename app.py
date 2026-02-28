from flask import Flask, render_template_string, request, session

app = Flask(__name__)
app.secret_key = "ig_pfp_2026"

QUESTIONS = [
    "Always feel understood or always feel appreciated?",
    "Know when you’re going to die or how you’re going to die?",
    "Give up social media forever or movies/TV forever?"
]

# Usernames and unique IDs for random avatars
FAKE_USERS = [
    ("lexi_sky", 1), ("jaden.vibe", 2), ("sarah_xo", 3), 
    ("king_dave", 4), ("mitch_99", 5)
]

STYLE = """
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    body { background: #000; color: #fff; font-family: -apple-system, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
    .card { background: #121212; border: 1px solid #333; padding: 25px; border-radius: 12px; width: 90%; max-width: 360px; text-align: center; }
    .ig-text { background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold; font-size: 22px; margin-bottom: 20px; display: block; }
    .btn { display: block; width: 100%; padding: 14px; margin: 10px 0; border: 1px solid #363636; border-radius: 10px; background: #262626; color: #fff; cursor: pointer; font-size: 14px; }
    table { width: 100%; margin-top: 15px; border-collapse: collapse; }
    td { padding: 10px 0; border-bottom: 1px solid #262626; vertical-align: middle; }
    .pfp { width: 35px; height: 35px; border-radius: 50%; margin-right: 10px; vertical-align: middle; border: 1px solid #333; }
    .username { color: #fff; font-size: 14px; font-weight: 600; }
    .follow-btn { background: #0095f6; color: white; border: none; padding: 6px 12px; border-radius: 8px; font-weight: 600; font-size: 12px; float: right; cursor: pointer; margin-top: 5px; }
    .following { background: #363636; color: #efefef; }
</style>
<script>
    function follow(btn) {
        btn.innerText = "Following";
        btn.style.background = "#363636";
    }
</script>
"""

@app.route('/', methods=['GET', 'POST'])
def play():
    if 'idx' not in session: session['idx'] = 0
    if request.method == 'POST':
        session['idx'] += 1
        if session['idx'] >= len(QUESTIONS):
            session.clear()
            rows = "".join([f'''
                <tr>
                    <td>
                        <img src="https://i.pravatar.cc/150?u={uid}" class="pfp">
                        <span class="username">@{u}</span>
                        <button class="follow-btn" onclick="follow(this)">Follow</button>
                    </td>
                </tr>''' for u, uid in FAKE_USERS])
            return render_template_string(STYLE + f'<div class="card"><span class="ig-text">Leaderboard</span><table>{rows}</table><a href="/" style="color:#8e8e8e; display:block; margin-top:20px; text-decoration:none; font-size:12px;">Play Again</a></div>')

    return render_template_string(STYLE + """
        <div class="card">
            <span class="ig-text">Would You Rather</span>
            <p style="color:#8e8e8e; font-size: 12px;">Question {{ q_num + 1 }} of 3</p>
            <h2 style="font-size: 18px; margin: 25px 0;">{{ question }}</h2>
            <form method="POST">
                <button class="btn">Option A</button>
                <button class="btn">Option B</button>
            </form>
        </div>
    """, question=QUESTIONS[session['idx']], q_num=session['idx'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
