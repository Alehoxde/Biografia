#Mapa 
import webbrowser

# Puedes usar dirección o coordenadas
ubicacion = "Bogotá, Colombia"
# ubicacion = "40.4168,-3.7038"  # coordenadas

url = f"https://www.google.com/maps/place/Cra+20+%23+49-10,+Teusaquillo,+Bogot%C3%A1,+D.C.,+Bogot%C3%A1,+Bogot%C3%A1,+D.C./@4.637502,-74.0744487,17z/data=!3m1!4b1!4m6!3m5!1s0x8e3f9a3210826455:0x31a5cf3673f2d916!8m2!3d4.6374967!4d-74.0718738!16s%2Fg%2F11rtlxzqt7!5m1!1e2?entry=ttu&g_ep=EgoyMDI2MDIwNC4wIKXMDSoASAFQAw%3D%3D"

webbrowser.open(url)
