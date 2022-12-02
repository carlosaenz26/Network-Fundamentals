#%%
from ftplib import FTP, all_errors
import ftplib
import os #Se ingresó este módulo por facilidad en la hora de descargar el archivo
#%%

ftp_server = FTP("157.253.192.111")
usu1 = "pupi" #input("Por favor ingrese su usuario: ") #Se pide el usuario
pass1 = "pupi" #input("Por favor ingrese su contraseña: ") #Se pide la clave

try:
    ftp_server.login(user=usu1,passwd=pass1) #Inicio de sesión FTP mediante las credenciales dadas anteriormente

    print(ftp_server.getwelcome()) #Mensaje de bienvenida
    print("Se inició sesión correctamente en el cliente FTP")

    ftp_server.cwd('home') #Se accede al directorio donde se encuentran los archivos a analizar
    print("Ubicado exitosamente en la carpeta: "+ ftp_server.pwd())
    ftp_server.retrlines("LIST")

    print("Se ingresó correctamente al directorio")

    # Enter File Name with Extension
    filename = "650k.jpg"
 
# Read file in binary mode
    with open(filename, "wb") as file:
    # Command for Uploading the file "STOR filename"
        ftp_server.retrbinary(f"RETR {filename}", file.write)
    # Display the content of downloaded file
    file= open(filename, "r")
    print('File Content:', file.read())
    
    # Close the Connection
    ftp_server.quit()
                               
        
except Exception as e: #Este except funciona, por ejemplo, en caso que las credenciales dadas sean incorrectas
    print("No se pudo iniciar sesión: "+str(e))
    

ftp_server.close()

# %%
