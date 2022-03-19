# escolas-9-cre
Projeto de visualização de dados utilizando folium

O projeto é dividido em duas partes: 1) coleta das informações de latitude e longitude de escolas da 9ª CRE da cidade do Rio de Janeiro e 2) dispor os locais de cada escola no mapa, colorindo os pins de acordo com o tipo de escola (EDI, Ciep, creche, escola e escola especial).

As duas partes são independentes, de forma que a primeira é responsável apenas por colher os dados e estruturá-los, enquando a segunda parte apenas necessita dos dados formatados. Assim, foram utilizadas duas abordagens diferentes. Na primeira abordagem, foi utilizada a API do Bing Maps para realizar consultas aos nomes das escolas. Dentre as informações retornadas pela API, estão justamente as informações de latitude/longitude. Entretanto, as informações retornadas nem sempre eram precisas.

A segunda abordagem utilizou o móduo pyautogui para controlar os eventos de mouse e teclado. Para cada escola da lista, foi realizada uma pesquisa no Google Maps utilizando uma combinação das informações. Duas características cruciais para execução desta abordagem são a) o fato de que a barra de pesquisa do Google Maps fica estática na tela e b) o ponto encontrado fica sempre centralizado no mapa. Além disso, ao clicar com o botão direito na região desejada, um menu de contexto surge e, clicando na primeira opção do menu, as informações de latitude e longitude do ponto são copiadas para a área de transferência.
