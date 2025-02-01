# Implementação de Assinatura Digital com RSA e OAEP #
Este projeto implementa um sistema de assinatura digital baseado no algoritmo RSA com padding OAEP, garantindo autenticidade, integridade e segurança das mensagens. Ele permite a geração de chaves, assinatura e verificação de assinaturas digitais utilizando funções hash SHA-3.

## Funcionalidades
✅ Geração de chaves RSA

✅ Assinatura digital de mensagens

✅ Verificação da assinatura digital

✅ Uso de OAEP para maior segurança

✅ Utilização de SHA3-256 para garantir integridade

## Estrutura do Projeto
```plaintext
.
├── .idea/                  
├── documento.txt           
├── geradorVerificador.py  
├── parte1.py              
├── parte2.py               
├── parte3.py               
├── Slides.pdf
├── Relatório.pdf

```
## Descrição dos Arquivos

```geradorVerificador.py``` → Arquivo principal que integra todas as funções e executa o fluxo do programa.

```parte1.py``` → Contém as funções de geração de chaves, encriptação, decriptação e hash SHA-3.

```parte2.py``` → Responsável por assinar mensagens (sign_message) e verificar assinaturas (verify_signature).

```parte3.py``` → Implementa parsing e verificação de documentos assinados com as funções parse_signed_document e verify_signed_document.

```documento.txt``` → Contém a mensagem que será assinada digitalmente.

```Slides.pdf``` → Apresentação do projeto

```Relatório.pdf``` → Documento detalhado com explicação do projeto

## Como Executar o Projeto

1. Clonar o Repositório
```bash 
git clone https://github.com/GioLeiren/Gerador-Verificador-de-Assinaturas.git
cd Gerador-Verificador-de-Assinaturas
```
2. Executar o Script Principal
```bash 
python geradorVerificador.py
```

## Funcionamento
1. Geração das chaves RSA: O sistema gera um par de chaves (pública e privada).
2. Leitura da mensagem a partir do arquivo: A mensagem é carregada do ```documento.txt```.
3. Assinatura Digital: A mensagem é convertida em um hash SHA-3 e assinada com RSA.
4. Verificação da Assinatura: O documento assinado é verificado utilizando a chave pública RSA.
5. Validação da Integridade: O programa confirma se a assinatura corresponde à mensagem original.
