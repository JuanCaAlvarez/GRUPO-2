class HistorialNavegacion:
    def __init__(self):
        # Inicializamos la pila vacía
        self.pila = []

    def visitar(self, url):
        # a) Agrega la página a la pila
        self.pila.append(url)
        print(f"Visitando: {url}")
        print(f"Historial actual: {self.pila}")

    def retroceder(self):
        # b) Quita la última página si la pila no está vacía
        if len(self.pila) > 1:
            pagina_eliminada = self.pila.pop()
            print(f"\nRetrocediendo... (Saliendo de {pagina_eliminada})")
            print(f"Regresaste a: {self.pagina_actual()}")
        elif len(self.pila) == 1:
            print("\nEstás en la página inicial, no puedes retroceder más.")
        else:
            print("\nEl historial está vacío.")

    def pagina_actual(self):
        # c) Muestra la última página sin quitarla (es el índice -1)
        if self.pila:
            return self.pila[-1]
        return "Ninguna"

# --- d) Prueba del sistema ---
navegador = HistorialNavegacion()

navegador.visitar("Google")
navegador.visitar("YouTube")
navegador.visitar("GitHub")

navegador.retroceder()
navegador.retroceder()

print(f"\nEstado final - Página actual: {navegador.pagina_actual()}")