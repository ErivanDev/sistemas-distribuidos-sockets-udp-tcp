# Atividade SD - Erivan, Paulo Henrique, Ribamar - Wireshark 

Foi escolhida a linguagem python e implementado um cliente e um servidor socket usando UDP e outro par de software usando TCP. 

Nos dois casos, a aplicação cliente funciona como um conversor de moedas na qual o usuário informa via console um valor (R$ 10) e a moeda desejada (e.g., dólar), essas informações são enviadas à aplicação servidora que realiza o cálculo de acordo com a cotação atual da moeda (e.g., use uma função randômica para gerar esse valor). A resposta da conversão é então enviada de volta para o cliente.