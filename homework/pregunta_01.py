# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    import os
    import pandas as pd
    import zipfile

    raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    ruta_input = os.path.join(raiz, 'input')
    carpeta_salida = os.path.join(raiz, 'files', 'output')
    os.makedirs(carpeta_salida, exist_ok=True)

    archivo_zip = os.path.join(raiz, 'files', 'input.zip')
    if not os.path.isdir(ruta_input):
        with zipfile.ZipFile(archivo_zip, 'r') as archivo:
            archivo.extractall(raiz)

    def cargar_textos(nombre_carpeta):
        registros = []
        categorias = ['positive', 'negative', 'neutral']
        for clase in categorias:
            ubicacion = os.path.join(ruta_input, nombre_carpeta, clase)
            if not os.path.isdir(ubicacion):
                continue
            for nombre_archivo in os.listdir(ubicacion):
                if nombre_archivo.endswith('.txt'):
                    archivo_txt = os.path.join(ubicacion, nombre_archivo)
                    with open(archivo_txt, encoding='utf-8') as texto:
                        contenido = texto.read().strip()
                        registros.append({'phrase': contenido, 'target': clase})
        return registros

    for particion in ['train', 'test']:
        conjunto = cargar_textos(particion)
        tabla = pd.DataFrame(conjunto)
        tabla.to_csv(os.path.join(carpeta_salida, f'{particion}_dataset.csv'), index=False)

