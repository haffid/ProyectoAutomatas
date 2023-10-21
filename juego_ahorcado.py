import random

def dibujar_ahorcado(intentos):
    # Aquí puedes definir los dibujos del ahorcado en cada etapa
    etapas = [
        '''
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
          /      |
                |
        ''',
        '''
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        ''',
        '''
           ------
           |    |
           O    |
          /|    |
                |
                |
        ''',
        '''
           ------
           |    |
           O    |
                |
                |
                |
        ''',
        '''
           ------
           |    |
                |
                |
                |
                |
        ''',
        '''
           ------
           |    |
                |
                |
                |
                |
        '''
    ]
    print(etapas[6 - intentos])

def juego_ahorcado():
    palabras = ['palabra', 'mercado', 'caballo', 'murcielago', 'sandwich', 'galleta', 'teclado',
                'telefono', 'escuela', 'cocina', 'estrella', 'almendra', 'biblioteca', 'familia',
                'elefante', 'tortuga', 'girafa', 'avestruz', 'cocodrilo', 'paraguas']
    
    palabra = random.choice(palabras)
    palabra_a_adivinar = '_' * len(palabra)
    intentos = 6  # Número máximo de intentos
    
    while intentos > 0 and '_' in palabra_a_adivinar:
        letra = input(f'Palabra actual: {palabra_a_adivinar}\nTienes {intentos} intentos restantes. Ingresa una letra: ')
        
        if letra in palabra:
            indices = [i for i, l in enumerate(palabra) if l == letra]
            palabra_a_adivinar = list(palabra_a_adivinar)
            for indice in indices:
                palabra_a_adivinar[indice] = letra
            palabra_a_adivinar = ''.join(palabra_a_adivinar)
        else:
            intentos -= 1
            dibujar_ahorcado(intentos)
    
    if '_' not in palabra_a_adivinar:
        print(f'¡Ganaste! La palabra es: {palabra}')
    else:
        print(f'Perdiste. La palabra era: {palabra}')

if __name__ == '__main__':
    juego_ahorcado()
