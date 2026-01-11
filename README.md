# Secure GHCR Release Demo

![CI](https://github.com/Adhityaramadhana/secure-ghcr-release-demo/actions/workflows/ci.yml/badge.svg)

Minimal FastAPI service used to practice a secure DevOps workflow: tests + lint, container build, vulnerability scanning, SBOM generation, and signed releases to GitHub Container Registry (GHCR).

## Endpoints
- GET /health
- GET /version

## Run locally (Python)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
PYTHONPATH=. pytest -q
ruff check .
uvicorn app.main:app --reload
```

## Container image (GHCR)
```bash
docker pull ghcr.io/adhityaramadhana/secure-ghcr-release-demo:latest
docker run --rm -p 8000:8000 ghcr.io/adhityaramadhana/secure-ghcr-release-demo:latest
curl http://localhost:8000/health
curl http://localhost:8000/version
```
