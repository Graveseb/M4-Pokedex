# M4-Pokedex
El sigueinte codigo lo escribo con los siguientes puntos en mente
Consumo exitoso de la PokeAPI: El código utiliza la biblioteca requests para realizar una llamada a la PokeAPI
y obtener datos sobre un Pokémon en base a su nombre. La función get_pokemon_data maneja esta tarea y parece funcionar correctamente.

Validación de status codes correcta: La función get_pokemon_data verifica si el código de estado de la respuesta es 
404 para manejar la situación en la que el Pokémon no se encuentra en la PokeAPI.

Despliegue correcto de la información: El código procesa los datos del Pokémon obtenidos de la PokeAPI y los muestra
de manera organizada en la consola. Muestra el nombre, peso, tamaño, movimientos, habilidades y tipos del Pokémon.

Guardar adecuadamente el archivo .json: El código incluye la función save_to_json que guarda la información del Pokémon 
en un archivo JSON. Los datos se almacenan en un archivo con el nombre del Pokémon en una carpeta llamada "pokedex".

Mostrar imagen: El código descarga la imagen del Pokémon desde la URL proporcionada por la PokeAPI y la muestra en una
ventana separada utilizando la biblioteca PIL. La imagen también se guarda en formato JPEG en la carpeta "pokedex".

Manejo de errores: El código incluye un manejo de errores para detectar problemas al mostrar la imagen y los captura en caso de que ocurran.

Hablando de mi experiencia al desarollar ese codigo puedo decir que me costo trabajo especialmente porque en el ejemplo que se dio, el codigo funcionaba con jupyter 
lo cual no estaba acostumbrado de utilizar ni pude entender bien como aplicar por lo que termine usando las bases que ya conozco
me asegure de cumplir con todos los puntos dados en la rubrica pero la funcionalidad para mostrar la imagen podría variar 
según el sistema operativo en el que se esté ejecutando el código. El código utiliza el comando os.system("start {img_path}") para abrir la imagen 
en la aplicación predeterminada del sistema, lo cual puede no funcionar en todos los sistemas operativos.
Además, de que se necesitan tener instaladas las bibliotecas requests, PIL (Pillow) y json para que el código funcione correctamente.
En general, el código parece cumplir con todos los méritos establecidos en la rúbrica por lo que me siento bien al saber que logre desarollar 
el pokedex
