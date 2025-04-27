from flask import Flask, request, jsonify
import os
import base64

app = Flask(__name__)

# The encryption key is stored as base64 and obfuscated
ENCODED_KEY_PART = os.environ.get("ENCODED_KEY_PART", "TXJHYWRodmlp")  # Default: base64 for "MrGadhvii"

# Value to add to each byte for additional obfuscation
SHIFT_VALUE = int(os.environ.get("SHIFT_VALUE", "143"))

# Secret token for authentication - change in Vercel environment
SECRET_TOKEN = os.environ.get("SECRET_TOKEN", "MrGadhvii")

@app.route('/api/key', methods=['GET', 'OPTIONS'])
def key_handler():
    # Handle CORS preflight request
    if request.method == 'OPTIONS':
        return build_cors_response({})
        
    # Check auth token
    auth_header = request.headers.get('Authorization', '')
    if not auth_header.startswith('Bearer ') or auth_header[7:] != SECRET_TOKEN:
        return build_cors_response({"error": "Unauthorized"}, status=401)
    
    # Return encoded key data
    return build_cors_response({
        "encoded": ENCODED_KEY_PART,
        "shift": SHIFT_VALUE
    })

def build_cors_response(data, status=200):
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Authorization, Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
    response.status_code = status
    return response

# Vercel needs this handler
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return key_handler() 
