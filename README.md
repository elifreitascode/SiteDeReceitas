# Site de Receitas

Site sendo desenvolvido em Python, utilizando Django Framework. O site está sendo desenvolvido e basicamente a ideia dele, é ser um site de receitas, aonde o qualquer 
pessoa vai poder cadastrar a sua receita, colocar o nome dela como autor, colocar o tempo de preparo e adicionar a descrição completa da receita. A data em que a pessoa
cadastrar a receita, vai ser gerada automaticamente quando a pessoa subir a receita (usei o "DateTimeField" do Models do Django). Para a receita subir pra página o 
usuário vai ter que preencher um formulário. E todas as informações, vão ser exibidas dentro de um card de receita; pra fazer isso eu utlizei um vetor, que vai 
percorrer um objeto com todas essas informações, ele vai percorrer cada índice e vai exibi-los no card.

Após o preenchimento de tudo, as receitas vão ser exibidas no "home" da página. Conforme as pessoas vão cadastrando as receitas, os cards vão se ajustando na página. Fiz
alguns "Blocks" e alguns "include" pra otimizar tempo e evitar reescrever os mesmos códigos. Dentro da pasta templates, que está no app do projeto, tem outra pasta chamada
"partials", dentro dela tem os arquivos HTML, que vou utilizar o "include" no outro arquivo HTML, que está dentro do "base_templates",ou seja, nele está a base da minha
página.

As alterações que faço no "Models" do Django e faço as migrações, consigo ter acesso no "admin" do Django. É lá que administro o site, podendo excluir autores ou receitas
cadastradas. 

Utilizei HTML (Linguagem de marcação) e CSS (Estilização). Foram feitas todas configurações (STATIC_ROOT e STATIC_URL) do arquivos estáticos, no "settings.py" do Django
e também as configurações dos templates (BASE_DIR).

Projeto está sendo desenvolvido, ainda não utilizei JavaScript e SQL, mas vou utilizar.

Só darei o deploy do site, se o cadastro e informações forem criptografadas.
