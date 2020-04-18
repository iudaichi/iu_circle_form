from main import app
import uvicorn
import sys


if __name__ == '__main__':
    port = sys.argv[1]
    uvicorn.run(app, host="0.0.0.0", port=port)
