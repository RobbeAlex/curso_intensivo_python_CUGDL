# 🐍 Curso Intensivo de Python: De Cero a Producción

Este repositorio contiene todo el material, ejercicios y proyectos desarrollados durante un curso intensivo de Python de 5 semanas. El programa está diseñado para abarcar desde la configuración inicial de un entorno de trabajo profesional hasta el despliegue de una aplicación funcional en producción.

---

## 🗂️ Estructura del Repositorio (Navegación por Ramas)

Para mantener el código organizado y facilitar el seguimiento progresivo del aprendizaje, **cada módulo del curso está alojado en una rama (`branch`) independiente**. 

Esta rama principal contiene la documentación general, pero para explorar el código fuente, los ejercicios y los proyectos de una semana en particular, es necesario cambiar a la rama correspondiente.

---

## 📚 Contenido de los Módulos

### 📍 [Semana 1] Setup & Basics: El Entorno Real
* Flujo Secuencial y Errores: El código se ejecuta estrictamente de arriba hacia abajo. Python ignora las líneas en blanco, pero es estrictamente sensible a la indentación (los espacios al inicio de la línea), los cuales usa para identificar bloques de código agrupados.
* Variables y Datos: Se revisaron los contenedores de información fundamentales: cadenas de texto (String declaradas entre comillas), enteros numéricos (Integer), números decimales (Float), y valores lógicos (Boolean que deben iniciar con mayúscula, ej. True o False).
* Lógica e Interacción: Se explicó el uso de estructuras condicionales (if, else) en conjunto con operadores de comparación (como mayor o menor que) para controlar las decisiones del programa. Además, se mostró el uso de funciones integradas como print() para mandar mensajes a la pantalla y input() para capturar respuestas tecleadas por el usuario.

### 📍 [Semana 2] Core Programming: Estructuras y Lógica
* Core Programming: Automatizando la Innovación
* Manipulación avanzada de estructuras de datos integradas (listas, tuplas, diccionarios y conjuntos).
* Manejo de excepciones y técnicas básicas de depuración de errores.

### 📍 [Semana 3] Pandas & APIs: El Poder de los Datos
* Introducción a la librería `pandas` para la exploración, limpieza y análisis de datos (DataFrames y Series).
* Lectura, procesamiento y exportación de archivos en múltiples formatos (CSV, Excel, JSON).
* Ejecución de peticiones HTTP para el consumo e integración de APIs REST.
* Transformación de datos crudos en información útil para análisis.

### 📍 [Semana 4] Construyendo el Frontend
* Diseño y estructuración de interfaces gráficas o aplicaciones web orientadas a datos.
* Conexión entre los procesos del backend (Python) y los componentes visuales del frontend.
* Manejo de eventos, captura de inputs del usuario y visualización de resultados en tiempo real.

### 📍 [Semana 5] Deployment y Presentación Final
* Preparación del código, empaquetado y gestión de variables de entorno para su despliegue.
* Configuración del proyecto en servicios de alojamiento en la nube (Cloud hosting).
* Pruebas de funcionamiento en producción y documentación técnica final del producto.

---

## ⚙️ Cómo explorar este repositorio

Si deseas revisar el código localmente en tu computadora, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/RobbeAlex/curso_intensivo_python_CUGDL.git
   cd curso_intensivo_python_CUGDL
   ```

2. Listar todas las ramas disponibles:
   ```bash
    git branch -a
   ```
   
3. Cambiar al módulo que deseas explorar:
   ```bash
    git checkout nombre-de-la-rama # Asegúrate de cambiar el nombre-de-la-rama por el nombre exacto asignado.
   ```

## 🛠️ Tecnologías y Herramientas Utilizadas
* Lenguaje Core: Python 3.x
* Análisis de Datos: Pandas
* Integración: APIs REST, Requests
* Control de Versiones: Git y GitHub
