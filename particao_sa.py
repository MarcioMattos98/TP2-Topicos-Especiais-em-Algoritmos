import random
import math

def calcular_valor_solucao(numeros, solucao):
    
    soma_subconjunto_0 = 0
    soma_subconjunto_1 = 0

    for i, pertence_ao_conjunto_1 in enumerate(solucao):
        if pertence_ao_conjunto_1 == 0:
            soma_subconjunto_0 += numeros[i]
        else:
            soma_subconjunto_1 += numeros[i]

    return abs(soma_subconjunto_0 - soma_subconjunto_1)


def simulated_annealing(numeros, temp_inicial, taxa_resfriamento, num_iteracoes):
   
    solucao_atual = [random.choice([0, 1]) for _ in range(len(numeros))]
    valor_atual = calcular_valor_solucao(numeros, solucao_atual)

    # Guarda a melhor solução encontrada até o momento
    melhor_solucao = solucao_atual[:]
    melhor_valor = valor_atual

    temperatura = temp_inicial

  
    for i in range(num_iteracoes):
        # Gera uma solução vizinha trocando um elemento de conjunto
        vizinho = solucao_atual[:]
        indice_a_trocar = random.randint(0, len(numeros) - 1)
        vizinho[indice_a_trocar] = 1 - vizinho[indice_a_trocar] # Troca 0 por 1 ou 1 por 0

        # Calcula o valor da solução vizinha
        valor_vizinho = calcular_valor_solucao(numeros, vizinho)

        # Calcula a diferença de "energia" (custo)
        delta_valor = valor_vizinho - valor_atual


        if delta_valor < 0:
            # Se o vizinho é melhor, aceita-o
            solucao_atual = vizinho[:]
            valor_atual = valor_vizinho 
        else:
            # Se o vizinho é pior, aceita-o com uma certa probabilidade
            probabilidade_aceitacao = math.exp(-delta_valor / temperatura)
            if random.random() < probabilidade_aceitacao:
                solucao_atual = vizinho[:]
                valor_atual = valor_vizinho

        # Atualiza a melhor solução encontrada até agora
        if valor_atual < melhor_valor:
            melhor_solucao = solucao_atual[:]
            melhor_valor = valor_atual
        
        
        temperatura *= taxa_resfriamento

    return melhor_solucao, melhor_valor



if __name__ == "__main__":
    
    dados_teste = [112, 45, 88, 23, 9, 150, 67, 89, 42, 101, 18, 77, 95, 33, 61, 29]
    print(f"Conjunto de números de entrada: {dados_teste}")
    print(f"Soma total: {sum(dados_teste)}\n")

    # Parâmetros do Simulated Annealing
    TEMP_INICIAL = 1000.0
    TAXA_RESFRIAMENTO = 0.995
    NUM_ITERACOES = 20000

    # Executa o algoritmo
    melhor_solucao_encontrada, melhor_diferenca = simulated_annealing(
        numeros=dados_teste,
        temp_inicial=TEMP_INICIAL,
        taxa_resfriamento=TAXA_RESFRIAMENTO,
        num_iteracoes=NUM_ITERACOES
    )


    print("--- Resultados ---")
    print(f"A melhor solução encontrada foi: {melhor_solucao_encontrada}")
    print(f"A menor diferença (valor da solução) foi: {melhor_diferenca}")

    # Exibe os dois subconjuntos resultantes
    subconjunto_0 = [dados_teste[i] for i, x in enumerate(melhor_solucao_encontrada) if x == 0]
    subconjunto_1 = [dados_teste[i] for i, x in enumerate(melhor_solucao_encontrada) if x == 1]

    print("\nPartição resultante:")
    print(f"Subconjunto 0: {subconjunto_0} -> Soma = {sum(subconjunto_0)}")
    print(f"Subconjunto 1: {subconjunto_1} -> Soma = {sum(subconjunto_1)}")
