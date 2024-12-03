class NodoCita:
    def __init__(self, cedula, info_cita):
        self.cedula = cedula
        self.info_cita = info_cita
        self.siguiente = None

class ListaEnlazadaCitas:
    def __init__(self):
        self.cabeza = None

    def agregar_cita(self, cedula, info_cita):
        nuevo_nodo = NodoCita(cedula, info_cita)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        print(f"Cita agendada para la cédula {cedula}.")

    def atender_cita(self):
        if not self.cabeza:
            print("No hay citas en la lista.")
            return None
        cita_atendida = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return cita_atendida

class NodoPaciente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

class ColaUrgencias:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def registrar_paciente(self, nombre):
        nuevo_paciente = NodoPaciente(nombre)
        if not self.primero:
            self.primero = nuevo_paciente
            self.ultimo = nuevo_paciente
        else:
            self.ultimo.siguiente = nuevo_paciente
            self.ultimo = nuevo_paciente
        print(f"Paciente {nombre} registrado en urgencias.")

    def atender_paciente(self):
        if not self.primero:
            print("No hay pacientes en la cola de urgencias.")
            return None
        paciente_atendido = self.primero
        self.primero = self.primero.siguiente
        if not self.primero:
            self.ultimo = None
        return paciente_atendido.nombre

class NodoHistorial:
    def __init__(self, paciente, diagnostico):
        self.paciente = paciente
        self.diagnostico = diagnostico
        self.siguiente = None
        self.anterior = None

class ListaDobleHistorial:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def registrar_atencion(self, paciente, diagnostico):
        nuevo_nodo = NodoHistorial(paciente, diagnostico)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        print(f"Atención registrada para el paciente {paciente}.")

class Consultorio:
    def __init__(self):
        self.citas = ListaEnlazadaCitas()
        self.urgencias = ColaUrgencias()
        self.historial = ListaDobleHistorial()

    def agendar_cita(self):
        cedula = input("Ingrese la cédula del paciente: ")
        info_cita = input("Ingrese la información de la cita: ")
        self.citas.agregar_cita(cedula, info_cita)

    def registrar_urgencia(self):
        nombre = input("Ingrese el nombre del paciente: ")
        self.urgencias.registrar_paciente(nombre)

    def atender_paciente(self):
        print("\n--- Opciones de Atención ---")
        print("1. Atender paciente de urgencias")
        print("2. Atender paciente con cita")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            paciente = self.urgencias.atender_paciente()
            if paciente:
                diagnostico = input(f"Ingrese el diagnóstico para el paciente {paciente}: ")
                self.historial.registrar_atencion(paciente, diagnostico)
        elif opcion == "2":
            cita = self.citas.atender_cita()
            if cita:
                print(f"Atendiendo cita de la cédula {cita.cedula}: {cita.info_cita}")
                diagnostico = input(f"Ingrese el diagnóstico para el paciente con cédula {cita.cedula}: ")
                self.historial.registrar_atencion(f"Cédula {cita.cedula}", diagnostico)
        else:
            print("Opción no válida.")

    def mostrar_historial(self):
        actual = self.historial.cabeza
        if not actual:
            print("No hay atenciones registradas.")
        else:
            print("Historial de atenciones:")
            while actual:
                print(f"Paciente: {actual.paciente}, Diagnóstico: {actual.diagnostico}")
                actual = actual.siguiente

def menu():
    consultorio = Consultorio()
    while True:
        print("\n--- Menú del Consultorio Médico ---")
        print("1. Agendar cita de consulta externa")
        print("2. Registrar paciente para urgencias")
        print("3. Atender paciente")
        print("4. Ver historial de atenciones")
        print("5. Salir")
        print("Javier Silva – 202155303 y Santiago Vásquez - 202155257")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultorio.agendar_cita()
        elif opcion == "2":
            consultorio.registrar_urgencia()
        elif opcion == "3":
            consultorio.atender_paciente()
        elif opcion == "4":
            consultorio.mostrar_historial()
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
