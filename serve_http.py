"""HTTP entrypoint for container deployments. Reuses the mcp object from server.py unchanged."""
import uvicorn
from yfmcp.server import mcp

# Use uvicorn directly so host/port are fully under our control,
# bypassing FastMCP's settings object entirely.
uvicorn.run(mcp.streamable_http_app(), host="0.0.0.0", port=3000)
