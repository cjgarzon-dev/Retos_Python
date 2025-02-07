from abc import ABC, abstractmethod

# Variable global
clientes = []
pets = []

# Clases Principales
class Veterinary:
    class Person:
        id_counter = 1
        
        def __init__(self, name, contact):
            self.name = name
            self.contact = contact
            
            self.id_counter = Veterinary.Person.id_counter
            Veterinary.Person.id_counter += 1

    class Client(Person):
        def __init__(self, name, contact, address):
            super().__init__(name, contact)
            self.address = address
            self.pet = []
        
        def addPet(self, pet):
            self.pet.append(pet)

    class Pet:
        id_counter = 1
        def __init__(self, name, specie, race, age):
            self.name = name
            self.specie = specie
            self.race = race
            self.age = age
            self.historyClinic = []
            self.id_counter = Veterinary.Pet.id_counter
            Veterinary.Pet.id_counter += 1
            
        def addDate(self, date):
            self.historyClinic.append(date)
        
        def eraseDate(self, date):
            self.historyClinic.remove(date)
                
        def showHistory(self):
            if not self.historyClinic:
                print(f'No hay citas registradas para {self.name}')
            else:
                print(f'\nHistorial de las citas para {self.name}:')
                for appointment in self.historyClinic:
                    print(f'{appointment.id_counter}. Cita el {appointment.date} a las {appointment.hour}, servicio: {appointment.service} con el vetrinario: {appointment.veterinarian}')
                    

    class Date:
        id_counter = 1
        
        def __init__(self, date, hour, service, veterinarian):
            self.date = date
            self.hour = hour
            self.service = service
            self.veterinarian = veterinarian
            
            self.id_counter = Veterinary.Date.id_counter
            Veterinary.Date.id_counter += 1
            
# Funciones del sistemas
def registerClient():
    try:
        name = input('Ingrese el nombre del cliente: ').strip()
        contact = input('Ingrese contacto del cliente: ').strip()
        address = input('Ingrese la dirección del cliente: ').strip()
        
        cliente = Veterinary.Client(name, contact, address)
        clientes.append(cliente)
        print(f'Cliente registrado con ID: {cliente.id_counter}')
    except ValueError as e:
        print(f'Error: {e}')

def registerPet(): 
    print('Clientes disponibles:')
    
    if not clientes:
        print('\tNo existen clientes registrados')
        return
        
    for c in clientes:
        print(f'\tID: {c.id_counter}, Nombre: {c.name}')
    
    try:
        idClient = int(input('Ingrese el id del cliente que desea agregarle una mascota: ').strip())
        client = next((c for c in clientes if c.id_counter == idClient), None)
        if not client:
            raise ValueError(f'No existen clientes registrados con el ID {idClient}')
            
        namePet = input(f'Ingrese el nombre de la mascota de {client.name}: ').strip()
        specie = input('Ingrese la especie de la mascota: ').strip()
        race = input('Ingrese la raza de la mascota: ').strip()
        age = input('Ingrese la edad de la mascota: ').strip()
        
        pet = Veterinary.Pet(namePet, specie, race, age)
        pets.append(pet)
            
        client.addPet(pet)
        print(f'Mascota con ID: {pet.id_counter} agregada con éxito')   
    except ValueError as e:
        print(f'Error: {e}')

def scheduleDate():
    print('Clientes registrados:')
    
    if not clientes:
        print('\tNo existen clientes registrados')
        return
    if not pets:
        print('\tNo existen mascotas registradas')
        return
        
    for c in clientes:
        print(f'\tID: {c.id_counter}, Nombre: {c.name}')          
    
    try:
        client_id = int(input('Ingrese el ID del cliente: '))
        client = next((c for c in clientes if c.id_counter == client_id), None)
        if not client:
            raise ValueError(f'\tNo existe cliente registrado con el ID {client_id}')
        
        print(f'Mascotas del cliente {client.name}: ')
        for p in client.pet:
            print(f'\tID Mascota: {p.id_counter}, Nombre Mascota {p.name}')
            
        pet_id = int(input('Ingrese el ID de la mascota para agendar cita: ').strip())
        pet = next((p for p in client.pet if p.id_counter == pet_id), None)
        if not pet:
            raise ValueError(f'\tNo existe mascota registrada con el ID: {pet_id} para el cliente {client.name}')
        
        date = input('Ingrese la fecha de la cita (DD-MM-YY): ').strip()
        while not validateDate(date):
            print('Fecha inválida, por favor ingresa la fecha en el formato correcto (ejm. 31-01-25): ')
            date = input('Ingrese la fecha de la cita (DD-MM-YY): ').strip()
        hour = input('Ingrese la hora de la cita (12:00): ').strip()
        while not validateHour(hour):
            print('Hora inválida, por favor agregar la hora en el formato correcto (ejm. 12:00) : ')
            hour = input('Ingrese la hora de la cita (12:00): ').strip()
        service = input('Ingrese el servicio deseado: ').strip()
        veterinarian = input('Ingrese el nombre del veterinario: ').strip()
        
        appointment = Veterinary.Date(date, hour, service, veterinarian)
        pet.addDate(appointment)
        print('Cita agregada con éxito')
    except ValueError as e:
        print(f'Error: {e}')


def consultHistory():
    print('Clientes registrados:')
    
    if not clientes:
        print('\tNo existen clientes registrados')
        return
    if not pets:
        print('\tNo existen mascotas registradas')
        return
    
    for c in clientes:
        print(f'\tID Cliente: {c.id_counter}, Nombre cliente: {c.name}, Mascotas: ')
        if not c.pet:
            print('\t\tNo tiene mascotas registradas')
        for p in c.pet:
            print(f'\t\tID Mascota: {p.id_counter}, Nombre mascota: {p.name}')
    
    print('\nConsultar historial')
    try:
        client_id = int(input('Ingrese el ID del cliente: ').strip())
        client = next((c for c in clientes if c.id_counter == client_id), None)
        if not client:
            raise ValueError(f'\tNo existe cliente registrado con el ID {client_id}')
            
        if not client.pet:
            raise ValueError(f'\tEl cliente {client.name} no tiene mascotas registradas')
        
        print(f'Mascotas del cliente {client.name}: ')
        for p in client.pet:
            print(f'\tMascota: Nombre: {p.name}, ID: {p.id_counter}')
            
        pet_id = int(input('Ingrese el id de la mascota para consultar su historial: ').strip())
        pet = next((p for p in client.pet if p.id_counter == pet_id), None)
        if not pet:
            raise ValueError(f'\tNo existe mascota registrada con el ID: {pet_id} para el cliente {client.name}')
        
        pet.showHistory()
    except ValueError as e:
        print(f'Error: {e}')

def updateDate():
    if not clientes:
        print('No se tienen clientes registrados')
        return
    if not pets:
        print('No se tienen mascotas registradas')
        return
    
    print('Clientes y mascotas registrados')
    for c in clientes:
        print(f'Id cliente: {c.id_counter}, Nombre: {c.name}, Mascotas:')
        if not c.pet:
            print('\tNo tiene mascotas registradas')
        for p in c.pet:
            print(f'\tId mascota: {p.id_counter}, Nombre mascota: {p.name}')
    
    try:
        id_client = int(input('Ingrese el id del Cliente que desea consultar: '))
        client = next((c for c in clientes if c.id_counter == id_client), None)
        if not client:
            raise ValueError('No se encontró cliente registrado con ese ID')
        
        print(f'Mascotas del cliente {client.name}')
        for p in client.pet:
            print(f'\tId mascota: {p.id_counter}, Nombre mascota: {p.name}')
        id_Pet = int(input('Ingrese el id de la mascota que desea consultar: '))
        pet = next((p for p in client.pet if p.id_counter == id_Pet), None)
        if not pet:
            raise ValueError('No se encontro máscota con ese ID')
        
        if not pet.historyClinic:
            raise ValueError(f'\tLa máscota con id {pet.id_counter} no tiene historial registrado')
        
        print('Citas disponibles para actualizar')
        pet.showHistory()
        
        id_History = int(input('Ingrese el id de la cita actualizar: '))
        history = next((h for h in pet.historyClinic if h.id_counter == id_History), None)
        
        if not history:
            raise ValueError('\tNo se encontro historial clínico con ese ID')
        
        dateNew = pet.historyClinic[id_History-1]
        print(f'Cambiando los datos de la cita {id_History}')
    except ValueError as e:
        print(f'Error: {e}')
    
    newDate = input('Ingrese la nueva fecha de la cita (DD-MM-YY): ').strip()
    while not validateDate(newDate):
        print('Fecha inválida, por favor ingresa la fecha en el formato correcto (ejm. 31-01-25): ')
        newDate = input('Ingrese la nueva fecha de la cita (DD-MM-YY): ').strip()
    newHour = input('Ingrese la nueva hora de la cita (12:00): ').strip()
    while not validateHour(newHour):
        print('Hora inválida, por favor agregar la hora en el formato correcto (ejm. 12:00) : ')
        newHour = input('Ingrese la nueva hora de la cita (12:00): ').strip()
    newService = input('Ingrese el nuevo servicio deseado: ').strip()
    newVeterinarian = input('Ingrese el nombre del nuevo veterinario: ').strip()
    
    dateNew.date = newDate
    dateNew.hour = newHour
    dateNew.service = newService
    dateNew.veterinarian = newVeterinarian
    
    print('Cita actualizada con exito')

def eraseDate():
    if not clientes:
        print('No se tienen clientes registrados')
        return
    if not pets:
        print('No se tienen mascotas registradas')
        return
    
    print('Clientes y mascotas registrados')
    for c in clientes:
        print(f'Id cliente: {c.id_counter}, Nombre: {c.name}, Mascotas:')
        if not c.pet:
            print('\tNo tiene mascotas registradas')
        for p in c.pet:
            print(f'\tId mascota: {p.id_counter}, Nombre mascota: {p.name}')
    
    try:
        id_client = int(input('Ingrese el id del Cliente que desea consultar: '))
        client = next((c for c in clientes if c.id_counter == id_client), None)
        if not client:
            raise ValueError('No se encontró cliente registrado con ese ID')
        
        print(f'Mascotas del cliente {client.name}')
        for p in client.pet:
            print(f'\tId mascota: {p.id_counter}, Nombre mascota: {p.name}')
        id_Pet = int(input('Ingrese el id de la mascota que desea consultar: '))
        pet = next((p for p in client.pet if p.id_counter == id_Pet), None)
        if not pet:
            raise ValueError('No se encontro máscota con ese ID')
        
        if not pet.historyClinic:
            raise ValueError(f'\tLa máscota con id {pet.id_counter} no tiene historial registrado')
            
        print('Citas disponibles para cancelar')
        pet.showHistory()
        
        id_History = int(input('Ingrese el id de la cita a cancelar: '))
        history = next((h for h in pet.historyClinic if h.id_counter == id_History), None)
        
        if not history:
            raise ValueError('\tNo se encontro historial clínico con ese ID')
        
        dateErase = pet.historyClinic[id_History-1]
        print(f'Cancelando la cita con id {id_History}')
        pet.eraseDate(dateErase)
        print('Cita cancelada con éxito')
    except ValueError as e:
        print(f'Error: {e}')
    

# Funciones auxiliares
def validateDate(date):
    from datetime import datetime
    try:
        datetime.strptime(date,'%d-%m-%y')
        return True
    except ValueError:
        return False

def validateHour(hour):
    from datetime import datetime
    try:
        datetime.strptime(hour, '%H:%M')
        return True
    except ValueError:
        return False
        

# Menu principal
def main():
    while True:
        print('\n+++++ MENU PRINCIPAL +++++')
        print('1. Registrar Cliente')
        print('2. Registrar Mascota')
        print('3. Programar Cita')
        print('4. Actualizar Cita')
        print('5. Eliminar Cita')
        print('6. Consultar Historial')
        print('7. Salir')
        
        option = input('Seleccione una opcion: ')
        
        if option == '1':
            print('\n+++ REGISTRO DE CLIENTES +++')
            registerClient()
        elif option == '2':
            print('\n+++ REGISTRO DE MASCOTAS +++')
            registerPet()
        elif option == '3':
            print('\n+++ PROGRAMACIÓN DE CITAS +++')
            scheduleDate()
        elif option == '4':
            print('\n+++ ACTUALIZACIÓN DE CITAS +++')
            updateDate()
        elif option == '5':
            print('\n+++ ELIMINACIÓN DE CITAS +++')
            eraseDate()
        elif option == '6':
            print('\n+++ CONSULTA DE HISTORIAL +++')
            consultHistory()
        elif option == '7':
            print('\n+++ HASTA PRONTO +++')
            break
        else:
            print('Opción no valida')

main()
