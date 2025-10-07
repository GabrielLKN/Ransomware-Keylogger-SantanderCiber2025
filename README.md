# 2 desafio de projeto do Bootcamp Santander Cibersegurança 2025
<br>
O desafio consiste em criar dois malwares, sendo eles um ransomware e um spyware (keylogger)<br>
<br>
- Ransomware:<br>
<br>
- Bibliotecas usadas:<br>
Fernet: garante criptografia simétrica (usa uma única chave para criptografar/descriptografar dados)<br>
OS: tem a função de navegar pelas pastas do sistema operacional<br>
- Funções:<br>
Gen_key:<br>
Gera uma chave para criptografar os dados e salva ela no arquivo "crypto.key"<br>
Load_key:<br>
Carrega a chave de criptografia<br>
Encrypt_file:<br>
Abre o arquivo escolhido, faz a leitura dos dados, criptografa eles usando a chave e sobrescreve o arquivo com os dados criptografados<br>
Search_files:<br>
Encontra os arquivos para criptografar mas sem que o script e a chave seja criptografada<br>
Rescue_msg:<br>
Cria uma mensagem de resgaste para a vítima 
Main:<br>
Função principal, tem o objetivo de executar tudo na sequência correta e por fim gera uma mensagem no terminal para confirmar que o script funcionou corretamente<br>
<br>
- Keylogger.pyw:<br>
<br>
- Bibliotecas usadas:<br>
Pynput: Usada para monitorar o teclado em tempo real, toda vez que uma tecla for pressionada ela chama uma função do código<br>
Smtplib: usado para fazer o envio do log por email
Mimetext: formata o conteúdo como mensagem de texto
Timer: permite o agendamento dos envios de log
<br>
- Conjunto ignore: lista de teclas ignoradas que não são necessárias para o log, tem o objetivo de deixar o log menos poluído e mais legível<br>
<br>
- Função on_press:<br>
Bloco try:<br>
Captura as teclas pressionadas e envia para um arquivo chamado "log.txt"<br>
Bloco except:<br>
Caso a tecla não seja considerada um caracter (backspace, espaço, enter, tab e esc) elas serão convertidas em seus respectivos comandos para facilitar a leitura do log (exemplo: espaço = " ")<br>
no caso de ser uma tecla desconhecida, ela será logada entre colchetes<br>
<br>
- Keylogger_email.pyw:<br>
<br>
-Variáveis:<br>
sEmail: email de origem<br>
dEmail: email de destino<br>
passEmail: senha de aplicativo<br>
<br>
-Função send_email: responsável por enviar o email formatado a cada 60 segundos<br>
(A função on_press tem o mesmo objetivo que a do arquivo keylogger.pyw)<br>
<br>
- Formas de se prevenir contra esses tipos de ataques:<br>
Uso de antívirus modernos, firewalls bem configurados, SIEM (monitorar comportamento de aplicativos e buscar por vulnerabilidades), políticas de segurança e instruções aos usuários.
