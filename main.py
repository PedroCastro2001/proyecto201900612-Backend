# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from Personas import Persona
from Canciones import Cancion 
from Comentarios import Comentario
from Solicitudes import Solicitud
from Favoritos import Favorito

app = Flask(__name__)
CORS(app)
Usuarios = []
Canciones = []
Comentarios = []
Solicitudes = []
Favoritos = []
cont_canciones = 0
cont_comentarios = 0
cont_solicitudes = 0
cont_Favoritos = 0

Usuarios.append(Persona('Usuario','Maestro','admin','admin','1'))
Usuarios.append(Persona('Pedro','Castro',"PC2001","1111",'2'))
Usuarios.append(Persona('Benjamin','Garcia',"benja_621","2222",'2'))
Usuarios.append(Persona('Antonio','Calderon',"antron_01","3333",'2'))

Comentarios.append(Comentario('0','Pedro','9','Me encanta esta canción'))
Comentarios.append(Comentario('1','Antonio','9','Esta es una de mis canciones favoritas, me encanta!!!!!'))

Solicitudes.append(Solicitud('0','How Deep Is Your Love','Calvin Harris ft. Disciples','Now That Is What I Call Music (2016)','2015','https://img.discogs.com/3_50UUoEl1DSaIDz275XL4M99SE=/fit-in/300x300/filters:strip_icc():format(jpeg):mode_rgb():quality(40)/discogs-images/R-7377290-1440175578-3968.jpeg.jpg','https://open.spotify.com/embed/track/22mek4IiqubGD9ctzxc69s','https://www.youtube.com/embed/EgqUJOudrcM?autoplay=0&fs=0&iv_load_policy=3&showinfo=0&rel=0&cc_load_policy=0&start=0&end=0&origin=https://youtubeembedcode.com'))
Solicitudes.append(Solicitud('1','Summertime Sadness','Lana Del Rey','Born To Die','2012','https://upload.wikimedia.org/wikipedia/en/thumb/2/22/SummertimeSadnessOfficial.png/220px-SummertimeSadnessOfficial.png','https://open.spotify.com/embed/track/3BJe4B8zGnqEdQPMvfVjuS','https://youtu.be/TdrL3QxjyVw'))

@app.route('/',methods=['GET'])
def rutaInicial():
    print("Hola perras")
    return("Hola perras")

@app.route('/Personas', methods=['GET'])
#Queremos que nos devuelva los datos de las personas
def obtenerPersonas():
    #Usamos la variable global para usar una variable declarada en el ambito global
    global Usuarios
    Datos = []
    #Los for se pueden trabajar como un for each, es decir un objeto dentro de los objetos
    for usuario in Usuarios:
        #Formando el JSON, segun la estructura del JSON lo formamos como un objeto 
        #Que tenga almacenado su nombre y su valor.
        Dato = {
            'nombre': usuario.getNombre(),
            'apellido': usuario.getApellido(),
            'contraseña': usuario.getPassword(),
            'usuario': usuario.getUsuario(),
            'tipo_usuario': usuario.getTipo_usuario()
            }
        Datos.append(Dato)
    #Usamos jsonify para convertir nuestro arreglo en un objeto JSON 
    #Y obtener así la respuesta no como arreglo sino como objeto JSON
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/Personas/<string:usuario>', methods=['GET'])
def ObtenerPersona(usuario):
    global Usuarios
    DatoUsuario = []
    for username in Usuarios:
        if username.getUsuario() == usuario:
            Salida = {
                'nombre': username.getNombre(),
                'apellido': username.getApellido(),
                'usuario': username.getUsuario(),
                'password': username.getPassword(),
                'tipo_usuario': username.getTipo_usuario()
                }
            DatoUsuario.append(Salida)   
    respuesta = jsonify(DatoUsuario)
    return(respuesta)

@app.route('/Personas/<string:usuario>', methods=['PUT'])
def ActualizarPersona(usuario):
    global Usuarios
    for i in range(len(Usuarios)):
        if usuario == Usuarios[i].getUsuario():
            Usuarios[i].setNombre(request.json['nombre'])
            Usuarios[i].setApellido(request.json['apellido'])
            Usuarios[i].setUsuario(request.json['usuario'])
            Usuarios[i].setPassword(request.json['password'])
            Usuarios[i].setTipo_usuario(request.json['tipo_usuario'])
            break
    return jsonify({'message': 'El usuario ha sido actualizado exitosamente'})

@app.route('/Personas', methods=['POST'])
def AgregarUsuario():
    global Usuarios
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    username = request.json['usuario']
    password = request.json['password']
    tipo_usuario = request.json['tipo_usuario']
    encontrado = False
    for usuario in Usuarios:
        if usuario.getUsuario() == username:
            encontrado = True
            break
        if encontrado:
            return jsonify({
                'message':'Failed',
                'reason':'El usuario ya está registrado'
                })
        else:
            nuevo = Persona(nombre,apellido,username,password,tipo_usuario)
            Usuarios.append(nuevo)
            return jsonify({
                'message':'Success',
                'reason':'Se agrego el usuario'

            })

@app.route('/Personas/<string:usuario>', methods=['DELETE'])
def DeleteUser(usuario):
    global Usuarios
    for j in range(len(Usuarios)):
        if usuario == Usuarios[j].getUsuario():
           del Usuarios[j]
           break
    return jsonify({'message':'El usuario ha sido eliminado exitosamente'}) 

@app.route('/Login', methods=['POST'])
def Login():
    global Usuarios
    username = request.json['usuario']
    password = request.json['password']
    for usuario in Usuarios:
        if usuario.getUsuario() == username and usuario.getPassword() == password:
            Dato = {
                'message': 'Success',
                'usuario': usuario.getUsuario()
                }
            break
        else:
            Dato = {
                'message': 'Failed',
                'usuario': ''
            }
    respuesta = jsonify(Dato)
    return(respuesta)

@app.route('/Cancion', methods=['POST'])
def guardarCancion():
        global Canciones, cont_canciones
        id = cont_canciones
        cancion = request.json['cancion']
        artista = request.json['artista']
        album = request.json['album']
        fecha = request.json['fecha']
        imagen = request.json['imagen']
        spotify = request.json['spotify']
        youtube = request.json['youtube']
        nuevo = Cancion(id, cancion, artista, album, fecha, imagen, spotify, youtube)
        Canciones.append(nuevo)
        cont_canciones += 1
        return jsonify({
                'message':'Sucess',
                'reason':'Se agrego la canción'
                })

@app.route('/Cancion', methods=['GET'])
def obtenerCanciones():
    global Canciones, cont_canciones
    Datos = []
    for cancion in Canciones:
        Dato = {
            'id': cancion.getId(),
            'cancion': cancion.getCancion(),
            'artista': cancion.getArtista(),
            'album': cancion.getAlbum(),
            'fecha': cancion.getFecha(),
            'imagen': cancion.getImagen(),
            'spotify': cancion.getSpotify(),
            'youtbe': cancion.getYoutube()
            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/Cancion/<int:id>', methods=['GET'])
def ObtenerCancion(id):
    global Canciones
    DatoCancion = []

    for identificador in Canciones:
        if identificador.getId() == id:
            Salida = {
                'id': identificador.getId(),
                'cancion': identificador.getCancion(),
                'artista': identificador.getArtista(),
                'album': identificador.getAlbum(),
                'fecha': identificador.getFecha(),
                'imagen': identificador.getImagen(),
                'spotify': identificador.getSpotify(),
                'youtube': identificador.getYoutube()
                }
            DatoCancion.append(Salida)
    respuesta = jsonify(DatoCancion)
    return(respuesta)      

@app.route('/Cancion/<int:id>', methods=['PUT'])
def UpdateSong(id):
    global Canciones
    for i in range(len(Canciones)):
        if id == Canciones[i].getId():
            Canciones[i].setCancion(request.json['cancion'])
            Canciones[i].setArtista(request.json['artista'])
            Canciones[i].setAlbum(request.json['album'])
            Canciones[i].setFecha(request.json['fecha'])
            Canciones[i].setImagen(request.json['imagen'])
            Canciones[i].setSpotify(request.json['spotify'])
            Canciones[i].setYoutube(request.json['youtube'])
            break
    return jsonify({'message': 'Se actualizó el dato exitosamente'})

@app.route('/Cancion/<int:id>', methods=['DELETE'])
def DeleteSong(id):
    global Canciones
    for j in range(len(Canciones)):
        if id == Canciones[j].getId():
            del Canciones[j]
            break
    return jsonify({'message':'La canción ha sido eliminada exitosamente!'})

@app.route('/Comentarios', methods=['GET'])
def GetComments():
    global Comentarios, cont_comentarios
    Array = []
    for comment in Comentarios:
        Coment = {
            'id_coment': comment.getId_coment(),
            'usuario': comment.getUsuario(),
            'id_cancion': comment.getId_cancion(),
            'descripcion': comment.getDescripcion()
            }
        Array.append(Coment)
    respuesta = jsonify(Array)
    return(respuesta)

@app.route('/Comentarios/<string:id_cancion>', methods=['GET'])
def ObtainComment(id_cancion):
    global Comentarios
    Array = []

    for codigo in Comentarios:
        if codigo.getId_cancion() == id_cancion:
            Salida = {
                'id_coment': codigo.getId_coment(),
                'usuario': codigo.getUsuario(),
                'id_cancion': codigo.getId_cancion(),
                'descripcion': codigo.getDescripcion()
                }
            Array.append(Salida)
    respuesta = jsonify(Array)
    return(respuesta) 

@app.route('/Comentarios/<string:id_coment>', methods=['PUT'])
def UpdateComment(id_coment):
    global Comentarios
    for i in range(len(Comentarios)):
        if id_coment == Comentarios[i].getId_coment():
            Comentarios[i].setUsuario(request.json['usuario'])
            Comentarios[i].setId_cancion(request.json['id_cancion'])
            Comentarios[i].setDescripcion(request.json['descripcion'])
            break
    return jsonify({'message': 'Se actualizó el comentario exitosamente'})

@app.route('/Comentarios', methods=['POST'])
def SaveComment():
        global Comentarios, cont_comentarios
        id_coment = cont_comentarios
        usuario = request.json['usuario']
        id_cancion = request.json['id_cancion']
        descripcion = request.json['descripcion']
        nuevo = Comentario(id_coment, usuario, id_cancion, descripcion)
        Comentarios.append(nuevo)
        cont_comentarios += 1
        return jsonify({
                'message':'Sucess',
                'reason':'El comentario ha sido agregado'
            })

@app.route('/Solicitudes', methods=['POST'])
def guardarSolicitud():
        global Solicitudes, cont_solicitudes
        id = cont_solicitudes
        cancion = request.json['cancion']
        artista = request.json['artista']
        album = request.json['album']
        fecha = request.json['fecha']
        imagen = request.json['imagen']
        spotify = request.json['spotify']
        youtube = request.json['youtube']
        nuevo = Solicitud(id, cancion, artista, album, fecha, imagen, spotify, youtube)
        Solicitudes.append(nuevo)
        cont_solicitudes += 1
        return jsonify({
                'message':'Sucess',
                'reason':'La solicitud ha sido enviada'
                })

@app.route('/Solicitudes', methods=['GET'])
def obtenerSolicitudes():
    global Solicitudes, cont_solicitudes
    Requests = []
    for solicitud in Solicitudes:
        Request = {
            'id': solicitud.getId(),
            'cancion': solicitud.getCancion(),
            'artista': solicitud.getArtista(),
            'album': solicitud.getAlbum(),
            'fecha': solicitud.getFecha(),
            'imagen': solicitud.getImagen(),
            'spotify': solicitud.getSpotify(),
            'youtbe': solicitud.getYoutube()
            }
        Requests.append(Request)
    respuesta = jsonify(Requests)
    return(respuesta)

@app.route('/Solicitudes/<string:id>', methods=['GET'])
def ObtenerSolicitd(id):
    global Solicitudes
    Requests = []

    for identificador in Solicitudes:
        if identificador.getId() == id:
            Salida = {
                'id': identificador.getId(),
                'cancion': identificador.getCancion(),
                'artista': identificador.getArtista(),
                'album': identificador.getAlbum(),
                'fecha': identificador.getFecha(),
                'imagen': identificador.getImagen(),
                'spotify': identificador.getSpotify(),
                'youtube': identificador.getYoutube()
                }
            Requests.append(Salida)
    respuesta = jsonify(Requests)
    return(respuesta)  

@app.route('/Solicitudes/<string:id>', methods=['PUT'])
def UpdateRequest(id):
    global Solicitudes
    for i in range(len(Solicitudes)):
        if id == Solicitudes[i].getId():
            Solicitudes[i].setCancion(request.json['cancion'])
            Solicitudes[i].setArtista(request.json['artista'])
            Solicitudes[i].setAlbum(request.json['album'])
            Solicitudes[i].setFecha(request.json['fecha'])
            Solicitudes[i].setImagen(request.json['imagen'])
            Solicitudes[i].setSpotify(request.json['spotify'])
            Solicitudes[i].setYoutube(request.json['youtube'])
            break
    return jsonify({'message': 'Se actualizó la solicitud'})

@app.route('/Solicitudes/<string:id>', methods=['DELETE'])
def DeleteRequest(id):
    global Solicitudes
    for j in range(len(Solicitudes)):
        if id == Solicitudes[j].getId():
            del Solicitudes[j]
            break
    return jsonify({'message':'La solicitud ha sido eliminada exitosamente!'})

@app.route('/Favorito', methods=['POST'])
def guardarFavorito():
        global Favoritos, cont_Favoritos
        id = cont_Favoritos
        cancion = request.json['cancion']
        artista = request.json['artista']
        album = request.json['album']
        fecha = request.json['fecha']
        imagen = request.json['imagen']
        spotify = request.json['spotify']
        youtube = request.json['youtube']
        nuevo = Favorito(id, cancion, artista, album, fecha, imagen, spotify, youtube)
        Favoritos.append(nuevo)
        cont_Favoritos += 1
        return jsonify({
                'message':'Sucess',
                'reason':'La canción se agregó a la lista de favoritos'
                })

@app.route('/Favorito', methods=['GET'])
def obtenerFavoritos():
    global Favoritos, cont_Favoritos
    Entrada = []
    for favorito in Favoritos:
        Dato = {
            'id': favorito.getId(),
            'cancion': favorito.getCancion(),
            'artista': favorito.getArtista(),
            'album': favorito.getAlbum(),
            'fecha': favorito.getFecha(),
            'imagen': favorito.getImagen(),
            'spotify': favorito.getSpotify(),
            'youtbe': favorito.getYoutube()
            }
        Entrada.append(Dato)
    respuesta = jsonify(Entrada)
    return(respuesta)


@app.route('/Favorito/<int:id>', methods=['GET'])
def obtenerFavorito(id):
    global Favoritos
    DatoFavorito = []

    for identificador in Favoritos:
        if identificador.getId() == id:
            Salida = {
                'id': identificador.getId(),
                'cancion': identificador.getCancion(),
                'artista': identificador.getArtista(),
                'album': identificador.getAlbum(),
                'fecha': identificador.getFecha(),
                'imagen': identificador.getImagen(),
                'spotify': identificador.getSpotify(),
                'youtube': identificador.getYoutube()
                }
            DatoFavorito.append(Salida)
    respuesta = jsonify(DatoFavorito)
    return(respuesta) 



if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0", port=5000, debug=True)
