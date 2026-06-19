Este documento representa la versión vigente del modelo.
Para consultar la evolución respecto del diseño inicial,
ver CAMBIOS_UML.md.

@startuml
skinparam classAttributeIconSize 0

'==================================================
' ENUMS
'==================================================

enum EstadoPedido {
    PENDIENTE
    CONFIRMADO
    CANCELADO
    ENTREGADO
}

enum TipoMovimientoStock {
    INGRESO
    EGRESO
    RESERVA
    LIBERACION
    AJUSTE
}

enum EstadoPago {
    PENDIENTE
    CONFIRMADO
    RECHAZADO
    ANULADO
}

'==================================================
' SEGURIDAD
'==================================================

class Usuario {
    -id : int
    -username : String
    -contrasenia : String
    -activo : Boolean
    -email_verificado : Boolean
    -creado_en : DateTime

    -roles : List<Rol>
    -pedidos : List<Pedido>

    +login()
    +cerrarSesion()
    +recuperarContrasenia()
    +cambiarContrasenia()
}

class Rol {
    -id : int
    -nombre : String
    -descripcion : String
}

Usuario "0..*" o-- "0..*" Rol

'==================================================
' PARTICIPANTES
'==================================================

abstract class Participante {
    -id : int
    -email : String
    -telefono : String
    -direccion : String

    -relacionesComerciales : List<RelacionComercial>

    +obtenerNombreCompleto() : String {abstract}
}

class PersonaFisica {
    -nombre : String
    -apellido : String
    -dni : String
    -fecha_nacimiento : Date

    +obtenerNombreCompleto() : String
}

class Empresa {
    -razon_social : String
    -cuit : String

    +obtenerNombreCompleto() : String
}

class Empleado {
    -legajo : String
    -fecha_ingreso : Date
}

Participante <|-- PersonaFisica
Participante <|-- Empresa

PersonaFisica <|-- Empleado

Participante "1" <-- "0..1" Usuario

'==================================================
' RELACIONES COMERCIALES
'==================================================

class RelacionComercial {
    -id : int
    -nombre : String
}

Participante "0..*" -- "0..*" RelacionComercial

'
' CLIENTE
' PROVEEDOR
'

'==================================================
' PRODUCTOS
'==================================================

class Categoria {
    -id : int
    -nombre : String

    -productos : List<Producto>
}

class Producto {
    -id : int
    -nombre : String
    -descripcion : String
    -precio_minorista : float
    -precio_mayorista : float
    -stock_actual : int
    -stock_reservado : int
    -foto_url : String
    -activo : boolean

    -categoria : Categoria
    -proveedores : List<Participante>

    +reservarStock()
    +liberarStock()
    +actualizarStock()
}

Categoria "1" -- "0..*" Producto

Participante "0..*" -- "0..*" Producto : proveedor

'==================================================
' PEDIDOS
'==================================================

class Pedido {
    -id : int
    -fecha : Date
    -estado : EstadoPedido
    -total : float

    -cliente : Participante
    -usuario : Usuario
    -detalles : List<DetallePedido>
    -repartidor: Empleado

    +agregarProducto(producto, cantidad)
    +calcularTotal()
    +confirmarPedido()
    +cancelarPedido()
    +cambiarEstado()
}

class DetallePedido {
    -id : int
    -cantidad : int
    -precio_unitario : float
    -tipo_precio : String

    -producto : Producto

    +calcularSubtotal()
}

Participante "1" --> "0..*" Pedido : cliente

Usuario "1" --> "0..*" Pedido : creado_por

Pedido "1" *-- "1..*" DetallePedido

DetallePedido "*" --> "1" Producto

Empleado "0..1" <-- "0..*" Pedido : repartidor

Pedido --> EstadoPedido

'==================================================
' PAGOS
'==================================================

abstract class Pago {
    -id : int
    -fecha : Date
    -monto : float
    -estado : EstadoPago

    +registrar()
    +confirmar() {abstract}
    +cancelar() {abstract}
}

class PagoEfectivo {
    -monto_recibido : float
    -vuelto : float

    +procesar(monto)
    +validar()
}

class PagoTransferencia {
    -cbu : String
    -alias : String
    -comprobante_url : String

    +procesar(monto)
    +validar()
}

class PagoMercadoPago {
    -preference_id : String
    -payment_id : String
    -external_reference : String

    +procesar(monto)
    +validar()
}

Pedido "1" -- "0..*" Pago

Pago <|-- PagoEfectivo
Pago <|-- PagoTransferencia
Pago <|-- PagoMercadoPago

Pago --> EstadoPago

'==================================================
' STOCK
'==================================================

class MovimientoStock {
    -id : int
    -fecha : Date
    -tipo : TipoMovimientoStock
    -cantidad : int
    -observacion : String

    -producto : Producto
    -usuario : Usuario
}

Producto "1" --> "0..*" MovimientoStock

Usuario "1" --> "0..*" MovimientoStock

MovimientoStock --> TipoMovimientoStock

@enduml


# Evolución del modelo
Principales cambios respecto del diseño inicial:
- Se eliminaron Cliente y Proveedor.
- Se incorporó RelacionComercial.
- Se eliminó Administrador, Vendedor y Repartidor.
- Se adoptó un esquema Usuario-Rol.
- Se incorporó la jerarquía Participante.
- Se abstractizó Pago.
- Se incorporó MovimientoStock.
- Se incorporó obtenerNombreCompleto() como método abstracto en Participante.

