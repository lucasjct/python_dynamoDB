# python_dynamoDB

AWS SDK para integrar com DynamoDB  


DynamoDB é um banco de dados NoSQL,orientado a chave e valor, oferecido pela cloud providor AWS.  

Podemos utlizar alguns SDK para integrar com este serviço, neste caso foi utilizado Python através do [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html, "Boto3").  

Para executar os scripts, é necessário configurar a [AWS CLI](https://aws.amazon.com/pt/cli/). É necessário as seguintes chaves: `aws_access_key_id` e `aws_secret_access_key`. Elas podem ser encontradas no serviço do IAM do seu usuário ou as do usuário criado com permissão unicamente para executar esse serviço. 

Após baixar a AWS CLI e ter em mãos as chaves, configurar no Shell com o seguinte comando: `aws configure`. Feito isto, podemos executar os scritps. 
