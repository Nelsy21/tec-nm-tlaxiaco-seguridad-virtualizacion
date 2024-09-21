<?php
session_start();

// Datos de usuario para la autenticación (esto normalmente se extrae de una base de datos)
$usuarios_validos = [
    'admin' => 'admin',  // Usuario admin
    'usuarioEjemplo' => 'passwordEjemplo'  // Usuario normal
];

// Obtén los datos del formulario
$usuario = $_POST['usuario'];
$password = $_POST['password'];

// Verifica la autenticación
if (isset($usuarios_validos[$usuario]) && $usuarios_validos[$usuario] === $password) {
    $_SESSION['usuario'] = $usuario; // Guarda el nombre de usuario en la sesión
    
    if ($usuario === 'admin') {
        header('Location: principal.html'); // Redirige al admin a principal.html
    } else {
        header('Location: perfil.php'); // Redirige a la página de perfil para otros usuarios
    }
    exit();
} else {
    // Redirige al formulario de login con un mensaje de error (puedes ajustar esto)
    header('Location: login.php?error=1');
    exit();
}
?>
