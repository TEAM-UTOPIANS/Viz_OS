# Vercel Deployment Guide for VizOS

## Files Created/Modified for Vercel

1. **`vercel.json`** - Vercel configuration file
2. **`api/index.py`** - Serverless function wrapper for Flask app
3. **`requirements.txt`** (root level) - Python dependencies for Vercel
4. **`.vercelignore`** - Files to exclude from deployment

## Deployment Steps

1. Make sure all changes are committed to git
2. Push to GitHub repository
3. In Vercel dashboard:
   - Import your GitHub repository
   - Vercel will auto-detect the Python configuration
   - Deploy

## Important Notes

- The Flask app is wrapped in a serverless function at `api/index.py`
- All routes are proxied through the Flask app
- Static files (frontend) are served by Flask
- Make sure the root `requirements.txt` is present (it is)

## Troubleshooting

If you still get 404 errors:
1. Check Vercel build logs for errors
2. Ensure all dependencies are in `requirements.txt`
3. Verify the `api/index.py` file is correctly importing the Flask app
4. Check that the project structure matches what's expected

