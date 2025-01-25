import base64
from parte1 import HASH_FUNCTION, generate_keys
from parte2 import verify_signature, sign_message

#parsing de um documento assinado formatado em Base64. Retorna a mensagem original e a assinatura como inteiros.
def parse_signed_document(signed_document):
    try:
        print("Iniciando o parsing do documento assinado.")
        # Decodifica o documento Base64
        decoded_data = base64.b64decode(signed_document)
        print("Documento decodificado de Base64 com sucesso.")
        
        # Divide a mensagem e a assinatura
        message_length = int.from_bytes(decoded_data[:4], 'big')
        print(f"Comprimento da mensagem extraído: {message_length} bytes.")
        
        message = decoded_data[4:4 + message_length].decode('utf-8')
        print(f"Mensagem extraída: {message}")
        
        signature = int.from_bytes(decoded_data[4 + message_length:], 'big')
        print(f"Assinatura extraída: {signature}")

        return message, signature
    except Exception as e:
        raise ValueError(f"Erro ao fazer o parsing do documento assinado: {e}")

# Verifica a validade de um documento assinado. Retorna um booleano e a mensagem original.
def verify_signed_document(signed_document, public_key):
    try:
        print("Iniciando a verificação do documento assinado...")
        # Parsing do documento assinado
        message, signature = parse_signed_document(signed_document)

        # Verifica a assinatura
        print("Verificando a assinatura...")
        is_valid = verify_signature(message, signature, public_key)
        print("Verificação da assinatura concluída.")
        return is_valid, message
    except ValueError as e:
        return False, str(e)

if __name__ == "__main__":

    print("Gerando chaves RSA...")
    keys = generate_keys(key_size=1024)
    print("Chaves geradas com sucesso.")

    # Mensagem para teste
    original_message = "Teste de assinatura e verificação."
    print(f"Mensagem original para teste: {original_message}")

    print("Gerando a assinatura da mensagem...")
    signature = sign_message(original_message, keys['private_key'])
    print(f"Assinatura gerada: {signature}")

    print("Formatando o documento assinado em Base64...")
    message_bytes = original_message.encode('utf-8')
    message_length_bytes = len(message_bytes).to_bytes(4, 'big')
    signature_bytes = signature.to_bytes((keys['public_key'][1].bit_length() + 7) // 8, 'big')

    signed_document = base64.b64encode(message_length_bytes + message_bytes + signature_bytes).decode('utf-8')
    print(f"Documento assinado formatado: {signed_document}")

    # Verifica o documento assinado
    is_valid, result = verify_signed_document(signed_document, keys['public_key'])

    if is_valid:
        print(f"A assinatura é válida. Mensagem original: {result}")
    else:
        print(f"A assinatura é inválida. Erro: {result}")
