# Cadastro Bovino em Django

Aplicação web em Django para cadastro de animais bovinos e controle de vacinas.

## Como executar

1. Instale as dependências:
   ```bash
   pip install django
   ```
2. Crie o banco de dados e execute o servidor de desenvolvimento:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

A aplicação permite cadastrar animais com sexo, idade, data de nascimento, número do brinco e número do brinco da mãe. Cada animal pode ter múltiplas vacinas associadas com nome, data de aplicação e, opcionalmente, uma segunda dose com data correspondente.

Os registros de animais podem ser consultados, editados e removidos através da interface web.
