"""HTTP entrypoint for container deployments. Reuses the mcp object from server.py unchanged."""
from yfmcp.server import mcp

mcp.run(transport="streamable-http", host="0.0.0.0", port=3000)
