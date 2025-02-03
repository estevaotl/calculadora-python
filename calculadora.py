
def calcular_porcentagem(valor, percentual):
    return (valor * percentual) / 100

def calcular_expressao(expressao):
    try:
        return eval(expressao)
    except Exception as e:
        return f"Erro: {e}"