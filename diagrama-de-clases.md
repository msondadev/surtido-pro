@startuml
skinparam classAttributeIconSize 0

class Usuario {
    -id : int
    -nombre : String
    -email : String
    -password : String
    -rol : List<Rol>
    --
    +login()
    +cambiarContrasenia()
    +crearPedido()
    +verPedidos()
    +gestionarProductos()
}

class Rol {
    -nombre : str
    --
    +crearRol()
    +editarRol()
}

class Cliente {
    -id : int
    -nombre : String
    -telefono : String
    -direccion : String
    --
    +verPedidos()
    +realizarPedido()
}

class Categoria {
    -id : int
    -nombre : String
    --
    +crearCategoria()
    +editarCategoria()
}

class Producto {
    -id : int
    -nombre : String
    -precioMinorista : float
    -precioMayorista : float
    -stockActual : int
    -stockReservado : int
    --
    +actualizarStock()
    +reservarStock(cantidad)
    +liberarStock(cantidad)
}

class Pedido {
    -id : int
    -fecha : Date
    -estado : String
    -total : float
    --
    +calcularTotal()
    +confirmarPedido()
    +cancelarPedido()
    +cambiarEstado()
}

class DetallePedido {
    -cantidad : int
    -precioUnitario : float
    -subtotal : float
    --
    +calcularSubtotal()
}

abstract class MetodoPago {
    +procesar(monto: float)
}

class PagoEfectivo {
    +procesar(monto: float)
}

class PagoTransferencia {
    +procesar(monto: float)
}

' ===== RELACIONES =====

' Composición = rombo RELLENO (*--)
Usuario "1" *-- "*" Rol : contiene >

' Asociación = línea simple
Usuario "1" -- "*" Pedido : crea >
Cliente "1" -- "*" Pedido : realiza >

' Composición = rombo RELLENO (*--)
Pedido "1" *-- "*" DetallePedido : compone >

' Asociación
Producto "1" -- "*" DetallePedido

' Agregación = rombo VACÍO (o--)
Categoria "1" o-- "*" Producto : agrupa >

' Herencia
MetodoPago <|-- PagoEfectivo
MetodoPago <|-- PagoTransferencia

@enduml