
CREATE DATABASE TeleRed;

USE TeleRed;

-- Tabla de Clientes
CREATE TABLE Clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

-- Tabla de Planes
CREATE TABLE Planes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    velocidad INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);

-- Tabla de Contratos
CREATE TABLE Contratos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    plan_id INT NOT NULL,
    fecha_inicio DATE NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
    FOREIGN KEY (plan_id) REFERENCES Planes(id)
);

-- Tabla de Equipos
CREATE TABLE Equipos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_serie VARCHAR(50) NOT NULL UNIQUE,
    modelo VARCHAR(50) NOT NULL,
    contrato_id INT NOT NULL,
    FOREIGN KEY (contrato_id) REFERENCES Contratos(id)
);