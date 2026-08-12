"""HTTP entrypoint for container deployments. Reuses the mcp object from server.py unchanged."""
from yfmcp.server import mcp

# Set host/port directly on the settings object — env vars alone aren't reliable
# across all FastMCP versions because the Settings may have a different env prefix.
mcp.settings.host = "0.0.0.0"
mcp.settings.port = 3000

mcp.run(transport="streamable-http")
