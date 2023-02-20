class Personaje:
    # atributos Personaje
    especie = "Humano"
    nombre = "Master Chief"
    altura = "2.70"

    # Métodos Personaje
    def correr(self, status):
        if status:
            print("El personaje " + self.nombre + " está corriendo")
        else:
            print("El personaje " + self.nombre + " se detuvo")

    def lanzarGranadas(self):
        print("El personaje " + self.nombre + " lanzó una granada")

    def recargarArma(self, municiones):
        cargador = 10
        cargador += municiones
        print("El arma tiene " + str(cargador) + " balas")


