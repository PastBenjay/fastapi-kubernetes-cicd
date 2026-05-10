from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI(
    title="Cloud Native DevOps Dashboard",
    description="FastAPI application deployed with Docker, Jenkins, and Kubernetes",
    version="1.0.0"
)

@app.get("/", response_class=HTMLResponse)
def home():

    current_time = datetime.utcnow()

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Dashboard</title>

        <style>
            body {{
                background-color: #0f172a;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
            }}

            .card {{
                background: #1e293b;
                width: 600px;
                margin: auto;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0px 0px 20px rgba(0,0,0,0.4);
            }}

            h1 {{
                color: #38bdf8;
            }}

            p {{
                font-size: 18px;
            }}

            .status {{
                color: #22c55e;
                font-weight: bold;
            }}
        </style>

    </head>

    <body>

        <div class="card">

            <h1>Cloud Native DevOps Dashboard</h1>

            <p class="status">
                Application Running Successfully
            </p>

            <p>
                CI/CD Pipeline with Jenkins, Docker & Kubernetes
            </p>

            <p>
                Deployment Timestamp:
            </p>

            <p>
                {current_time}
            </p>

        </div>

    </body>
    </html>
    """

@app.get("/health")
def health_check():
    return {
        "health": "healthy"
    }