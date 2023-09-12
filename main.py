from fastapi import FastAPI

from datetime import datetime, timezone

app = FastAPI()


GITHUB_REPO_URL = "https://github.com/olawuwo-abideen/hng"


@app.get("/api")
async def home(slack_name: str = "olawuwo abideen", track: str = "backend"):
    now = datetime.now()
    return {
        "slack_name": slack_name,
        "current_day": now.strftime("%A"),
        "utc_time": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": "https://github.com/olawuwo-abideen/hng/blob/main/main.py",
        "github_repo_url": GITHUB_REPO_URL,
        "status_code": 200,
    }
