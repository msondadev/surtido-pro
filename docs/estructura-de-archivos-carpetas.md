# Sistema Web: Surtido-Pro

## 📂 Estructura de archivos y carpetas
```
SURTIDO-PRO
├── app/                   
│    ├── __init__.py        # Indica que 'app' es un paquete de Python.
│    │
│    ├── core/
│    │    ├── __init__.py
│    │    ├── config.py
│    │    └── database.py
│    │
│    ├── models/            # Las clases
│    │    ├── __init__.py
│    │    ├── categoria.py
│    │    ├── detalle_pedido.py
│    │    ├── empleado.py                      
│    │    ├── empresa.py                    
│    │    ├── enums.py                     
│    │    ├── movimiento_stock.py                       
│    │    ├── pago_efectivo.py              
│    │    ├── pago_mercado_pago.py                                      
│    │    ├── pago_transferencia.py                   
│    │    │── pago.py             
│    │    │── participante.py                 
│    │    │── pedido.py              
│    │    │── persona_fisica.py  
│    │    │── producto.py 
│    │    │── relacion_comercial.py       
│    │    │── rol.py
│    │    └── usuario.py 
│    │
│    └── main.py
│        
│── docs
│   ├── cambios_UML.md 
│   ├── casos-de-uso.md 
│   ├── diagrama-de-clases.md 
│   ├── estructura-de-archivos-carpetas.md 
│   ├── historias-de-usuario.md                     
│   └── README.md 
│
│── .env                   # Variables de entorno
│── .env.example           # Si se sube a Git
│
├── env/                   # Entorno virtual
├── .gitignore             # Para no subir la carpeta /env a GitHub.
└── requirements.txt       # Lista de librerías (fastapi, sqlalchemy, etc.).

```


