from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Key Server API is running",
        "endpoints": ["/api/key"],
        "status": "ok"
    })

@app.route('/api')
def api_index():
    return jsonify({
        "message": "API is running. Use /api/key endpoint with proper authentication.",
        "endpoints": ["/api/key"],
        "status": "ok"
    })

# This is needed for Vercel
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) 