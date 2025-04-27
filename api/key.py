
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

def handler(request):
    # Check authentication
    auth_header = request.headers.get("Authorization", "")
    
    # Set CORS headers
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, OPTIONS",
        "Access-Control-Allow-Headers": "Authorization, Content-Type",
        "Content-Type": "application/json"
    }
    
    # Handle OPTIONS request for CORS preflight
    if request.method == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": headers,
            "body": ""
        }
    
    # Check token
    if not auth_header.startswith("Bearer ") or auth_header[7:] != SECRET_TOKEN:
        return {
            "statusCode": 401,
            "headers": headers,
            "body": json.dumps({"error": "Unauthorized. Invalid or missing token."})
        }
    
    # Return the key data
    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps({
            "encoded": ENCODED_KEY_PART,
            "shift": SHIFT_VALUE
        })
    } 
