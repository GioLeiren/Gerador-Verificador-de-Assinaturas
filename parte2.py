from parte1 import generate_keys, encrypt, decrypt, HASH_FUNCTION


def sign_message(message, private_key):
    # Calcula o hash da mensagem
    hash_msg = HASH_FUNCTION(message.encode('utf-8'))

    # Cifra o hash com a chave privada
    signature = encrypt(hash_msg, private_key)

    return signature


def verify_signature(message, signature, public_key):
    # Calcula o hash da mensagem
    hash_msg = HASH_FUNCTION(message.encode('utf-8'))
    hash_int_original = int.from_bytes(hash_msg, 'big')

    # Decifra a assinatura usando a chave pública
    hash_signed = decrypt(signature, public_key)
    hash_int_signed = int.from_bytes(hash_signed, 'big')

    # Verifica se o hash calculado é igual ao hash da assinatura
    return hash_int_original == hash_int_signed


def main():
    # Gera as chaves
    print("Gerando chaves RSA...")
    keys = generate_keys(key_size=1024)
    print("Chaves geradas:", keys)

    # Mensagem de teste
    message = "Esta é uma mensagem importante."
    print(f"Mensagem original: {message}")

    # Assinatura da mensagem
    signature = sign_message(message, keys['private_key'])
    print(f"Assinatura gerada (hex): {hex(signature)}")

    # Verificação da assinatura
    is_valid = verify_signature(message, signature, keys['public_key'])
    print(f"A assinatura é válida? {'Sim' if is_valid else 'Não'}")

    # Teste de falha: altera a mensagem
    altered_message = "Esta é uma mensagem alterada."
    is_valid_altered = verify_signature(altered_message, signature, keys['public_key'])
    print(f"A assinatura é válida para a mensagem alterada? {'Sim' if is_valid_altered else 'Não'}")


if __name__ == "__main__":
    main()
