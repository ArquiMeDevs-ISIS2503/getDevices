# getDevices

La funcionalidad de este microservicio es: Un microservicio de consulta de devices por sede y sin sede. Para correr el microservicio se debe ejecutar el siguiente comando:

```bash
$ python3 -m uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

En primer lugar, siga los siguientes pasos para la instalación en la máquina virtual de interés:

0. Clone el repositorio

```bash
git clone https://github.com/ArquiMeDevs-ISIS2503/getDevices.git
```

1. Instalar pip 

```bash
sudo apt update
sudo apt install python3-pip
```

2. Instalar las dependencias del proyecto al ingresar a la carpeta del proyecto

```bash
cd getDevices
pip3 install -r requirements.txt
```

Para detener la ejecución del microservicio se debe presionar las teclas Ctrl + C. Además para probar ambos debe ingresar a la siguiente dirección: http://34.72.34.0:8080/{nombre del endpoint}.