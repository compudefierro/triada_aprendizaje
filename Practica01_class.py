# class persona:
# Caracteristicas: 
# Cada instancia persona contiene las variables:
# nombre, edad, fecha_nac, dni
# Metodos (funciones): 
# consultar, modificar.
class persona:
  def __init__(self, nombre, edad, fecha_nac, dni):
    self.nombre = nombre
    self.edad = edad
    self.fecha_nac = fecha_nac
    self.dni = dni

  def consultar(self):
    return self.nombre, self.edad, self.fecha_nac, self.dni

  def modificar(self,tipo_dato, dato):
    if tipo_dato == 1:
      self.nombre = dato
      return f'El nombre: {self.nombre} guardado correctamente.'
    if tipo_dato == 2:
      self.edad = dato
      return f'La edad {self.edad} guardado correctamente.'
    if tipo_dato == 3:
      self.fecha_nac = dato
      return f'La Fecha Nac. {self.fecha_nac} guardado correctamente.'
    if tipo_dato == 4:
      self.dni = dato
      return f'El DNI {self.dni} guardado correctamente.'
