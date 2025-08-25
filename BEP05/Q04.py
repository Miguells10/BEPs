'''4. Crie uma variável que vai armazenar a palavra secreta “Programação”. Em
seguida, utilize uma estrutura de repetição que deve parar de solicitar uma palavra
apenas quando o usuário acertar a palavra secreta.'''

palavra_secreta = "Programação"
while True:
    tentativa = input("Digite a palavra secreta: ")
    if tentativa == palavra_secreta:
        print("Parabéns! Você acertou a palavra secreta.")
        break
    else:
        print("Palavra incorreta. Tente novamente.")
print("Fim do jogo.")