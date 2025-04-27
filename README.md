# Key Server for Vercel

This is a secure key server designed to be deployed on Vercel. It provides an encrypted key part that can be used to decrypt your secure code.

## How to Deploy

1. **Create a GitHub Repository**
   - Create a new private GitHub repository
   - Upload the contents of this `server` directory to the root of your repository

2. **Deploy to Vercel**
   - Go to [vercel.com](https://vercel.com) and sign in
   - Create a new project and import your GitHub repository
   - Configure the build settings:
     - Framework Preset: Other
     - Root Directory: ./
     - Build Command: (leave empty)
     - Output Directory: (leave empty)

3. **Set Environment Variables**
   - Go to Settings > Environment Variables
   - Add the following:
     - `ENCODED_KEY_PART`: Your base64-encoded key part (default: "TXJHYWRodmlp")
     - `SHIFT_VALUE`: Obfuscation value (default: "143")
     - `SECRET_TOKEN`: Authentication token (default: "MrGadhvii")

4. **Redeploy**
   - Go to Deployments and trigger a new deployment

## API Endpoints

- `GET /` - Returns a welcome message
- `GET /api` - Returns API information
- `GET /api/key` - Returns the encoded key part (requires authentication)

## Authentication

All requests to `/api/key` must include an `Authorization` header with a Bearer token:

```
Authorization: Bearer MrGadhvii
```

Replace `MrGadhvii` with your custom token if you changed it in the environment variables. 