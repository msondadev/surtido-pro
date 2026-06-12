## 1: Caso de Uso: Iniciar Sesión
- Actor: Usuario (Administrador / Vendedor)
- Descripción: Permite al usuario autenticarse en el sistema mediante email y contraseña.
- Flujo principal
   - El usuario ingresa su email
   - El usuario ingresa su contraseña
   - El sistema valida las credenciales
   - El sistema permite el acceso al sistema
- Flujos alternativos
   - 3a. Credenciales incorrectas → el sistema muestra un error
   - 3b. Usuario inexistente → el sistema informa que no está registrado
- Precondición
   - El usuario debe estar registrado
- Postcondición
   - El usuario accede al sistema según su rol

## 2: Caso de Uso: Gestionar Productos
- Actor: Administrador
- Descripción: Permite administrar el catálogo de productos del sistema.
- Flujo principal
   - El administrador accede a la sección de productos
   - Elige crear, editar o eliminar un producto
   - Ingresa o modifica los datos del producto
   - El sistema guarda los cambios
- Flujos alternativos
   - 3a. Datos incompletos → el sistema solicita corrección
   - 4a. Error al guardar → el sistema notifica
- Precondición
El administrador debe estar logueado
- Postcondición
El catálogo queda actualizado

## 3: Caso de Uso: Crear Pedido
- Actor: Administrador / Vendedor
- Descripción: Permite generar un pedido para un cliente validando stock y calculando el total.
- Flujo principal
   - El usuario selecciona un cliente
   - Agrega productos al pedido
   - El sistema valida el stock disponible
   - El sistema calcula el total
   - El usuario confirma el pedido
   - El sistema registra el pedido
   - El sistema reserva el stock
- Flujos alternativos
   - 3a. Stock insuficiente → el sistema muestra error
   - 5a. El usuario cancela → no se guarda el pedido
- Precondición
   - El usuario debe estar logueado
   - Deben existir productos y clientes registrados
- Postcondición
   - El pedido queda registrado
   - El stock queda reservado


## 4: Caso de Uso: Gestionar Estado del Pedido
- Actor: Administrador
- Descripción: Permite actualizar el estado de un pedido para reflejar su progreso.
- Flujo principal
   - El administrador selecciona un pedido
   - Elige un nuevo estado
   - El sistema actualiza el estado
- Flujos alternativos
   - 2a. Estado inválido → el sistema muestra error
- Precondición
   - El pedido debe existir
   - El administrador debe estar logueado
- Postcondición
   - El estado del pedido queda actualizado
   - Si el pedido se cancela → se libera stock
   - Si se entrega → se descuenta stock

## 5: Caso de Uso: Consultar Catálogo y Realizar Pedido
Actor: Cliente
Descripción: Permite al cliente visualizar productos y enviar un pedido.
- Flujo principal
   - El cliente accede al catálogo
   - Visualiza productos
   - Filtra por categoría o precio
   - Agrega productos al carrito
   - Selecciona método de entrega
   - Envía el pedido por WhatsApp
- Flujos alternativos
   - 4a. No hay stock → el sistema informa
   - 6a. Error al enviar → se notifica al cliente
- Precondición
- El catálogo debe estar disponible
- Postcondición
   - El pedido es enviado al administrador
