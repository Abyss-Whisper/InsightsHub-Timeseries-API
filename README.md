# InsightsHub-Timeseries-API
Esse projeto contém APIs e configurações para requisições de GET/PUT da plataforma Insights Hub, da Siemens. 

# How to Use
## Dependências🧵
Baixe o `.zip` ou `git clone` nesse repositório para acessar as aplicações. Verifique o "requirements.txt" para olhar quais *imports* precisarão ser feitos (o principal sendo ele, o `Pandas`, para tratamantos de dados).
## Credenciais do ***Bearer Token***🔐
No Insights, você precisa assegurar de que está usando as credencias de aplicação corretas, para isso, registre um aplicativo ***(tutorial em construção)***. Quando você adquirir essas credênciais, insira elas no arquivo `main.py`.
Após inserir as credênciais, recomendo que user o comando `print(mindsphere.getBearerToken())`, assim você receberá o token. 
Não se preocupe em colocar esse token em alguma parte do código, o script lida com isso sozinho. Sempre que uma nova requisição é feitas, um novo Bearer Token é gerado em JSON, e o script usa esse `access_token` para fazer as requisições.
## Retrieve dos dados📊
No arquivo `main.py`, edite os campos: 
- Asset Id
- Aspect Name
- fromDateTime
- toDateTime

Depois da edição, utilize o `print` para aquisitar os dados desejados.
Exemplo: `print(mindsphere.getTimeSeries(assetId,aspectName,fromDateTime,toDateTime))`

## Uso do Pandas🐼
O `Pandas` é usado apenas para formatar os dados do JSON que será recebido pelo GET. EDITE o quanto você quiser!

## Considerações importantes
### Editar o MindSphere.py
Se você reparar, o `MindSphere.py` possui uma lista de GET e algumas formatações montadas já. Caso queira receber outras mensagens ou receber valores diferentes vindo daquele GET, edite as funções `def` do `get` para retornar o que você deseja.
### V3 e V4
No atual momento, estamos usando a versão V3 das APIs. Com o decorrer do tempo, a V4 irá surgir. Caso esse rep não seja atualizado, lembre-se de trocar no ser código 😉!
### RAW TimeSeries Aggregates TimeSeries
A API que estamos usando, se beneficias do RAW TimeSeries, ou seja, devido a uma limitação da plataforma InsightsHub, o máx de período que conseguimos requisitar são: 
- 90 dias
- 2000 datapoints
