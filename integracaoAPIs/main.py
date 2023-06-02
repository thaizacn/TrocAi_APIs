from fastapi import FastAPI
from controllers import usuario_controller, plataforma_controller, produto_controller

app = FastAPI()

# Inicializando rotas
app.include_router(usuario_controller.router, prefix="/usuario")
app.include_router(plataforma_controller.router, prefix="/plataforma")
app.include_router(produto_controller.router, prefix="/produto") 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)