import math
import csv
import os

# =========================================
# Vetores (listas) - cada posição = 1 registro
# =========================================
culturas = []           # "CANA" ou "CAFE"
nomes_talhao = []       # identificador do talhão

# Dados geométricos (preenche de acordo com a cultura; o resto fica None)
cana_comp_m = []        # CANA: comprimento (m)
cana_larg_m = []        # CANA: largura (m)

cafe_raio_m = []        # CAFE: raio (m)

# Dados de insumos
# CANA (fertilizante)
cana_dose_kg_ha = []    # kg/ha

# CAFE (pulverização por rua)
cafe_qtd_ruas = []      # inteiro
cafe_comp_rua_m = []    # m
cafe_dose_ml_m = []     # mL por metro

# Resultados calculados (para facilitar saída e R)
area_m2 = []
area_ha = []
insumo_total = []       # CANA: kg | CAFE: litros
insumo_unidade = []     # "kg" ou "L"


# =========================================
# Funções utilitárias
# =========================================
def ler_float(msg):
    while True:
        valor = input(msg + " (ou 0 para cancelar): ").strip()

        if valor == "0":
            return None
        try:
            return float(valor.replace(",", "."))
        except ValueError:
            print("Entrada inválida. Digite um número (use ponto ou vírgula).")


def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Entrada inválida. Digite um inteiro.")


def calcula_registro(idx):
    """Recalcula área e insumo do registro idx."""
    cultura = culturas[idx]

    if cultura == "CANA":
        comp = cana_comp_m[idx]
        larg = cana_larg_m[idx]
        dose = cana_dose_kg_ha[idx]

        a_m2 = comp * larg
        a_ha = a_m2 / 10_000.0

        total_kg = a_ha * dose

        area_m2[idx] = a_m2
        area_ha[idx] = a_ha
        insumo_total[idx] = total_kg
        insumo_unidade[idx] = "kg"

    elif cultura == "CAFE":
        r = cafe_raio_m[idx]
        ruas = cafe_qtd_ruas[idx]
        comp_rua = cafe_comp_rua_m[idx]
        dose_ml = cafe_dose_ml_m[idx]

        a_m2 = math.pi * (r ** 2)
        a_ha = a_m2 / 10_000.0

        total_ml = ruas * comp_rua * dose_ml
        total_l = total_ml / 1_000_000.0

        area_m2[idx] = a_m2
        area_ha[idx] = a_ha
        insumo_total[idx] = total_l
        insumo_unidade[idx] = "L"

    else:
        print("Cultura desconhecida. Registro não recalculado.")


def inserir_registro():
    print("\n== Entrada de dados ==")
    print("1) CANA-DE-AÇÚCAR (retângulo + fertilizante kg/ha)")
    print("2) CAFÉ (círculo + pulverização por rua mL/m)")
    print("0) Voltar ao menu")

    op = input("Escolha a cultura (1/2/0): ").strip()

    if op == "0":
        print("Voltando ao menu...")
        return

    nome = input("Nome do talhão (ex: T1, Área Norte, etc.): ").strip()
    if not nome:
        nome = f"T{len(culturas) + 1}"

    if op == "1":
        culturas.append("CANA")
        nomes_talhao.append(nome)

        comp = ler_float("Comprimento (m): ")
        larg = ler_float("Largura (m): ")
        dose = ler_float("Dose de fertilizante (kg/ha): ")

        cana_comp_m.append(comp)
        cana_larg_m.append(larg)
        cafe_raio_m.append(None)

        cana_dose_kg_ha.append(dose)
        cafe_qtd_ruas.append(None)
        cafe_comp_rua_m.append(None)
        cafe_dose_ml_m.append(None)

    elif op == "2":
        culturas.append("CAFE")
        nomes_talhao.append(nome)

        r = ler_float("Raio da área (m): ")
        ruas = ler_int("Quantidade de ruas: ")
        comp_rua = ler_float("Comprimento de cada rua (m): ")
        dose_ml = ler_float("Dose de pulverização (mL por metro): ")

        cana_comp_m.append(None)
        cana_larg_m.append(None)
        cafe_raio_m.append(r)

        cana_dose_kg_ha.append(None)
        cafe_qtd_ruas.append(ruas)
        cafe_comp_rua_m.append(comp_rua)
        cafe_dose_ml_m.append(dose_ml)

    else:
        print("Opção inválida.")
        return

    # reserva espaço de resultados e calcula
    area_m2.append(0.0)
    area_ha.append(0.0)
    insumo_total.append(0.0)
    insumo_unidade.append("")

    calcula_registro(len(culturas) - 1)
    print("Registro inserido e calculado com sucesso.")


def listar_registros():
    print("\n== Saída de dados (listagem) ==")
    if len(culturas) == 0:
        print("Nenhum registro cadastrado.")
        return

    for i in range(len(culturas)):
        print(f"\n[{i}] Talhão: {nomes_talhao[i]} | Cultura: {culturas[i]}")
        print(f"    Área: {area_m2[i]:.2f} m² ({area_ha[i]:.4f} ha)")
        print(f"    Insumo total: {insumo_total[i]:.4f} {insumo_unidade[i]}")

        if culturas[i] == "CANA":
            print(f"    Retângulo: {cana_comp_m[i]} m x {cana_larg_m[i]} m")
            print(f"    Dose: {cana_dose_kg_ha[i]} kg/ha")
        else:
            print(f"    Círculo: raio {cafe_raio_m[i]} m")
            print(
                f"    Ruas: {cafe_qtd_ruas[i]} | Comp/rua: {cafe_comp_rua_m[i]} m | Dose: {cafe_dose_ml_m[i]} mL/m")


def atualizar_registro():
    print("\n== Atualização de dados ==")
    if len(culturas) == 0:
        print("Nenhum registro para atualizar.")
        return

    print("Pressione ENTER para voltar ao menu")
    idx_str = input(
        "Digite o índice do registro a atualizar: ").strip()
    if idx_str == "":
        print("Voltando ao menu...")
        return
    try:
        idx = int(idx_str)
    except ValueError:
        print("Índice inválido.")
        return
    if idx < 0 or idx >= len(culturas):
        print("Índice inválido.")
        return

    cultura = culturas[idx]
    print(f"Atualizando [{idx}] {nomes_talhao[idx]} ({cultura})")

    novo_nome = input("Novo nome do talhão (enter para manter): ").strip()
    if novo_nome:
        nomes_talhao[idx] = novo_nome

    if cultura == "CANA":
        comp = ler_float("Novo comprimento (m): ")
        larg = ler_float("Nova largura (m): ")
        dose = ler_float("Nova dose (kg/ha): ")
        cana_comp_m[idx] = comp
        cana_larg_m[idx] = larg
        cana_dose_kg_ha[idx] = dose

    elif cultura == "CAFE":
        r = ler_float("Novo raio (m): ")
        ruas = ler_int("Nova quantidade de ruas: ")
        comp_rua = ler_float("Novo comprimento de cada rua (m): ")
        dose_ml = ler_float("Nova dose (mL por metro): ")
        cafe_raio_m[idx] = r
        cafe_qtd_ruas[idx] = ruas
        cafe_comp_rua_m[idx] = comp_rua
        cafe_dose_ml_m[idx] = dose_ml

    calcula_registro(idx)
    print("Registro atualizado e recalculado.")


def deletar_registro():
    print("\n== Deleção de dados ==")
    if len(culturas) == 0:
        print("Nenhum registro para deletar.")
        return

    print("Pressione ENTER para voltar ao menu")
    idx_str = input(
        "Digite o índice do registro a deletar: ").strip()
    if idx_str == "":
        print("Voltando ao menu...")
        return
    try:
        idx = int(idx_str)
    except ValueError:
        print("Índice inválido.")
        return
    if idx < 0 or idx >= len(culturas):
        print("Índice inválido.")
        return

    # remove de todas as listas (mesmo índice)
    for vetor in (
        culturas, nomes_talhao,
        cana_comp_m, cana_larg_m, cafe_raio_m,
        cana_dose_kg_ha, cafe_qtd_ruas, cafe_comp_rua_m, cafe_dose_ml_m,
        area_m2, area_ha, insumo_total, insumo_unidade
    ):
        vetor.pop(idx)

    print("Registro deletado.")


def exportar_csv():
    print("\n== Exportar CSV para análise ==")
    if len(culturas) == 0:
        print("Nada para exportar.")
        return

    print("0) Voltar ao menu")
    nome_arquivo = input(
        "Nome do arquivo (ex: dados_fazenda) ou 0 para voltar: ").strip()
    if nome_arquivo == "0":
        print("Voltando ao menu...")
        return
    if not nome_arquivo:
        nome_arquivo = "dados_fazenda.csv"

    base_dir = os.path.dirname(os.path.abspath(__file__))
    pasta_csv = os.path.join(base_dir, "..", "relatorios", "csv")

    os.makedirs(pasta_csv, exist_ok=True)

    caminho = os.path.join(pasta_csv, f"{nome_arquivo}.csv")

    with open(caminho, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow([
            "idx", "talhao", "cultura",
            "area_m2", "area_ha",
            "insumo_total", "insumo_unidade"
        ])
        for i in range(len(culturas)):
            w.writerow([
                i, nomes_talhao[i], culturas[i],
                f"{area_m2[i]:.6f}", f"{area_ha[i]:.6f}",
                f"{insumo_total[i]:.6f}", insumo_unidade[i]
            ])

    print(f"Exportado com sucesso em:\n{caminho}")


# =========================================
# Programa principal (menu + loop)
# =========================================
def main():
    while True:
        print("\n==============================")
        print(" FarmTech Solutions - Menu")
        print("==============================")
        print("1) Entrada de dados (inserir)")
        print("2) Saída de dados (listar)")
        print("3) Atualizar dados (por índice)")
        print("4) Deletar dados (por índice)")
        print("5) Exportar CSV (para análise)")
        print("0) Sair")
        op = input("Escolha: ").strip()

        if op == "1":
            inserir_registro()
        elif op == "2":
            listar_registros()
        elif op == "3":
            atualizar_registro()
        elif op == "4":
            deletar_registro()
        elif op == "5":
            exportar_csv()
        elif op == "0":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
