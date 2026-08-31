# 🥗 Sistema Gerenciador Nutricional

Um sistema completo para cálculo de IMC, avaliação nutricional e recomendações de saúde baseadas em tabelas da OMS (Organização Mundial da Saúde).

## ✨ Funcionalidades

- 📊 **Cálculo de IMC** - Com classificação segundo tabelas OMS
- 💧 **Ingestão de Água** - Recomendação personalizada por peso
- 🔥 **TMB (Taxa Metabólica Basal)** - Usando equação Mifflin-St Jeor
- 📋 **Tabela de Referência** - Padrão OMS com níveis de risco
- 💾 **Histórico** - Registro de todas as avaliações
- ⚠️ **Alertas de Saúde** - Baseados em risco nutricional

## 🚀 Como Usar

### Executar o programa:

```bash
python sistema_nutricional.py
```

### Menu Principal:

```
=== GERENCIADOR NUTRICIONAL & IMC ===
1. Cadastrar Nova Avaliação
2. Ver Tabela de Referência do IMC
3. Ver Histórico de Avaliações
4. Sair
```

## 📝 Exemplo de Uso

1. Escolha a opção **1** para cadastrar
2. Insira os dados:
   - Nome
   - Idade
   - Sexo (M/F)
   - Peso (kg)
   - Altura (m)

3. Receba o relatório com:
   - IMC Calculado
   - Diagnóstico
   - Recomendações de água
   - Gasto calórico basal

## 📊 Classificações IMC (OMS)

| Faixa de IMC | Classificação | Risco |
|---|---|---|
| < 18.5 | Abaixo do peso | Baixo (Risco nutrição) |
| 18.5 - 24.9 | Peso normal | Eutrófico (Ideal) |
| 25.0 - 29.9 | Sobrepeso | Aumentado |
| 30.0 - 34.9 | Obesidade Grau I | Moderado |
| 35.0 - 39.9 | Obesidade Grau II | Grave |
| ≥ 40.0 | Obesidade Grau III | Muito Grave |

## 💻 Requisitos

- Python 3.6 ou superior

## 📄 Licença

Livre para uso

---

**Desenvolvido com ❤️ para saúde e nutrição**
