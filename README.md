# getDevices :stethoscope:

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://god.gw.postman.com/run-collection/23133886-86c51ae9-6904-41e0-82d6-2f6dc9c8baf4?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D23133886-86c51ae9-6904-41e0-82d6-2f6dc9c8baf4%26entityType%3Dcollection%26workspaceId%3Da85db7f7-a2a8-4feb-a95e-057fc72e8379)

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

3. Una vez instaladas las dependencias, se debe ejecutar el siguiente comando para correr el microservicio

```bash
python3 -m uvicorn main:app --host 0.0.0.0 --port 8080
```

Para detener la ejecución del microservicio se debe presionar las teclas Ctrl + C. Además para probar ambos debe ingresar a la siguiente dirección: http://35.225.29.96:8080/{nombre del endpoint}. A continuación se encuentran los endpoints disponibles:

1. /devices/{sede} : Consulta los devices de una sede en específico. Ejemplo: http://35.225.29.96:8080/devices/sede/Barrancabermeja
2. /devices : Consulta todos los devices. Ejemplo: http://35.225.29.96:8080/devices