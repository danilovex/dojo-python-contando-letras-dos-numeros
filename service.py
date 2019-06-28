# def soma(x, y):
#     return x + y

string_ate_19 = {
    1:  'um',
    2:  'dois',
    3:  'tres',
    4:  'quatro',
    5:  'cinco',
    6:  'seis',
    7:  'sete',
    8:  'oito',
    9:  'nove',
    10: 'dez',
    11: 'onze',
    12: 'doze',
    13: 'treze',
    14: 'quatorze',
    15: 'quinze',
    16: 'dezesseis',
    17: 'dezessete',
    18: 'dezoito',
    19: 'dezenove'
}

string_dezenas = {
    2: 'vinte',
    3: 'trinta',
    4: 'quarenta',
    5: 'cinquenta',
    6: 'sessenta',
    7: 'setenta',
    8: 'oitenta',
    9: 'noventa'
}

def quantidade_caracter(texto):
    return len(texto.replace(' ', ''))

def calcula_tamanho(num):
    saida = 0
    for i in range(1, num + 1):
        saida += quantidade_caracter(retorna_string_numero(i))
    return saida

def retorna_string_numero(num):
    if num < 20:
        return string_ate_19[num] 
    if num >= 20:
        unidade = num % 10
        dezena = num // 10
        if unidade == 0:
            return string_dezenas[dezena]
        else:
            return string_dezenas[dezena] + "e" + string_ate_19[unidade]
    
    return string_dezenas[2]
