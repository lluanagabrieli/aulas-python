<!-- Criando um aplicativo -->
1) Navegar ate a pasta onde desejo armazenar o app
2) Dar o comando python manage.py startapp <nome-do-app>
3) Mapeando o arquivo models.py com o banco de dados (na pasta principal que guarda o app): python manage.py inspectdb > <nome-do-app>.models.py
4) Copiar os dados do <nome-app>.models.py para o models.py do app
5) Testar a conexão com o comando pasta-principal> python manage.py shell
6) Depois from <nome-app>.models import Customer