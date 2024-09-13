import socket
from flask import Flask, request, jsonify
from langchain_email import analyze_email, detect_tone, generate_reply

app = Flask(__name__)

def find_available_port(default_port=5000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(("0.0.0.0", default_port))
        sock.listen(1)
        sock.close()
        return default_port
    except OSError:
        sock.close()
        return 0

@app.route("/generate-reply", methods=["POST"])
def generate_email_reply():
    data = request.json
    email_body = data.get("email_body", "")
    tone_style = data.get("tone_style", "professional")

    email_summary = analyze_email(email_body)

    tone = detect_tone(email_body)

    reply = generate_reply(email_summary, tone, style=tone_style)

    return jsonify({
        "summary": email_summary,
        "tone": tone,
        "reply": reply
    })

if __name__ == "__main__":
    port = find_available_port(default_port=5000)
    app.run(host="0.0.0.0", port=port)