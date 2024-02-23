import pandas as pd

# Crear el DataFrame
data = {
    'Nombre de la Planta': ['Soledad', 'Carbonero', 'La Sirena', 'Montebello', 'Campoalegre', 'Cascajal', 'Voragine', 'Alto los Mangos', 'Pichinde', 'Km18'],
    'Vereda': ['La Buitrera cabecera', 'La Buitrera-Fonda', 'La Sirena', 'Montebello Cabecera', 'Campoalegre', 'Cascajal', 'Voragine', 'Alto los Mangos', 'Pichinde', 'Kilometro 18'],
    'Corregimiento': ['La Buitrera', 'La Buitrera', 'La Buitrera', 'Montebello', 'Montebello', 'Hormiguero', 'Pance', 'Buitrera','Pichinde', 'La Elvira'],
    'Tipo de Planta': ['Convencional-FIME', 'Convencional-FIME', 'Convencional-FIME', 'Convencional', 'Convencional-FIME', 'Compacta', 'Convencional-FIME', 'Convencional-FIME', 'Convencional-FIME', 'Convencional-FIME'],
    'Caudal de Servicio (litros/segundo)': [13.0, 10.0, 10.0, 30.0, 10.0, 12.6, 3, 3.5, 6.3, 1],
    'Número de Usuarios': [2000, 1800, 2000, 5000, 1000, 427, 90, 533, 293, 60],
    'Número de Habitantes': [10000, 9000, 10000, 25000, 5000, 1708, 360, 2132, 1172, 300],
    'Ente Administrador': ['Acuabuitrera', 'Acuabuitrera', 'ASAVLASI', 'ASUSERVICIOS MONTEBELLO', 'ACOPS', 'ASOCASCAJAL', 'ASOVORAGINE', 'J.A.A.  Alto los Mangos', 'ACUAPICHINDE', 'ACUA18'],
    'Latitud': [3.38795, 3.37828, 3.40170, 3.46988, 3.50268, 3.31742, 3.34090, 3.39228, 3.44003, 3.51468],
    'Longitud': [-76.59043, -76.59383, -76.57929, -76.55201, -76.56131, -76.51000, -76.59922, -76.58783, -76.62250, -76.62290]
}

df_plantas_agua = pd.DataFrame(data)

