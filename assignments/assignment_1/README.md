# Assignment 1: Simple Flask API

Super simple Flask API - just baby steps!

## Files

- `app.py` - Simple Flask example
- `app1.py` - FastAPI example

## How to Run

### Flask (app.py)
```bash
pip3 install Flask
python3 app.py
```

Visit: http://127.0.0.1:5000

### FastAPI (app1.py)
```bash
pip3 install fastapi uvicorn
uvicorn app1:app --reload
```

Visit: http://127.0.0.1:8000

## Test the Endpoints

### In Browser:
- `http://127.0.0.1:5000/` - Home
- `http://127.0.0.1:5000/dashboard` - Dashboard
- `http://127.0.0.1:5000/user/sriya` - Get user

### Using curl:
```bash
# Test add endpoint
curl -X POST http://127.0.0.1:5000/add \
  -H "Content-Type: application/json" \
  -d '{"a": 5, "b": 3}'
```

That's it! Super simple! 🎉
