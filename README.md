Autor: Manuel Muñoz
Descripción:
    El concepto básico es el de un blog donde el autor comparte diferentes anecdotas de viajes a lo largo de Perú, donde existen también, suscriptores que al suscribirse recibirán correos con actualizaciónes y, a futuro, comentar las mismas.
    
Admin:
    mamz1303
    Bobbypeque13

Modelos:
    -Suscriptor
    -Post
    -Tag

Explicación de modelos:
    Suscriptor: Tiene el concepto de un usuario registrado y actualmente solo puede registrarse.
    Post: Publicación de un lugar, puede registrarse.
    Tag: Palabras clave de un determinado Post

    Notas: 
        -La idea de crear los modelos de Post y Tag, es que tengan un modelo relacional de muchos a muchos

Procedimiento de testeo de datos:
    La creación y busqueda de los modelos, se encuentran en el navegador con los siguientes nombres:
        -Suscriptor: BuscarSuscriptor y NewSuscriptor
        -Post: BuscarPost y NewPost
        -Tag: BuscarTag y NewTag
    Desde BuscarPost se puede buscar mediante ID, sugerencia Id's: 5, 6, 7, 8 (ya creado)
    Desde BuscarTag se puede buscar mediante ID, sugerencia Id, 1,2,3,4,5,6,7 (ya creado)
        La idea de Post y Tag es que al buscar un Post, salga una lista de sus 'Tags'
    Desde BuscarSuscriptor se puede buscar mediante Email, sugerencia test@test.com (2 ya creados)

