import datetime


# --- TABELAS DE REFERÊNCIA (OMS) ---
def obter_classificacao_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso", "Risco de desnutrição e deficiências de micronutrientes."
    elif 18.5 <= imc < 25.0:
        return "Peso normal (Eutrofia)", "Menor risco para complicações de saúde."
    elif 25.0 <= imc < 30.0:
        return "Sobrepeso (Pré-obesidade)", "Risco moderado para diabetes tipo 2 e doenças cardiovasculares."
    elif 30.0 <= imc < 35.0:
        return "Obesidade Grau I", "Risco elevado para hipertensão, diabetes e colesterol alto."
    elif 35.0 <= imc < 40.0:
        return "Obesidade Grau II (Severa)", "Risco muito elevado para múltiplas comorbidades."
    else:
        return "Obesidade Grau III (Mórbida)", "Risco extremamente elevado e iminente à saúde."


def exibir_tabela_referencia():
    print("\n" + "="*60)
    print("        TABELA OFICIAL DE CLASSIFICAÇÃO DO IMC (OMS)")
    print("="*60)
    print(f"{'Faixa de IMC':<18} | {'Classificação':<25} | {'Nível de Risco'}")
    print("-" * 60)
    print(f"{'< 18.5':<18} | {'Abaixo do peso':<25} | {'Baixo (Risco nutrição)'}")
    print(f"{'18.5 - 24.9':<18} | {'Peso normal':<25} | {'Eutrófico (Ideal)'}")
    print(f"{'25.0 - 29.9':<18} | {'Sobrepeso':<25} | {'Aumentado'}")
    print(f"{'30.0 - 34.9':<18} | {'Obesidade Grau I':<25} | {'Moderado'}")
    print(f"{'35.0 - 39.9':<18} | {'Obesidade Grau II':<25} | {'Grave'}")
    print(f"{'>= 40.0':<18} | {'Obesidade Grau III':<25} | {'Muito Grave'}")
    print("="*60 + "\n")


# --- CÁLCULOS NUTRICIONAIS ---
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def calcular_agua_diaria(peso):
    # Recomendação média de 35ml de água por kg
    return (peso * 35) / 1000


def calcular_tmb(peso, altura_cm, idade, sexo):
    # Equação de Mifflin-St Jeor (amplamente utilizada na nutrição)
    if sexo.upper() == 'M':
        return (10 * peso) + (6.25 * altura_cm) - (5 * idade) + 5
    else:
        return (10 * peso) + (6.25 * altura_cm) - (5 * idade) - 161


# --- SISTEMA PRINCIPAL ---
def sistema_nutricional():
    historico = []

    while True:
        print("\n=== GERENCIADOR NUTRICIONAL & IMC ===")
        print("1. Cadastrar Nova Avaliação")
        print("2. Ver Tabela de Referência do IMC")
        print("3. Ver Histórico de Avaliações")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")

        if opcao == '1':
            print("\n--- CADASTRO DE AVALIAÇÃO ---")
            nome = input("Nome do paciente/usuário: ")
            
            try:
                idade = int(input("Idade (anos): "))
                sexo = input("Sexo (M/F): ").strip().upper()
                peso = float(input("Peso (kg): ").replace(',', '.'))
                altura = float(input("Altura (m) [ex: 1.75]: ").replace(',', '.'))
            except ValueError:
                print("❌ Erro: Por favor, insira números válidos para peso, altura e idade.")
                continue

            # Processamento de Dados
            imc = calcular_imc(peso, altura)
            classificacao, risco = obter_classificacao_imc(imc)
            agua = calcular_agua_diaria(peso)
            tmb = calcular_tmb(peso, altura * 100, idade, sexo)
            data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

            # Salvar no Histórico
            registro = {
                "data": data_atual,
                "nome": nome,
                "imc": imc,
                "classificacao": classificacao,
                "agua": agua,
                "tmb": tmb
            }
            historico.append(registro)

            # Exibição do Relatório do Paciente
            print("\n" + "─"*45)
            print(f"📊 RELATÓRIO NUTRICIONAL - {nome.upper()}")
            print("─"*45)
            print(f"• IMC Calculado:        {imc:.2f} kg/m²")
            print(f"• Diagnóstico:          {classificacao}")
            print(f"• Alerta de Saúde:      {risco}")
            print(f"• Ingestão de Água:     ~{agua:.2f} Litros/dia")
            print(f"• Gasto Basal (TMB):    ~{tmb:.0f} kcal/dia (em repouso)")
            print("─"*45)

        elif opcao == '2':
            exibir_tabela_referencia()

        elif opcao == '3':
            if not historico:
                print("\n⚠️ Nenhum registro encontrado no histórico.")
            else:
                print("\n" + "="*65)
                print("                  HISTÓRICO DE AVALIAÇÕES")
                print("="*65)
                for i, rec in enumerate(historico, 1):
                    print(f"{i}. [{rec['data']}] {rec['nome']}")
                    print(f"   IMC: {rec['imc']:.2f} ({rec['classificacao']}) | Água: {rec['agua']:.1f}L | TMB: {rec['tmb']:.0f} kcal")
                    print("-" * 65)

        elif opcao == '4':
            print("\nEncerrando o sistema. Até mais!")
            break
        else:
            print("❌ Opção inválida! Escolha entre 1 e 4.")


if __name__ == "__main__":
    sistema_nutricional()
