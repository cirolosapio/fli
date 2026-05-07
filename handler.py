from mangum import Mangum
from fli.mcp.server import create_http_app   # aggiusta il path se diverso

app = create_http_app()   # oppure importa direttamente l'app FastAPI
handler = Mangum(app, lifespan="off")