# CER2-DOMENECHJUAN

PROYECTO FUNCIONANDO COMO DEBERIA: https://github.com/JustHipo/CER2-DOMENECHJUAN-FUNCIONA

CAMBIOS SIMPLES HECHOS EN EL CODIGO FUNCIONANDO (hay otros pequeños cambios en la version funcionando, no importantes para el backend)
main.html:
editar referencias en el navbar:
      linea 29 {% url 'home' %}
      linea 32 {% url 'admin:index' %}
      linea 35 {% url 'register' %}
      linea 51 {% block content %}
      linea 99 {% endblock %}
views.py
editar return del def home
      linea 22 return render(request, 'webapp/main.html', DTS)
      linea 64 return redirect(home)
urls.py
agregar el name a home
      linea 13 path("home/", views.home, name="home"),

certamen 2 juan francisco domenech. 
La mayor parte del frontend no funciona, ya que no logra cargar correctamente los comunicados. 
los comunicados pueden ser creados, modificados y publicados por un usuario staff, pero no aparecen en el frontend. solo en la pestaña de administrador

los usuarios pueden registrarse por la pestaña de registro, y para obrener permisos de creacion de comunicados, deben esperar a que el superusuario, llamado admin, contraseña admin, les asigne los permisos, el role y el estatus de staff. 
Hubo un intento de permitir que solo usuarios de role especificos, (es decir informatica, electronica, construccion, etc) puedan crear comunicados para esa area, como se puede ver en los permisos del usuario informaticopromedio. 
no funciono.

La pestaña de registro de usuario funcionaba hasta hace 15 minutos antes de la entrega. no se que la rompió, tampoco creo ser capaz de arreglarlo a este punto ni yo se como funciona mi codigo. por favor considerar que en el codigo si existe una pestaña de registro funcional...en algun lado.

Si bien se le pueden dar los permisos a los usuarios regulares (usuarios anonimos) para ver los comunicados, no pude implementar los comunicados al frontend por lo que no funciona
está el codigo, simplemente me falló css, html, bootstrap y dios

