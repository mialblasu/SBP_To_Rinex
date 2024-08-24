#-------------------------------------------------------------------------------
# Name:        module1
# Purpose: Convers sbp files into rinex 3.00
#It is mandatory to put the new sbp files in the os.chdir directory
#
# Author:      migue
#
# Created:     10-06-2019
# Copyright:   (c) migue 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, subprocess, shutil

Altura = input("Entre la altua instrumental con 4 decimales (termina en 1) ")


directory =("C:/SBP_TO_RINEX/")

line_num = 9
line_num = 11

# Texto que debe reemplazar las lineas 9 y 11 respectivamente
text = "HXCGPS500           HXCGPS500                               ANT # / TYPE\n"
text1 = "        "+str(Altura)+"        0.0000        0.0000                  ANTENNA: DELTA H/E/N\n"

# Funcion para reemplazar texto de nombre de antena y altura instrumental en el arvhivo de observaciones rinex
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

# Comando de linea para convertir sbp to rinex
comando = "sbp2rinex.exe -v 3.00 C:/SBP_TO_RINEX/"

cwd = os.getcwd()
print cwd

os.chdir("C:/SBP_TO_RINEX")
print os.chdir("C:/SBP_TO_RINEX")

# ahora si la magia
for filename in os.listdir(cwd):
    if filename.endswith(".sbp"):
        os.mkdir(cwd+"/"+filename[:4])  #  [:4]
        subprocess.call(comando+filename, shell=True)
        shutil.move(directory+(filename[:4])+"-00000.obs",directory+filename[:4]+"/"+(filename[:4]+".obs"))
        shutil.move(directory+(filename[:4])+"-00000.nav",directory+filename[:4]+"/"+(filename[:4]+".nav"))
        shutil.move(directory+(filename[:4])+"-00000.sbs",directory+filename[:4]+"/"+(filename[:4]+".sbs"))
        file_name = (directory+filename[:4]+"/"+(filename[:4]+".obs"))
        replace_line(file_name,9,text)
        replace_line(file_name,11,text1)

        print filename

        continue
    else:
        continue

print ("Todo Termino con EXITO")







