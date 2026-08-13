# https://docs.astral.sh/uv/guides/integration/docker/
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS uv

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev --no-editable

ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-editable

FROM python:3.12-slim-bookworm

WORKDIR /app

COPY --from=uv --chown=app:app /app/.venv /app/.venv
# Copy the HTTP entrypoint wrapper (serve_http.py lives in the build stage via ADD . /app)
COPY --from=uv /app/serve_http.py /app/serve_http.py

ENV PATH="/app/.venv/bin:$PATH"
# FastMCP reads these via its Pydantic settings to configure the uvicorn server.
ENV FASTMCP_HOST=0.0.0.0
ENV FASTMCP_PORT=3000

EXPOSE 8000
CMD ["python", "serve_http.py"]
