## API predicion de popularidad de canciones

* Para usarla deben ingresar al URL: http://18.218.7.251:5000/

  El api pide dos argumentos numéricos

    - duration_ms = Duración de la canción en milisegundos 
    - explicit = Indica si la canción es explícita (0 = No, 1 = Sí)

Ejemplo: http://18.218.7.251:5000/predict/?duration_ms=200000&explicit=1

Ejemplo: http://18.218.7.251:5000/predict/?duration_ms=468000&explicit=0

En github coloque todo los archivo

  https://github.com/erramirezc1/MLyPLN_Proyecto_API

Esta el notebook y los archivos que cargue a el EC2 de AWS

Solo use duration_ms y explicit para entrenar un modelo de regresión
