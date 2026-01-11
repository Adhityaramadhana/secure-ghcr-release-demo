# Portfolio — Secure GHCR Release Demo

**Repository:** https://github.com/Adhityaramadhana/secure-ghcr-release-demo
**Image (GHCR):** ghcr.io/adhityaramadhana/secure-ghcr-release-demo:latest
**Latest tag:** v0.1.0

## Overview
A minimal FastAPI service built to practice a secure DevOps pipeline: automated tests and linting, container builds, vulnerability scanning, SBOM generation, and signed releases to GitHub Container Registry (GHCR).

## What I implemented
- FastAPI endpoints:
  - `GET /health` → returns service health
  - `GET /version` → returns `APP_VERSION` (default: `dev`)
- CI workflow (push/PR):
  - Installs dependencies
  - Lints code with `ruff`
  - Runs unit tests with `pytest`
  - Builds a Docker image
  - Runs Trivy vulnerability scan and uploads results to GitHub Security (SARIF)
- Release workflow (tag `v*`):
  - Builds and pushes a multi-arch container image (amd64 + arm64) to GHCR
  - Generates an SBOM (CycloneDX) and attaches it to the GitHub Release
  - Signs the image using Cosign keyless signing (OIDC)

## How to verify
### Run locally (Python)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
PYTHONPATH=. python -m pytest -q
ruff check .
uvicorn app.main:app --reload
```

### Run from GHCR (Docker)
```bash
docker pull ghcr.io/adhityaramadhana/secure-ghcr-release-demo:latest
docker run --rm -p 8000:8000 ghcr.io/adhityaramadhana/secure-ghcr-release-demo:latest
curl http://localhost:8000/health
curl http://localhost:8000/version
```
