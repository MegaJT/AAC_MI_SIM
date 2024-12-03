#https://aac-mi-sim.onrender.com 
import dash
from dash import Dash, dcc, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np


# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])
server = app.server

# Load CSV data
data = pd.read_csv('AAC_FI_MS CSV.csv', index_col=False)


'''
Reserve code for selecting multi answers in the dropdown box
months_available = sorted(data['Month'].unique())
visits_available = sorted(data['Visit'].unique())
options=[{'label': month, 'value': month} for month in months_available],
        value=months_available,  # Default to selecting all
'''        
# Mapping dictionaries
month_dict = {1: 'July', 2: 'August', 3: 'September', 4: 'October'}
visit_dict = {1: '1st Visit', 2: '2nd Visit'}
segment_dict = {1: 'Seg D', 2: 'SUV B', 3: 'SUV C', 4: 'SUV D', 5: 'SUV F'}
model_dict = {
    1: 'Land Cruiser', 2: 'Coolray', 3: 'Accord', 4: 'RAV4', 5: 'Expedition',
    6: 'Territory', 7: 'Sonata', 8: 'Seltos', 9: 'Camry', 10: 'Tucson',
    11: 'Rush', 12: 'Altima', 13: 'Kicks', 14: 'X-Trail', 15: 'Patrol'
}
bank_dict = {
    1: 'ADCB', 2: 'ADIB', 3: 'DIB', 4: 'EIB', 5: 'ENBD', 6: 'EID', 7: 'FAB'
}
insurance_dict = {
    1: 'Adnic', 2: 'Al Ahlia', 3: 'Al Hilal', 4: 'Allaiance', 5: 'AXA',
    6: 'DIG', 7: 'Emirates', 8: 'GAG', 9: 'GIG', 10: 'Liva',
    11: 'Meta takaful', 12: 'Oman Insurance', 13: 'Orient Insurance',
    14: 'Orient Takaful', 15: 'RSA', 16: 'Sukoon', 17: 'Takaful', 18: 'DIC'
}
loan_tenure_dict = {
    1: '3 Years', 2: '4 Years', 3: '5 Years'
}


# Map numeric values to their respective labels in the DataFrame
data['Month'] = data['Month'].map(month_dict)
data['Visit'] = data['Visit'].map(visit_dict)
data['Segment'] = data['Segment'].map(segment_dict)
data['Model'] = data['Model'].map(model_dict)

data['Rec_Bank_1'] = data['Rec_Bank_1'].replace(' ', 0).astype(int)
data['Rec_Bank_1'] = data['Rec_Bank_1'].map(bank_dict).fillna('None')

data['Rec_Bank_2'] = data['Rec_Bank_2'].replace(' ', 0).astype(int)
data['Rec_Bank_2'] = data['Rec_Bank_2'].map(bank_dict).fillna('None')

data['Rec_Bank_3'] = data['Rec_Bank_3'].replace(' ', 0).astype(int)
data['Rec_Bank_3'] = data['Rec_Bank_3'].map(bank_dict).fillna('None')

data['Ins_Company_1'] = data['Ins_Company_1'].replace(' ', 0).astype(int)
data['Ins_Company_1'] = data['Ins_Company_1'].map(insurance_dict).fillna('None')

data['Ins_Company_2'] = data['Ins_Company_2'].replace(' ', 0).astype(int)
data['Ins_Company_2'] = data['Ins_Company_2'].map(insurance_dict).fillna('None')

data['Ins_Company_3'] = data['Ins_Company_3'].replace(' ', 0).astype(int)
data['Ins_Company_3'] = data['Ins_Company_3'].map(insurance_dict).fillna('None')

data['Loan_Tenure_Yrs_1'] = data['Loan_Tenure_Yrs_1'].replace(' ', 0).astype(int)
data['Loan_Tenure_Yrs_1'] = data['Loan_Tenure_Yrs_1'].map(loan_tenure_dict).fillna('None')

data['Loan_Tenure_Yrs_2'] = data['Loan_Tenure_Yrs_2'].replace(' ', 0).astype(int)
data['Loan_Tenure_Yrs_2'] = data['Loan_Tenure_Yrs_2'].map(loan_tenure_dict).fillna('None')

data['Loan_Tenure_Yrs_3'] = data['Loan_Tenure_Yrs_3'].replace(' ', 0).astype(int)
data['Loan_Tenure_Yrs_3'] = data['Loan_Tenure_Yrs_3'].map(loan_tenure_dict).fillna('None')

data['Interest_Rate_1'] = data['Interest_Rate_1'].replace(' ', np.nan).astype(float)
data['Interest_Rate_1']=data['Interest_Rate_1']*100

data['Interest_Rate_2'] = data['Interest_Rate_2'].replace(' ', np.nan).astype(float)
data['Interest_Rate_2']=data['Interest_Rate_2']*100

data['Interest_Rate_3'] = data['Interest_Rate_3'].replace(' ', np.nan).astype(float)
data['Interest_Rate_3']=data['Interest_Rate_3']*100

data['Downpayment_Perc_1'] = data['Downpayment_Perc_1'].replace(' ', np.nan).astype(float)
data['Downpayment_Perc_1']=data['Downpayment_Perc_1']*100

data['Downpayment_Perc_2'] = data['Downpayment_Perc_2'].replace(' ', np.nan).astype(float)
data['Downpayment_Perc_2']=data['Downpayment_Perc_2']*100

data['Downpayment_Perc_3'] = data['Downpayment_Perc_3'].replace(' ', np.nan).astype(float)
data['Downpayment_Perc_3']=data['Downpayment_Perc_3']*100


data['Processing_Fees_AED_1'] = data['Processing_Fees_AED_1'].replace(' ', np.nan).astype(float)
data['Processing_Fees_AED_1']=data['Processing_Fees_AED_1']*100

data['Processing_Fees_AED_2'] = data['Processing_Fees_AED_2'].replace(' ', np.nan).astype(float)
data['Processing_Fees_AED_2']=data['Processing_Fees_AED_2']*100

data['Processing_Fees_AED_3'] = data['Processing_Fees_AED_3'].replace(' ', np.nan).astype(float)
data['Processing_Fees_AED_3']=data['Processing_Fees_AED_3']*100

data['Insurance_Rate_Perc_1'] = data['Insurance_Rate_Perc_1'].replace(' ', np.nan).astype(float)
data['Insurance_Rate_Perc_1']=data['Insurance_Rate_Perc_1']*100

data['Insurance_Rate_Perc_2'] = data['Insurance_Rate_Perc_2'].replace(' ', np.nan).astype(float)
data['Insurance_Rate_Perc_2']=data['Insurance_Rate_Perc_2']*100

data['Insurance_Rate_Perc_3'] = data['Insurance_Rate_Perc_3'].replace(' ', np.nan).astype(float)
data['Insurance_Rate_Perc_3']=data['Insurance_Rate_Perc_3']*100



data.to_excel('output.xlsx', index=False)
# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([html.Img(src='assets/DG_Logo.png', height="100px")],width=3),
        dbc.Col([
            html.H1("F&I MS Study 2024", className="text-center mb-4"),
        ],width=6),    
        dbc.Col([""],width=3),
    dbc.Row([html.Hr()]),    
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Label("MONTH(S):"),
            dcc.Dropdown(id='month', options=[{'label': v, 'value': v} for v in month_dict.values()], multi=True, placeholder="Select Month(s)"),
        ],width=3),
        dbc.Col([    
            html.Label("VISIT(S):"),
            dcc.Dropdown(id='visit', options=[{'label': v, 'value': v} for v in visit_dict.values()], multi=True, placeholder="Select Visit(s)"),
        ],width=3),
        dbc.Col([        
            html.Label("SEGMENT:"),
            dcc.Dropdown(id='segment', options=[{'label': v, 'value': v} for v in segment_dict.values()], placeholder="Select Segment"),
        ],width=3),            
        dbc.Col([        
            html.Label("MODEL:"),
            dcc.Dropdown(id='model', placeholder="Select Model"),
         ],width=3),         
            html.Hr(),
            dbc.Button('Submit', id='submit-button', n_clicks=0),
        
    ]),
    html.Br(),
    dbc.Row([html.H4("Bank Details", className="text-center mb-4"), dash_table.DataTable(id='bank-data-table', style_table={'overflowX': 'auto'}, style_cell={'textAlign': 'center'})]),
    html.Br(),
    dbc.Row([html.H4("Insurance Details", className="text-center mb-4"), dash_table.DataTable(id='insurance-data-table', style_table={'overflowX': 'auto'}, style_cell={'textAlign': 'center'})])
])

# Callback to update Model dropdown based on Segment selection
@app.callback(
    Output('model', 'options'),
    Input('segment', 'value')
)
def update_model_dropdown(segment_val):
    if not segment_val:
        return []
    available_models = data[data['Segment'] == segment_val]['Model'].unique()
    return [{'label': model, 'value': model} for model in available_models]

# Callback to fetch and display data in DataTables based on selected inputs
@app.callback(
    [Output('bank-data-table', 'data'),
     Output('bank-data-table', 'columns'),
     Output('insurance-data-table', 'data'),
     Output('insurance-data-table', 'columns')],
    Input('submit-button', 'n_clicks'),
    State('month', 'value'),
    State('visit', 'value'),
    State('segment', 'value'),
    State('model', 'value')
)
def update_tables(n_clicks, months, visits, segment, model):
    if n_clicks == 0 or not (months and visits and segment and model):
        return [], [], [], []

    # Filter data based on the selected inputs
    filtered_data = data[
        (data['Month'].isin(months)) &
        (data['Visit'].isin(visits)) &
        (data['Segment'] == segment) &
        (data['Model'] == model)
        
    ]

    if filtered_data.empty:
        return [], [], [], []
    


    # Bank details in stacked format
    bank_table_data = []
    for _, row in filtered_data.iterrows():
        if row['Rec_Bank_1'] != 'None':
            bank_table_data.append({'Visit': row['Visit'], 'Month': row['Month'], 'Model': row['Model'], 'Dealer Price': row['Dealer_Price'], 'Bank Name': row['Rec_Bank_1'], 'Interest Rate (%)': f"{row['Interest_Rate_1']:.2f}%", 'Loan Tenure (Years)': row['Loan_Tenure_Yrs_1'], 'Downpayment (%)': f"{row['Downpayment_Perc_1']:.2f}%", 'Processing Fees (%)': f"{row['Processing_Fees_AED_1']:.2f}%"})
        if row['Rec_Bank_2'] != 'None':
            bank_table_data.append({'Visit': row['Visit'], 'Month': row['Month'], 'Model': row['Model'], 'Dealer Price': row['Dealer_Price'], 'Bank Name': row['Rec_Bank_2'], 'Interest Rate (%)': f"{row['Interest_Rate_2']:.2f}%", 'Loan Tenure (Years)': row['Loan_Tenure_Yrs_2'], 'Downpayment (%)': f"{row['Downpayment_Perc_2']:.2f}%", 'Processing Fees (%)': f"{row['Processing_Fees_AED_2']:.2f}%"})
        if row['Rec_Bank_3'] != 'None':
            bank_table_data.append({'Visit': row['Visit'], 'Month': row['Month'], 'Model': row['Model'], 'Dealer Price': row['Dealer_Price'], 'Bank Name': row['Rec_Bank_3'], 'Interest Rate (%)': f"{row['Interest_Rate_3']:.2f}%", 'Loan Tenure (Years)': row['Loan_Tenure_Yrs_3'], 'Downpayment (%)': f"{row['Downpayment_Perc_3']:.2f}%", 'Processing Fees (%)': f"{row['Processing_Fees_AED_3']:.2f}%"})

    bank_columns = [
        {'name': 'Visit', 'id': 'Visit'},
        {'name': 'Month', 'id': 'Month'},
        {'name': 'Model', 'id': 'Model'},
        {'name': 'Dealer Price', 'id': 'Dealer Price'},
        {'name': 'Bank Name', 'id': 'Bank Name'},
        {'name': 'Interest Rate (%)', 'id': 'Interest Rate (%)'},
        {'name': 'Loan Tenure (Years)', 'id': 'Loan Tenure (Years)'},
        {'name': 'Downpayment (%)', 'id': 'Downpayment (%)'},
        {'name': 'Processing Fees %', 'id': 'Processing Fees (%)'}
    ]

    # Insurance details in stacked format
    # Insurance details in stacked format
    insurance_table_data = []
    for _, row in filtered_data.iterrows():
        if row['Ins_Company_1'] != 'None':
            insurance_table_data.append({'Visit': row['Visit'], 'Month': row['Month'], 'Model': row['Model'], 'Insurance Company': row['Ins_Company_1'], 'Insurance Rate (%)': f"{row['Insurance_Rate_Perc_1']:.2f}%"})
        if row['Ins_Company_2'] != 'None':
            insurance_table_data.append({'Visit': row['Visit'], 'Month': row['Month'], 'Model': row['Model'], 'Insurance Company': row['Ins_Company_2'], 'Insurance Rate (%)': f"{row['Insurance_Rate_Perc_2']:.2f}%"})
        if row['Ins_Company_3'] != 'None':
            insurance_table_data.append({'Visit': row['Visit'], 'Month': row['Month'], 'Model': row['Model'], 'Insurance Company': row['Ins_Company_3'], 'Insurance Rate (%)': f"{row['Insurance_Rate_Perc_3']:.2f}%"})


    insurance_columns = [
        {'name': 'Visit', 'id': 'Visit'},
        {'name': 'Month', 'id': 'Month'},
        {'name': 'Model', 'id': 'Model'},
        {'name': 'Insurance Company', 'id': 'Insurance Company'},
        {'name': 'Insurance Rate (%)', 'id': 'Insurance Rate (%)'}
    ]

    return bank_table_data, bank_columns, insurance_table_data, insurance_columns


if __name__ == '__main__':
    app.run_server(debug=True)
