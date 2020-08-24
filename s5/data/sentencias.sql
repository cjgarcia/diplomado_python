/* Insertar varios records */
INSERT INTO estudiantes(nombre, apellido) VALUES('Fraks', 'Gill'),
('Ramon', 'Alcantara'), ('Luffy', 'D.Mokey'), ('Mickey', 'Tilldelman');

/* Buscar los records */
SELECT * FROM estudiantes;

/*Nombre completo del estudiante*/
SELECT (e.nombre || ' ' || e.apellido) as nombre_completo 
FROM estudiantes as e; 

/* inner join*/

SELECT (e.nombre || ' ' || e.apellido) as nombre_completo, count(a.id) as num_asistencias
FROM estudiantes as e
JOIN asistencias as a ON a.estudiante_id = e.id
GROUP BY nombre_completo
ORDER BY num_asistencias DESC;
