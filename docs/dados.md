# Intrução de modelo de dados


## Base de dados (.csv)
 para ser possível automatizar seus certificados é necessário criar um arquivo .csv(Comma-separated values) com os dados das pessoas que precisarão ser substituidos no seu respectivo modelo.


 Exemplo:


data.csv:
 ```csv

    name,cpf,nascimento
    carlos,12345678910,10/06/1998
    maria,234567,16/06/1998

 ```

## Arquivo base(.pptx)

no seu modelo, defina aonde devem ser colocado cada atributo de cada coluna da sua base de dados utilizando a sintaxe  **#-atributo-#**. Isso fara com que cada coluna seja substituido pelo seu respectivo valor, para cada linha do seu CSV , será criado uma cópia do seu modelo , fazendo a substituição dos dados conforme indicavo na sua base.


Caso na sua base tenha a coluna **name** você utiliza a sintaxe **#-name-#** para realizar a substituição dos valores.