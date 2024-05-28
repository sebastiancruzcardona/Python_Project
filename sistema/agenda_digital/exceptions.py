class Nombre_No_Debe_Contener_numeros(Exception):
   def __init__(self, message='El nombre no debe contener números.'):
      super().__init__(message)   
   pass

class Apellido_No_Debe_Contener_numeros(Exception):
   def __init__(self, message='El apellido no debe contener números.'):
      super().__init__(message)   
   pass

class Email_No_Valido(Exception):
   def __init__(self, message='Debe ingresar un email valido.'):
      super().__init__(message)   
   pass

class Telefono_No_Valido(Exception):
   def __init__(self, message='Debe ingresar un teléfono valido.'):
      super().__init__(message)   
   pass