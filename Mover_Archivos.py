import os
import shutil

from_dir = "C:/Users/Lenovo Franco/Downloads"
to_dir = "C:/Users/Lenovo Franco/Documents/Archivos_Documentos"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files:
    name, extencion = os.path.splitext(i)
    #print(name)
    #print(extencion)
    if extencion == "":
        continue
    if extencion in ['.txt', '.doc', '.docx', '.pdf']:
        ruta1 = from_dir+'/'+i
        ruta2 = to_dir+'/'+"Archivos_Documentos"
        ruta3 = to_dir+'/'+"Archivos_Documentos"+'/'+i
        if os.path.exists(ruta2):
            print("Moving" + i + "...")

            shutil.move(ruta1, ruta2)

        else:
            os.makedirs(ruta2)
            print("Moving" + i + "...")
            shutil.move(ruta1, ruta3)