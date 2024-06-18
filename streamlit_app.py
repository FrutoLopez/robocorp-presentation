import streamlit as st
import time


_WhatRPA = """
# ¿Qué es :red[RPA]?
- Automatización robótica de procesos (:red[**R**]obotic :red[**P**]rocess :red[**A**]utomation)
- Herramienta de automatización de procesos con pasos definidos por medio de bots
- **No** es AI
## Características generales de herramientas de RPA
- Suelen ser :green[low-code] o :green[no-code]
	- Robocorp es :blue[**full**] code
- Tienen capacidad de gestión y despliegue de los bots mediante un orquestrador
- Facilita interacciones entre distintos programas
	- Capaz de interactuar con elementos de UI
- Pueden funcionar de forma:
    - Atendida: que un usuario lo pone a correr a demanda
    - Desatendida: no requiere interacción de usuario para correr
    - Agente: tiene capacidad de interacción con un usuario

"""

tab1, tab2 = st.tabs(["RPA","Robocorp"])

def WhatRPA_stream():
    for word in _WhatRPA.split(" "):
        yield word + " "
        time.sleep(0.00)

with tab1:
    st.write_stream(WhatRPA_stream)
    time.sleep(0.05)
    st.image('Images/cloud-processing-icon-flat-design-J34YRB-04.png',caption="Imagen de Softbotic")
    with st.expander("Vendors"):
        vend1, vend2, vend3 = st.columns(3)
        vend4, vend5, vend6 = st.columns(3)
        vend7, vend8, vend9 = st.columns(3)
        with vend1:
            st.image("Images/Vendors/1MSPA.webp",caption = "Microsoft Power Automate")
        with vend2:
            st.image("Images/Vendors/2UI.png",caption = "UI Path")
        with vend3:
            st.image("Images/Vendors/3AA.png",caption = "Automation Anywhere")
        with vend4:
            st.image("Images/Vendors/4BP.png",caption = "Blue Prism")
        with vend5:
            st.image("Images/Vendors/5AE.jpeg",caption = "AutomationEdge")
        with vend6:
            st.image("Images/Vendors/6IBM.svg",caption = "IBM")
        with vend7:
            st.image("Images/Vendors/7Ap.png",caption = "Appian")
        with vend8:
            st.image("Images/Vendors/8Sap.png",caption = "SAP")
        with vend9:
            st.image("Images/Vendors/9Pe.png",caption = "Pega")

with tab2:
    """
    # ¿Qué es :blue[Robocorp]?
    - Plataforma Open Source de RPA construida sobre Python
        - Inicialmente programable mediante Robot Framework
        - Actualmente se programa utilizando Python
            - Esto le permite utilizar diversas bibliotecas de Python (aunque trabaja mejor con las bibliotecas directas de Robocorp o RPA)
    - Tiene herramientas de gestión por medio de cloud: Control Room
    """
    st.image("Images/control-room-overview.png", caption="Estructura de Robocorp")
    """
    ## ¿Por qué Robocorp vs Python Script?
    - Portabilidad y administraciíón
        - Un task package de Robocorp incluye un archivo de configuración conda.yaml donde se especifican las bibliotecas a utilizar y las versiones de las mismas
        - Si la biblioteca no está presente en el entorno, corre el comando "pip install"
    """
    st.image("Images/conda.png")
    
    """
    - No requiere tener Python instalado para ejecutar un bot
        - El equipo del usuario final puede tener instalado los componentes de agente o trabajador para gestionar el bot desde el orquestador
        - Flexibilidad a la hora de gestionar y desplegar bots
            - Por medio del Control Room
                - Limitado pero funcional para la versión gratuita
            - Por medio de rcc
                - Herramienta de línea de comando que gestiona los entornos de RPA
                - Descarga las dependencias requeridas según el archivo conda
                - Se puede crear un archivo .bat para ejecutarlo sin necesidad de tener un IDE
    """
    st.image("Images/bot-folder.png", caption = "Los archivos necesarios para ejecutar un bot")
    st.image("Images/bat.png", caption = "Ejemplo sencillo de archivo bat para ejecutar el bot")
