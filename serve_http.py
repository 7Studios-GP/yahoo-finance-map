"""HTTP entrypoint for container deployments. Reuses the mcp object from server.py unchanged."""
import os

import uvicorn
from mcp.server.transport_security import TransportSecuritySettings

from yfmcp.server import mcp

# server.py builds FastMCP with the default host="127.0.0.1", so the SDK auto-enables
# DNS-rebinding protection scoped to localhost and answers 421 "Invalid Host header"
# for anything arriving via the cluster ingress hostname. That hostname is assigned
# per deployment, so there is no fixed value to allow-list instead.
mcp.settings.transport_security = TransportSecuritySettings(enable_dns_rebinding_protection=False)

# Use uvicorn directly so host/port are fully under our control,
# bypassing FastMCP's settings object entirely.
uvicorn.run(mcp.streamable_http_app(), host="0.0.0.0", port=int(os.environ.get("PORT", "8000")))
