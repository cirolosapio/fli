from mangum import Mangum
from fli.mcp.server import mcp  # l'oggetto FastMCP si chiama quasi certamente 'mcp'

# fastmcp espone l'app ASGI per il deploy con Mangum
app = mcp.http_app()

handler = Mangum(app, lifespan="off")