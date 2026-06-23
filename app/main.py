from fastapi import FastAPI

app = FastAPI(
    title="Surtido Pro",
    description="Sistema de gestión para distribuidoras y emprendimientos mayoristas-minoristas.",
    version="0.1.0"
)


@app.get("/")
def root():
    """Endpoint raíz. Confirma que la API está corriendo."""
    return {"message": "Surtido Pro API"}


@app.get("/health")
def health_check():
    """Endpoint de salud. Usado para verificar el estado del servidor."""
    return {"status": "ok"}