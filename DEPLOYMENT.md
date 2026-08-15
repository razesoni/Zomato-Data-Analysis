Containerization and Streamlit Community Cloud deployment

This document explains how to run the Streamlit dashboard locally using Docker / docker-compose and how to deploy the app to Streamlit Community Cloud (Streamlit Sharing).

1) Run locally with Docker

Prerequisites: Docker and docker-compose installed.

Build the image:

    docker build -t zomato-eda:latest .

Run the container:

    docker run --rm -p 8501:8501 -v "$(pwd)/data:/app/data" zomato-eda:latest

Or using docker-compose (recommended during development):

    docker-compose up --build

Open http://localhost:8501 in your browser.

Notes:
- The container exposes port 8501 and mounts the repository and the data directory so you can change code and data without rebuilding.
- The app expects raw CSV files in data/raw/ (e.g. data/raw/zomato-dataset.csv and data/raw/Country-Code.csv). You can place them locally and they will be available inside the container.

2) Deploy to Streamlit Community Cloud (Streamlit Sharing)

Streamlit Community Cloud runs apps directly from a GitHub repository and does not use a Dockerfile. To deploy the app there:

- Ensure requirements.txt is present (this repository already has one).
- Ensure the Streamlit app file is in the repository root (app.py exists).
- Commit and push your changes to GitHub.

Then:
- Visit https://share.streamlit.io/ and sign in with your GitHub account.
- Click "New app" → choose the repository `razesoni/Zomato-Data-Analysis`, branch `main` (or the branch you pushed to), and the main file `app.py`.
- Click "Deploy". Streamlit will install packages from requirements.txt and launch the app.

Important:
- Streamlit Community Cloud does not use Docker images. The Dockerfile is for local development or deploying to other container platforms (Cloud Run, ECS, etc.).
- If your app requires large data files, consider hosting them externally (S3, GCS) or use Git LFS; the free Streamlit Cloud instance has storage limits.

3) Troubleshooting

- If Streamlit fails to start on the cloud, check the "Logs" on the app page — common issues are missing dependencies or missing data files.
- For local Docker issues, run `docker-compose logs -f` to inspect output.
