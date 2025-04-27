from http.server import BaseHTTPRequestHandler
import json
import os
import base64

# The encryption key is stored as base64 and obfuscated
# This will be set in Vercel environment variables
ENCODED_KEY_PART = os.environ.get("ENCODED_KEY_PART", "TXJHYWRodmlp")  # Default: base64 for "MrGadhvii"

# Value to add to each byte for additional obfuscation
SHIFT_VALUE = int(os.environ.get("SHIFT_VALUE", "143"))

# Secret token for authentication - change in Vercel environment
SECRET_TOKEN = os.environ.get("SECRET_TOKEN", "MrGadhvii")

def handler(request, response):
    # Add CORS headers
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
    
    # Handle preflight OPTIONS request
    if request.method == "OPTIONS":
        return {}
    
    # Check for required token in request
    auth_header = request.headers.get("Authorization", "")
    request_token = ""
    
    # Check if token is in Authorization header
    if auth_header.startswith("Bearer "):
        request_token = auth_header[7:]
    
    # Check if token is valid
    if not request_token or request_token != SECRET_TOKEN:
        response.status_code = 401
        return {
            "error": "Unauthorized. Invalid or missing token."
        }
    
    # Return encoded data and shift value for additional security
    return {
        "encoded": ENCODED_KEY_PART,
        "shift": SHIFT_VALUE
    } 