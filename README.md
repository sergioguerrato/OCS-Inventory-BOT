# OCS-Inventory-BOT

Contextualizando, na minha empresa utilizamos um sistema de inventário de computadores open code cahamado OCS Inventory. Ele trás divesas informações do computador como Nome, IP, MAC, Fabricante, Versão do SO entre várias outras, tal como a última vez que aquela máquina foi vista na rede.
Como temos que gerenciar 12 empresas, totalizando hoje mais de 450 computadores. A ideia do projeto foi criar um bot que identifique computadores que estiverem mais de 30 dias sem aparecer na rede e automaticamente mande um email para nosso sistema de chamados, informando que o computador está desaparecido, bem como o nome do computadore, a loja, o modelo, o último ip e mais algumas outras informações daquela máquina. Visando facilitar a identificação desses computadores.

**OBS: As informações de email, senha, servidor e tabela de export.csv tiveram seus dados alterados para dados genéricos para proteger a integridade da empresa.**


--------------------

-- Instructions --

install node.js

install python


exec on cmd:

npm i puppeteer

npm install dotenv --save

--------------------
