import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import folium

# Creación de la aplicación Dash
app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

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


# Lista de opciones para el dropdown (nombre de las veredas)
#dropdown_options = [{'label': vereda, 'value': vereda} for vereda in df_plantas_agua['Vereda'].unique()]
# Lista de opciones para el dropdown (nombre de las veredas)
dropdown_options = [{'label': vereda, 'value': vereda} for vereda in df_plantas_agua['Vereda'].unique()]


# Diseño de la aplicación
app.layout = html.Div([
    html.Div(html.H1('Hello Dash')),
    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(html.H5("Nombre de la Planta")),
                dbc.CardBody(id="ptap-card-body", className="card-body"),
            ], className="mx-2"),
        ),
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(html.H5("Número de Usuarios")),
                dbc.CardBody(id="usuarios-card-body", className="card-body"),
            ], className="mx-2"),
        ),
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(html.H5("Caudal en Litros/segundo")),
                dbc.CardBody(id="caudal-card-body", className="card-body"),
            ], className="mx-2"),
        )
    ], className="g-0"),
    dbc.Row([
        dbc.Col(), 
        dbc.Col(html.Div(html.H3("Eligir Acueducto"))), 
        dbc.Col()
    ]),
    dbc.Row([
        dbc.Col(width=2),  # Columna vacía para espacio a la izquierda
        dbc.Col(
            dcc.Dropdown(
                id='acueducto-dropdown',
                options=dropdown_options,
                value=dropdown_options[0]['value']
            ),
            className="mx-2"
        ),  # Tarjeta "elije"
        dbc.Col(width=2)   # Columna vacía para espacio a la derecha
    ]),
    html.Div(style={'height': '20px'}),  # Espacio en blanco con altura de 20px
    dbc.Row([dbc.Col(html.Div(html.H6(""))), dbc.Col(html.Div(html.H6("")))]),
    dbc.Row([
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(html.H5("Información de la Línea")),
                dbc.CardBody(id="info-linea-card-body", className="card-body"),
            ], className="mx-2"),
        )
    ]),
    dbc.Row([
        dbc.Col([
            html.Iframe(id='mapa-iframe', width='100%', height='600')
        ])
    ]),  # Mapa de Folium
    dbc.Row(),  # Fila vacía si deseas añadir más contenido debajo
])

# Callback para actualizar las tarjetas con la información correspondiente a la selección del dropdown
@app.callback(
    [Output("ptap-card-body", "children"),
     Output("usuarios-card-body", "children"),
     Output("caudal-card-body", "children"),
     Output("info-linea-card-body", "children"),
     Output('mapa-iframe', 'srcDoc')],
    [Input("acueducto-dropdown", "value")]
)
def update_cards(selected_vereda):
    if selected_vereda:
        # Filtrar el DataFrame por la vereda seleccionada
        filtered_data = df_plantas_agua[df_plantas_agua['Vereda'] == selected_vereda]
        # Obtener la información para las tarjetas
        ptap_name = filtered_data.iloc[0]['Nombre de la Planta']
        num_users = filtered_data.iloc[0]['Número de Usuarios']
        caudal = filtered_data.iloc[0]['Caudal de Servicio (litros/segundo)']
        # Nuevos datos para la última tarjeta
        admin = filtered_data.iloc[0]['Ente Administrador']
        num_habitantes = filtered_data.iloc[0]['Número de Habitantes']
        tipo_planta = filtered_data.iloc[0]['Tipo de Planta']
        # Crear el contenido de las tarjetas actualizadas
        ptap_card_content = html.H4(ptap_name, className="card-title")
        users_card_content = html.H4(num_users, className="card-title")
        caudal_card_content = html.H4(caudal, className="card-title")
        # Contenido para la última tarjeta
        info_linea_content = [
            html.P(f"Ente Administrador: {admin}"),
            html.P(f"Número de Habitantes: {num_habitantes}"),
            html.P(f"Tipo de Planta: {tipo_planta}")
        ]
        # Generar el mapa de Folium
        mapa_html = generate_map(filtered_data['Latitud'].values[0], filtered_data['Longitud'].values[0])
        return ptap_card_content, users_card_content, caudal_card_content, info_linea_content, mapa_html
    # Si no hay selección, devolver tarjetas vacías
    return [html.Div(), html.Div(), html.Div(), html.Div(), '']

# Función para generar el mapa de Folium
def generate_map(latitud, longitud):
    # Crear mapa de Folium
    mapa = folium.Map(location=[latitud, longitud], zoom_start=15)
    # Marcar la ubicación en el mapa
    folium.Marker(location=[latitud, longitud], popup='Ubicación de la Planta').add_to(mapa)
    # Convertir el mapa de Folium a HTML
    mapa_html = mapa._repr_html_()
    return mapa_html

# Ejecutar la aplicación si este archivo es el principal
#if __name__ == "__main__":
    #app.run_server(debug=True, port=8050)
