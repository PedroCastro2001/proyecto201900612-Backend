class Comentario:
    def __init__(self, id_coment, usuario, id_cancion, descripcion):
        self.id_coment = id_coment
        self.usuario = usuario
        self.id_cancion = id_cancion
        self.descripcion = descripcion

    def getId_coment(self):
        return self.id_coment

    def getUsuario(self):  
        return self.usuario
    
    def getId_cancion(self):
        return self.id_cancion

    def getDescripcion(self):
        return self.descripcion

    def setId_coment(self, id_coment):
        self.id_coment = id_coment

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setId_cancion(self, id_cancion):
        self.id_cancion = id_cancion
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion   