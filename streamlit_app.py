import streamlit as st
import time



_WhatRPA = """
## ¿Qué es :red[**RPA**]?
- Automatización robótica de procesos (:red[**R**]obotic :red[**P**]rocess :red[**A**]utomation)
- Herramienta de automatización de procesos con pasos definidos por medio de bots
- **No** es AI
### Características generales de herramientas de RPA
- Suelen ser :green[low-code] o :green[no-code]
	- Robocorp es :blue[**full**] code
- Tienen capacidad de gestión y despliegue de los bots mediante un orquestrador
- Facilita interacciones entre distintos programas
	- Capaz de interactuar con elementos de UI

"""





_WhatRobocorp="""
## ¿Qué es Robocorp?
- Plataforma Open Source de RPA construida sobre Python
	- Es programable en Python
- Tiene herramientas de gestión por medio de cloud
"""


def WhatRPA_stream():
    for word in _WhatRPA.split(" "):
        yield word + " "
        time.sleep(0.05)

if st.button("Inicio"):
    st.write_stream(WhatRPA_stream)
    time.sleep(0.05)
    st.image('https://github.com/FrutoLopez/robocorp-presentation/blob/main/.github/workflows/cloud-processing-icon-flat-design-J34YRB-04.png',caption="Imagen de Softbotic")
    with st.expander("Vendors"):
        vend1, vend2, vend3 = st.columns(3)
        vend4, vend5, vend6 = st.columns(3)
        vend7, vend8, vend9 = st.columns(3)
        with vend1:
            st.image("Vendors/1MSPA.webp",caption = "Power Automate")
        with vend2:
            st.image("Vendors/2UI.png",caption = "UI Path")
        with vend3:
            st.image("Vendors/3AA.png",caption = "Automation Anywhere")




