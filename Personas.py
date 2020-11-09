class Persona:
    def __init__(self,nombre,apellido,usuario,password,tipo_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password
        self.tipo_usuario = tipo_usuario

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getUsuario(self):
        return self.usuario
    
    def getPassword(self):
        return self.password

    def getTipo_usuario(self):
        return self.tipo_usuario

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setUsuario(self, usuario):
        self.usuario = usuario

    def setPassword(self, password):
        self.password = password

    def setTipo_usuario(self, tipo_usuario):
        self.tipo_usuario = tipo_usuario