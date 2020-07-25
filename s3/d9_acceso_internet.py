import urllib.request as request, json

url = "http://cjgarcia.github.io/datasets/dpy/asistencia.json"

fichero_json = request.urlopen(url).read()

datos = json.loads(fichero_json)

for estudiante in datos[1:]:
    print(estudiante['S3'])
