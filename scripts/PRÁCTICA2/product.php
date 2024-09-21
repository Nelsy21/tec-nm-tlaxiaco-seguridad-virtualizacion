<!DOCTYPE html>
<html lang="en">
<head>
    <center>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario de Productos</title>
    <link rel="stylesheet" type="text/css" href="estilo.css">
</head>
<body>
    <h1>Formulario de Productos</h1>
    <form action="productos.php" method="post">
        <input type="hidden" name="action" id="action" value="insert">
        <label for="codigo">Código:</label>
        <input type="text" id="codigo" name="codigo" required><br>

        <label for="codigoExterno">Código Externo:</label>
        <input type="text" id="codigoExterno" name="codigoExterno" required><br>

        <label for="descripcion">Descripción:</label>
        <input type="text" id="descripcion" name="descripcion" required><br>

        <label for="venta">Venta:</label>
        <input type="text" id="venta" name="venta" required><br>

        <label for="precio">Precio:</label>
        <input type="number" id="precio" name="precio" step="0.01" required><br>

        <label for="iva">IVA (%):</label>
        <input type="number" id="iva" name="iva" step="0.01" required><br>

        <label for="stock">Stock:</label>
        <input type="number" id="stock" name="stock" required><br>

        <button type="submit" onclick="document.getElementById('action').value='insert';">Guardar</button>
        <button type="submit" onclick="document.getElementById('action').value='delete';">Eliminar</button>
        <button type="submit" onclick="document.getElementById('action').value='update';">Modificar</button>
    </form>
</center>
</body>
</html>
