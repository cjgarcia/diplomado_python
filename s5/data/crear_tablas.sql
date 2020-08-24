DROP TABLE IF EXISTS estudiantes;
DROP TABLE IF EXISTS asistencias;

CREATE TABLE estudiantes(
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL
);

CREATE TABLE asistencias(
    id INTEGER PRIMARY KEY,
    estudiante_id INTEGER NOT NULL,
    fecha DATETIME DEFAULT (datetime('now', 'localtime')),
    estado BOOLEAN DEFAULT 1,

    FOREIGN KEY(estudiante_id) REFERENCES estudiantes(id) 
);