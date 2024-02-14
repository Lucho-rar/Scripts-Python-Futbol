import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Crear una nueva figura y ejes
fig, ax = plt.subplots()

# Cargar la imagen de fondo del campo de fútbol
img = plt.imread('campo.jpg')  # Cambia 'campo_futbol.jpg' por la ruta de tu propia imagen
ax.imshow(img, extent=[0, 100, 0, 100])

# Función para dibujar el disparo al arco
def draw_shot(event):
    if event.button == 1:  # Verificar si es un clic izquierdo
        x_shot, y_shot = event.xdata, event.ydata
        x_target, y_target = 50, 95  # Coordenadas del arco
        plt.plot([x_shot, x_target], [y_shot, y_target], color='green', linewidth=0.5)
        plt.scatter(x_shot, y_shot, color='green')
        plt.draw()

# Conectar la función de dibujo al evento de clic en el gráfico
plt.connect('button_press_event', draw_shot)

# Ajustar los límites de los ejes y aspecto
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.gca().set_aspect('equal', adjustable='box')

# Mostrar el resultado
plt.title('Localización de goles - FASE 1 IDA')
plt.show()
