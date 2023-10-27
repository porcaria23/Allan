# Allan
**PROJETO QR CODE ACESSIBILIDADE: UMA VISÃO INTEGRADA**

# Manual do Painel Administrativo

## Introdução

Olá, Allan! Este é o seu manual passo a passo para utilizar o Painel Administrativo do Projeto QR Code Acessibilidade. Aqui, você encontrará instruções claras e detalhadas para ajudá-lo a gerenciar e atualizar as informações de cada sala, assim como uma breve descrição das tecnologias utilizadas e por que elas foram escolhidas.

## Acesso ao Painel

1. Abra o navegador de sua preferência.
2. Digite ou clique no link: [https://allan23-b11e7f74f497.herokuapp.com/](https://allan23-b11e7f74f497.herokuapp.com/).
3. Aguarde a página carregar completamente.

## Entendendo a Página Inicial

Após acessar o link, você verá uma página com a seguinte estrutura:

- **Logo** no topo da página.
- Uma **tabela** mostrando todos os IDs das salas, o nome da sala e se há um arquivo de áudio associado.
- Três **formulários** abaixo da tabela, para atualizar informações da sala, deletar informações e fazer upload de áudios.

## Como Usar o Painel 
1.**Atualizando Informações de uma Sala**:
  - Role a página até encontrar o formulário intitulado Atualizar.
  - No campo ID, digite o ID da sala que você deseja atualizar.
  - No campo Sala, digite o novo nome ou identificação para a sala.
  - Clique no botão Atualizar.
  - A página será recarregada e as informações da sala correspondente ao ID fornecido serão atualizadas na tabela.
    
2.**Adicionando um Arquivo de Áudio**:
  - No terceiro formulário, intitulado Upload:
  - No campo ID, digite o ID da sala à qual você deseja associar o arquivo de áudio.
  - Clique no botão "Escolher arquivo" ou similar (o nome do botão pode variar de acordo com o navegador) e selecione o arquivo de áudio que você deseja enviar (deve ser .mp3 ou .wav).
  - Clique no botão Upload.
  - A página será recarregada e o arquivo de áudio selecionado será associado à sala correspondente ao ID fornecido.
    
3.**Deletando Informações de uma Sala**:
  - Localize o segundo formulário, intitulado Apagar.
  - No campo ID, digite o ID da sala que você deseja deletar as informações.
  - Clique no botão Apagar.
  - A página será recarregada e as informações da sala selecionada serão redefinidas para os valores padrão.   

## Tecnologias Utilizadas e Por Que Foram Escolhidas
1. **Flask**:
   - *O que é*: Flask é um micro-framework de Python que permite desenvolver aplicações web de maneira rápida e simples.
   - *Por que foi usado*: Por sua simplicidade e leveza, o Flask é uma excelente opção para construção de painéis administrativos e aplicações web de pequeno e médio porte. Ele nos permitiu desenvolver e manter o seu painel com eficiência e sem complicação.

2. **Heroku**:
   - *O que é*: Heroku é uma plataforma em nuvem que permite hospedar, gerenciar e escalar aplicações web.
   - *Por que foi usado*: Heroku é conhecido por sua facilidade de uso e integração direta com várias ferramentas de desenvolvimento, incluindo o Flask. Além disso, oferece hospedagem gratuita, que é adequada para projetos em estágios iniciais ou com tráfego moderado, como é o caso do seu painel administrativo.

3. **HTML & CSS**:
   - *O que são*: São as linguagens padrão para criar e estilizar páginas web.
   - *Por que foram usados*: HTML foi usado para estruturar o conteúdo da página e criar os formulários. CSS foi usado para dar estilo e tornar a interface amigável e atraente.

Esperamos que essa breve explicação tenha dado a você uma ideia das tecnologias que estão por trás do seu painel e o motivo de suas escolhas. Elas foram escolhidas pensando em eficiência, facilidade de uso e estabilidade.

Allan, espero que este manual tenha sido útil. Se tiver alguma dúvida ou se algo não estiver claro, por favor, peça ajuda! Estamos aqui para garantir que você possa usar este Painel Administrativo com confiança e eficiência.

