# Clases eliminadas
| UML anterior  | UML aprobado | Motivo                            |
| ------------- | ------------ | --------------------------------- |
| Cliente       | Eliminada    | Reemplazada por RelacionComercial |
| Proveedor     | Eliminada    | Reemplazada por RelacionComercial |
| Administrador | Eliminada    | Reemplazada por Rol               |
| Vendedor      | Eliminada    | Reemplazada por Rol               |
| Repartidor    | Eliminada    | Reemplazada por Rol               |


# Clases creadas
| Clase             | Motivo                                                    |
| ----------------- | --------------------------------------------------------- |
| RelacionComercial | Permitir múltiples relaciones sobre un mismo participante |
| Participante      | Unificar actores del dominio                              |
| PersonaFisica     | Especialización de Participante                           |
| Empresa           | Especialización de Participante                           |
| Empleado          | Especialización de PersonaFisica (Personal interno)       |


# Clases modificadas
## Usuario
- Antes: Usuario especializado por Administrador/Vendedor/Repartidor
- Ahora: Usuario asociado a múltiples Roles
- Motivo: Los roles representan permisos y no entidades del dominio.

## Participante
- Antes: Existían Cliente y Proveedor como entidades separadas.
- Ahora: 
    Participante centraliza personas y empresas. 
    Las relaciones comerciales determinan su rol.
- Motivo: Evitar duplicación y permitir que un mismo actor sea cliente y proveedor.
- gregado: Se incorpora `obtenerNombreCompleto()` como método abstracto para garantizar 
  que PersonaFisica y Empresa definan su propia representación de nombre.

## MovimientoStock
- Antes: El stock era tratado únicamente como un valor del producto.
- Ahora: 
    Se registran eventos de stock mediante MovimientoStock. 
    Producto conserva stock_actual y stock_reservado.
- Motivo: Permitir trazabilidad y auditoría sin recalcular el inventario completo.

## Pago
- Antes: Un único tipo de pago.
- Ahora: Jerarquía abstracta con distintos medios de pago.
    - Subclases:
        PagoEfectivo
        PagoTransferencia
        PagoMercadoPago

## Pedido
- Cambios:
    Se aclara que Usuario representa "creado_por".
    Cliente pasa a ser Participante.

