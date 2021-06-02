
#Introdução

## Apresentação

Boa tarde / dia, o meu nome é Nuno Morais, nesta apresentação vou apresentar uma proposta de solução descentralizada para a monitorização e gestão de recursos presentes em dispositivos da Edge.

Vou começar por introduzir o contexto e motivação e explicar o problema que se pretende resolver, depois falo de alguns trabalhos relacionados, e explico a solução proposta.

## Contexto e Motivação

A computação na Cloud é atualmente o paradigma mais popular para o desenvolvimento e gestão de serviços. Em poucas palavras, a computação na cloud é o fornecimento de serviços informáticos, incluindo servidores, armazenamento, bases de dados, rede, software, análises e inteligência, através da Internet. 

Este paradigma proporciona:
* a ilusão de capacidade de computação ilimitada,
* redução de custos tanto para clientes como para provedores de serviços
* revolucionou o processo de desenvolvimento e gestão de aplicações.

No entanto, o modelo centralizado proposto por este paradigma diverge do modelo de aplicações como as aplicações para a Internet Das Coisas (IoT) e para aplicações móveis, dado que a produção e requisição dos dados é predominantemente feita por dispositivos que estão fora dos centros de dados. 

Desta divergência surgem vários problemas:

	* Custos de infrastrutura adicionais
	* Aumento da latência para utilizadores e provedores de serviços
	* Questões sobre a privacidade e segurança dos dados

Para mitigar as limitações previamente mencionadas, surgiu um novo paradigma: Edge Computing. Este paradigma propõe executar computações, e potencialmente armazenar dados, em dispositivos situados entre a origem dos dados e os centros de dados. Isto tem vantagens como: 

 * melhorar a qualidade de serviço de aplicações mobile / interativas. 
 * Possibilitar a criação de serviços que seriam impossíveis de criar apenas com base na computação na Cloud, por exemplo, o Boeing 787 produz perto de 5 GB de dados por minuto, o que seria impossível de transportar e processar na Cloud para efeitos de, por exemplo, condução autónoma. 

No entanto, à medida que nos distanciamos dos centros de dados, a capacidade de computação e armazenamento dos dispositivos tende a ser limitada, e as suas ligações tendem a ser instàveis.
Para mitigar esta falta de capacidade, surge a necessidade de partilhar recursos entre dispositivos de modo a habilitar o sistema a efetuar computações que outrora seriam impossíveis de efetuar apenas com um único dispositivo destes.

## Problema

O estudo do estado da arte revelou que as soluções existentes para a gestão e partilha de recursos como o Mesos, Yarn e Omega são normalmente especializadas para ambientes de computação na Cloud, onde os dispositivos possuem grandes capacidades de processamento e armazenamento, e estão equipados com ligações estáveis, que facilitam a gestão dos seus recursos. 

Estas soluções geralmente empregam um único componente centralizado, com conhecimento completo do estado do sistema, que desempenha as seguintes funções: (1) gere toda informação relativa ao funcionamento dos dispositivos e das computações em curso; (2) gere as necessidades de recursos que surgem dos clientes; (3) faz a gestão dos recursos de modo a garantir as necessidades dos clientes e (4) garantir que o sistema se mantém equilibrado, mesmo na presença de cargas de trabalho dinâmicas. No entanto, no contexto de ambientes heterogéneos, dinâmicos, e de larga escala como os contemplados em Edge Computing, efetuar a gestão dos recursos num componente centralizado é um obstáculo para o desempenho do sistema, e também é um ponto único de falha.

Dado isto, é importante que os dispositivos integrem um sistema que faça a gestão e monitorização de recursos descentralizadamente. Esta solução de controlo, composta por multiplos componentes potencialmente organizados de uma maneira hierárquica, terá de federar todos os dispositivos e armazenar informação relativa tanto ao estado dos dispositivos, como também das computações que estes estão a desempenhar. Esta informação, por sua vez, suportará a tomada de decisões baseadas em conhecimento parcial do sistema que balanceiam a carga e adaptam-se a alterações no sistema.

# Trabalho relacionado

Agora vamos falar do estudo do trabalho relacionado objetivos estabelecidos, por questões de limitação de tempo, vou-me cingir
a falar de 3 soluções em específico.

A primeira é o Astrolabe.

## Astrolabe

O Astrolabe é uma solução que estabelece uma solução de gestão de informação descentralizada. Para o fazer, o astrolabe estabelece uma estrutura hierárquica composta por zonas.

As zonas são identificadas pelo seu nome, que é composto pelo seu próprio identificador (único à zona a que está contida) em conjunto com os identificadores de todas as zonas que estão acima na hierarquia (e.g. /zone1/subzone1/ ). 

A cada zona está associada uma Management Information Base, que é composta por diversos atributos gerados através de funções de agregação, que são compostas por código SQL e instaladas pelos utilizadores. Em cada zona, um ou mais membros são eleitos para propagar a MIB relativa a essa zona, 

## Mesos

## ENORM

# Solução proposta


A solução proposta consiste numa infrastrura que permite a gestão e monitorização descentralizada de recursos, esta será especialmente desenvolvida a pensar nas necessidades de aplicações que sejam edge-enabled. A infrastrutura terá de ser seja escalável e de se adaptar à heterogeneidade dos dispositivos que o compõem. Esta tem como objetivo: 

	* Monitorizar o estado de aplicações a serem executadas
	* Providenciar operações para a operação de aplicações edge-enabled
	* Encontrar conjuntos de dispositivos que sejam adequados para executar certas computações
	* Encontrar dispositivos que estejam perto e permitam a delegação de computações

## Modelo do sistema

Agora estabelecemos o modelo do sistema da solução, composto por:

	* dispositivos estáveis, que são compostos por dispositivos desde centros de dados na cloud e edge até servidores privados e portáteis.

	* dispositivos instáveis, são compostos por tablets, telemóveis e sensores / atuadores, estes têm connexoes sem fios, que levantam um conjunto de questões relativas á sua comunicação e mobilidade que não são o foco desta dissertação, no entanto, estes dispositivos poderão participar no sistema através dos dispositivos estáveis (e.g. gateway) 

	* aplicações edge-enabled, são aplicações compostas por componentes que podem ser decompostos em múltiplos componentes independentes, estes podem estar contidos dentro de um só dispositivo, e funcionar como uma aplicação centralizada, ou ter os componentes espalhados por dispositivos no sistema. Por consequência, definimos 3 operações para estas: replicar, migrar e decomissionar. Replicar significa criar uma copia de um componente noutro dispositivo, migrar significa transferir a execução de um componente (ou uma porção dele) para outro dispositivo, e decomissionar significa transicionar a aplicação de ativa para inativa.

Durante o desenvolvimento desta solução assumimos 2 coisas: diferenças de domínio administrativo entre os dispositivos não afetam a qualidade das ligações, e não existe mais que 1 falha simultânea ao nível dos centros de dados.

## Solução

Esta solução estará dividida em 4 mecanismos que são co-dependentes:

	* Controlo da topologia
	* Procura e descoberta de recursos
	* Monitorização de recursos
	* Gestão de recursos

### Gestão da topologia

Primeiro temos o mecanismo de gestão da topologia, este mecanismo consiste num algoritmo cujo objetivo é estabelecer uma overlay network com uma topologia hierárquica, inspirada no astrolabe, que cumpre os seguintes 3 requisitos:

	* Estabelecer uma topologia hierarquica baseada nas capacidades dos dispositivos
	* Garantir a conectividade da topologia resultante
	* Detetar falhas ao nível do dispositivo

### Monitorização de recursos

De seguida temos o mecanismo de monitorização de recursos, o objetivo deste mecanismo é utilizar a topologia estabelecida para:

* colecionar metricas sobre o funcionamento dos componentes que estão a executar 
* emitir alertas consoante a deteção de anomalias no funcionamento, ou da deteção de mau desempenho nos componentes.

### Localização e descoberta de recursos

Utilizará a estrutura da topologia para proporcionar estratégias de procura e descoberta de recursos para serem utilizados pela camada de gestão de recursos

### Gestão de recursos

Relativamente à gestão dos recursos, o foco deste trabalho não é de criar uma solução que coloque os componentes aplicacionais nos dispositivos ideais, a nossa camada de gestão de recursos procura acomodar uma camada adicional do sistema que trata de descobrir o melhor escalonamento possível para os componentes. Visto isto, a camada de gestão de recursos proposta faz uma gestão muito limitada dos recursos do sistema, nomeadamente:

* Lida com as falhas tanto ao nível dos dispositivos, como dos componentes aplicacionais, e dos alertas emitidos pelo mecanismo de monitorização
* Providencia mecanismos para encontrar dispositivos (através do mecanismo de descoberta e localização)
* Providencia a habilidade de hospedar componentes aplicacionais nos dispositivos que compõem o sistema
* Providencia um mecanismo de subscrição que permite a esta camada adicional de escalonamento ser notificada de mudanças feitas para lidar com aletas e falhas.

## Avaliação

A avaliação desta solução será feita através de testes experimentais. Os dispositivos que vão compor estes testes vão ser dispositivos na cloud, no cluster grid5000 e nos cerca de 20 raspberry pis que temos disponíveis no departamento de informática.

Para avaliar a nossa solução, iremos implementar 2 versões de sistemas de monitorização que são representativos de sistemas que são empregues atualmente, a primeira é uma solução centralizada, em que a gestão e monitorização de recursos é feita num único componente no sistema. A segunda será representativa de um sistema que não é hierarquico, e todos os dispositivos no sistema têm responsabilidades semelhantes. 

Para comparar estas soluções, iremos colecionar 2 tipos de métricas:

	* metricas do sistema, como a utilização de recursos por dispositivo, e o número de mensagens enviadas para manter o funcionamento do sistema
	* information freshness, que representa o quão recente é a informação obtida VS a informação atual
	* precisão da informação, que representa a diferença entre os dados obtidos e o estado real do dispositivo / componentes lá a correr


## Calendarização

cenas






