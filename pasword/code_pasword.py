import json as js

class pasword :
    def __init__(self,texto):
        self.pwd = texto #Lista de paswords
        self.response = [{'pwd':'','issues': []}]*len(texto)
        for i in range (len(texto)) :
            self.response[i]['pwd'] = texto[i]

    #Crear metodos para verificar cada uno de los requisitos
    def validate_pwd_size (self):
        for i in range (len(self.pwd)) :
            #cada i es una pasword
            if len(self.pwd[i]) < 8 or len(self.pwd[i]) > 16 :
                self.response[i]['issues'].append('Pasword should have at least 8 characters and no more than 16.')
                break


    def validate_upper_case (self):
        for i in range (len(self.pwd)) :
            if sum(1 for c in self.pwd[i] if c.isupper()) < 1:
                self.response[i]['issues'].append('Pasword should have at least one upper case')
                break


    def have_4diff_char (self):
        for i in range (len(self.pwd)) :
            if set(self.pwd[i]) < 4 :
                self.response[i]['issues'].append('Pasword should have at least 4 differents characters')
                break
        

    def have_adyacent_char (self):
        for i in range (len(self.pwd)) :
            for j in len(1,self.pwd[i]) :
                if self.pwd[i][j] == self.pwd[i][j-1] :
                    self.response[i]['issues'].append('Pasword cannot have consecutive equal characters')
                    break        


def crear_datos ():  
    dicc = { "users" : [{"name": "nandaUnical","pwd": "12345"}, {"name": "brunoUnical","pwd" : "qwert"}, {"name":"amandaUnical","pwd":"1q2w3e"}] }
    with open("data.json", "w") as f:
        js.dump(dicc, f)


def obtener_datos ():
    with open('data.json', 'r') as f:
        user_dicc = js.load(f)
    #Obteniendo cada pasword
    pwd = []#Paswords de todos los usuarios
    for i in user_dicc:
        #print (user_dicc[i])#lista de diccionarios
        for j in user_dicc[i]:
            #print (j)#cada diccionario en la lista
            pwd.append(j['pwd'])
    return pwd
        
 
crear_datos()
texto = obtener_datos()

a = pasword(texto)

