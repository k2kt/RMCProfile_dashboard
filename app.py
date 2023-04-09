import base64
import io
import dash
from dash import html, dcc
import dash_bio as dashbio
from dash.dependencies import Input, Output
from dash_bio.utils import xyz_reader

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False,
        accept='.xyz'
    ),
    html.Div([
        dcc.Dropdown(
            id='default-speck-preset-views',
            options=[
                {'label': 'Default', 'value': 'default'},
                {'label': 'Ball and stick', 'value': 'stickball'}
            ],
            value='default'
        ),
    ], style={'margin': '10px'}),
    html.Div(id='output')
])

@app.callback(Output('output', 'children'),
              Input('upload-data', 'contents'),
              Input('default-speck-preset-views', 'value'))
def update_output(contents, preset_view):
    if contents is not None:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string).decode('utf-8')
        xyz_data = xyz_reader.read_xyz(datapath_or_datastring=decoded, is_datafile=False)
        return dashbio.Speck(
            id='default-speck',
            data=xyz_data,
            presetView=preset_view
        )

if __name__ == '__main__':
    app.run_server(debug=True)