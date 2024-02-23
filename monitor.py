import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import folium
from tabla import dropdown_options
from dataframe import df_plantas_agua

# Inicia la aplicación Dash con Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define el navbar con un color más acorde al esquema de color de la aplicación
navbar = dbc.NavbarSimple(
    children=[],
    brand="Monitoreo Rural",
    brand_href="#",
    color="#404040",  # Gris oscuro personalizado para el navbar
    dark=True,  # Asegura texto claro sobre el fondo oscuro del navbar
)

# Define el layout de la aplicación
app.layout = dbc.Container(
    [
        navbar,  # Navbar modificado
        html.Div(style={'height': '20px'}),
        dbc.Row(
            [
                dbc.Col(dbc.Card([dbc.CardHeader(html.H5("Nombre de la Planta")),
                                  dbc.CardBody(id="ptap-card-body", className="card-body")]), width=4),
                dbc.Col(dbc.Card([dbc.CardHeader(html.H5("Caudal en Litros/segundo")),
                                  dbc.CardBody(id="caudal-card-body", className="card-body")]), width=4),
                dbc.Col(dbc.Card([dbc.CardHeader(html.H5("Número de Usuarios")),
                                  dbc.CardBody(id="usuarios-card-body", className="card-body")]), width=4),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(
                    id='acueducto-dropdown',
                    options=dropdown_options,
                    value=dropdown_options[0]['value']), width={'size': 6, 'offset': 3}),
            ], className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(html.Div(dbc.Card(
                    [dbc.CardHeader(html.H5("Información de la Línea")),
                     dbc.CardBody(id="info-linea-card-body", className="card-body")]), className="p-3 border bg-light"), width=6),
                dbc.Col([html.Iframe(id='mapa-iframe', width='100%', height='600')], width=6),
            ]
        ),
    ],
    fluid=True,
)

# Callbacks para actualizar el contenido basado en la selección del usuario
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
        admin = filtered_data.iloc[0]['Ente Administrador']
        num_habitantes = filtered_data.iloc[0]['Número de Habitantes']
        tipo_planta = filtered_data.iloc[0]['Tipo de Planta']
        # Crear el contenido de las tarjetas actualizadas
        ptap_card_content = html.H4(ptap_name, className="card-title")
        users_card_content = html.H4(num_users, className="card-title")
        caudal_card_content = html.H4(caudal, className="card-title")
        info_linea_content = [
            html.P(f"Ente Administrador: {admin}"),
            html.P(f"Número de Habitantes: {num_habitantes}"),
            html.P(f"Tipo de Planta: {tipo_planta}")
        ]
        # Generar el mapa de Folium
        mapa_html = generate_map(filtered_data['Latitud'].values[0], filtered_data['Longitud'].values[0])
        return ptap_card_content, users_card_content, caudal_card_content, info_linea_content, mapa_html
    return [html.Div(), html.Div(), html.Div(), html.Div(), '']

# Función para generar el mapa de Folium
def generate_map(latitud, longitud):
    mapa = folium.Map(location=[latitud, longitud], zoom_start=15)
    folium.Marker(location=[latitud, longitud], popup='Ubicación de la Planta').add_to(mapa)
    mapa_html = mapa._repr_html_()
    return mapa_html

if __name__ == '__main__':
    app.run_server(debug=True, port=4000)
