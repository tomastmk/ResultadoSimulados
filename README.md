# certificate-generator
Um programa simples para automatizar o envio do resultado de simulados des alunes.

## Dependências
- PyPDF2 `pip install PyPDF2`

## Uso
```
usage: enviar_resultados.py

```

### Arquivos especiais
O programa depende de alguns arquivos especiais
- O módulo `sendmail.py` contém as funções responsáveis por enviar os emails
- O módulo `converter.py` contém as funções responsáveis por dividir o pdf e nomear cada página do ID de alune
- O módulo `progress.py` contém as funções responsáveis por mostrar o progresso do programa
- O arquivo lista.csv contém id, nome e email des alunes
```
id,nome,email
12,Paulo Hortas,paulohortas@gmail.com
```
- O arquivo `relatorio.pdf` é o arquivo csv que contém os resultados do simulado, sendo sua primeira página o gabarito:

### Output
O programa vai gerar um pdf para cada alune em `lista.csv`, salvá-lo em PDF na pasta `files\\save` e enviá-lo ao corresponde email. 
