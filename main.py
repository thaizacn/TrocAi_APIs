from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import usuario_controller, plataforma_controller, produto_controller

app = FastAPI()

origins = [
    "http://localhost",
    "https://trocai.netlify.app/",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializando rotas
app.include_router(usuario_controller.router, prefix="/usuario")
app.include_router(plataforma_controller.router, prefix="/plataforma")
app.include_router(produto_controller.router, prefix="/produto") 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
