# API de Apresentação Django

A API de Apresentação para esta prova de conceito foi desenvolvida utilizando o framework Django, com o propósito de servir como um CMS para a geração de manifestos de imagens. A escolha do Django se deu por sua facilidade de implementação e como Django não apenas simplifica a criação de APIs, mas também fornece, de forma automática, uma interface administrativa para controle de conteúdo, além de sistemas de autenticação e autorização, o que facilita o gerencimento.

Nessa implementação temos primáriamente três endpoits principais:

- `/`: Interface com o Mirador integrado aos manifestos.
- `/manifest/<id>`: Endpoint para acessar o manifesto.
- `/admin`: Interface administrativa do Django, onde é possível gerenciar os manifestos e estruturas.
