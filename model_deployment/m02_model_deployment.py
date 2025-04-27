#!/usr/bin/python

import pandas as pd
import joblib
import sys
import os

def predict_popu(duration_ms, explicit):
    """
    Predice la probabilidad de popularidad de una canción basada en sus características.

    Args:
        duration_ms (int or str): Duración de la canción en milisegundos.
        explicit (int or str): Si la canción es explícita (1) o no (0).

    Returns:
        float: Probabilidad de que la canción sea popular.
    """
    # Carga el modelo entrenado
    try:
        clf = joblib.load(os.path.join(os.path.dirname(__file__), 'modelo_popularidad.pkl'))
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        return None

    try:
        duration_ms = int(duration_ms)
    except Exception:
        print("Advertencia: duration_ms no es un entero válido.")
        return None
    try:
        explicit = int(explicit)
        if explicit not in [0, 1]:
            print("Advertencia: explicit debe ser 0 o 1.")
            return None
    except Exception:
        print("Advertencia: explicit no es un entero válido (debería ser 0 o 1).")
        return None

    # Crear el DataFrame de entrada como en el ejemplo proporcionado
    input_data = pd.DataFrame({
        'duration_ms': [duration_ms],
        'explicit': [explicit],
    })

    try:
        popularidad = clf.predict(input_data)
    except Exception as e:
        print(f"Error al predecir la probabilidad: {e}")
        return None

    return popularidad


#probabilidad_popularidad = predict_popu(300000,0)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print('Por favor, proporciona los tres argumentos requeridos: duration_ms, explicit')
        print('Ejemplo: 200000 0')

    else:
        duration_ms = sys.argv[1]
        explicit = sys.argv[2]
        
        probabilidad_popularidad = predict_popu(duration_ms, explicit)

        print(f"Argumentos recibidos: duration_ms={duration_ms}, explicit={explicit}")
        print('Probabilidad de popularidad: ', probabilidad_popularidad)