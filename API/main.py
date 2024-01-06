from MindSphere import MindSphere
import json
import datetime
import pandas as pd

mindsphere = MindSphere(app_Name="<YOUR_APP_NAME>", #app_name
                        app_Version="<YOUR_APP_VERSION>", #v1.0.0
                        tenant="<YOUR_APP_TENANT>", #tenant
                        gateway_URL="https://gateway.eu1.mindsphere.io/", #don't edit
                        client_ID="<YOUR_Client_ID>", 
                        client_Secret="YOUR_CLIENT_SECRET"
                        )


assetId = "<YOUR_ASSET_ID>" #insira aqui o assetID do seu asset
aspectName = "<YOUR_ASPECT_NAME>" #insira aqui o aspectName do seu asset
fromDateTime = "" #2024-01-01T00:00:00Z <- examplo
toDateTime = ""#2024-01-01T00:00:00Z <- exemplo

#print(mindsphere.getBearerToken()) #printa o token

#print(mindsphere.getTimeSeries(assetId,aspectName,fromDateTime,toDateTime)) #printa a requisição GET, de acordo com o asset e com o Aspect

#print(mindsphere.getTimeSeries(assetId,aspectName,"","")) #retorna o último timestamp disponível

now = datetime.datetime.now() #tempo atual

#print(mindsphere.getAssetList())

print(mindsphere.getTypeList())


#print(mindsphere.putTimeSeriesData(assetId,aspectName,{"_time":now,"temperature":"90.50"})) #utiliza o PUT para colcoar TimeSeries

def sum_teste_values(json_data): #função para pegar o parâmetro desejado da lista JSON que será retornado
    total = 0
    for entry in json_data:
        if 'teste' in entry:
            total += entry['teste']
    return total

# Teste de JSON aleatório:
data = [{'temperature': '990', '_time': '2023-10-10T12:01:00Z'}, 
        {'temperature': '0', '_time': '2023-10-10T12:02:00Z'}, 
        {'teste': 10, '_time': '2023-10-14T02:58:41.477Z'},
        {'teste': 20, '_time': '2023-10-14T03:58:41.477Z'}]

#print("O valor soma é: ",sum_teste_values(mindsphere.getTimeSeries(assetId,aspectName,fromDateTime,toDateTime)))  # imprime o valor da soma

#print(mindsphere.putTimeSeriesData(assetId,aspectName,{"_time":now,"total":sum_teste_values(mindsphere.getTimeSeries(assetId,aspectName,fromDateTime,toDateTime))})) #envia dado somado para o MindSphere


#difinir que o output do GET, é um DataFrama do Pandas
#timeSeries_df=pd.DataFrame(mindsphere.getTimeSeries(assetId,aspectName,fromDateTime,toDateTime))
#print(timeSeries_df)

#adicionar assets ao CSV
#listAsset_df = pd.DataFrame(mindsphere.getTypeList())
#listAsset_df.to_csv(r"C:\...\file_name.csv")

#adicionar type CSV
listTypes_df = pd.DataFrame(mindsphere.getTypeList())
print(listTypes_df)
#listTypes_df.to_csv(r"C:\...\file_name.csv")

#ver as 5 primeiras linhas (caso queria ver mais, troque o valor de X timeSeries_df.head(X))
#print(timeSeries_df.head())

#quantas linhas totais aquele JSON tem
#print(timeSeries_df.shape)

#mostra algumas infos interessantes sobre o JSON
#print(timeSeries_df.describe())