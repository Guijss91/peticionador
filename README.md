# peticionador
# PROMPT

Crie uma aplicação frontend com design moderno e que impressione.

A aplicação funciona como um formulario web com as seguintes caracteristicas:



Envia todos os campos em formato JSON pra o seguinte endpoint: "https://n8neditor.ljit.com.br/webhook-test/peticionador";



Ele possui os seguintes campos de entrada de texto:

1- Tipo de ação (texto normalmente curto)

2- Juizo (texto normalmente curto)

3- Partes (texto curto)

4- Fatos (texto longo)

5- Pedido (texto longo)

6- Valor da causa (valor monetario R$ - Reais, deve aceitar apenas entrada de numeros e deve possuir uma mascara para que o valor seja exibido no sgeuinte formato: Exemplo - R$ 234,00)

A aplicação é destinada ao uso mobile e web desktop.
Quero que o campo "partes" seja mais fino e estreito e possua uma opção de "adicionar parte" para adicionar mais partes ao processo, assim como a possibilidade de informar se é requerido ou requerente no processo.

A aplicação deve aguardar a resposta da requisição que será um JSON de texto longo no seguinte formato:


  {
    "output": "Excelentíssimo Senhor Doutor Juiz de Direito da 2ª Vara de Família e Sucessões,\n\nMaria Silva Santos, brasileira, cabeleireira autônoma, residente e domiciliada na endereço completo constante nos documentos anexos], inscrita no CPF sob o nº [informar], nesta ato representando seu filho menor Pedro Lucas Santos Oliveira..."
  }


Utilize python, flask e tailwind como tecnologias.
O projeto será dockerizado, portanto ao final traga os arquivos necessarios. Exemplo: dockefile, requirements.txt, etc
Não há necessidade de criar um docker compose.

