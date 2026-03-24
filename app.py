import csv
import json
import os
from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st


# =========================================================
# CONFIGURAÇÃO
# =========================================================
st.set_page_config(
    page_title="Mini-desafio Interativo — Loops em Java",
    page_icon="🔁",
    layout="wide"
)

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

CSV_PATH = DATA_DIR / "respostas_minidesafio.csv"
JSONL_PATH = DATA_DIR / "respostas_minidesafio.jsonl"

TEACHER_PASSWORD = st.secrets.get("app", {}).get(
    "teacher_password",
    os.getenv("TEACHER_PASSWORD", "prof123")
)

TOTAL_QUESTOES = 4


# =========================================================
# QUESTÕES
# =========================================================
QUESTOES = [
    {
        "id": "Q1",
        "titulo": "Contagem simples",
        "tipo": "radio",
        "enunciado": "Qual código imprime os números de 1 até 10 corretamente?",
        "codigo": None,
        "opcoes": [
            """for (int i = 1; i <= 10; i++) {
    System.out.println(i);
}""",
            """for (int i = 0; i < 10; i++) {
    System.out.println(i);
}""",
            """while (i <= 10) {
    System.out.println(i);
}""",
            """for (int i = 10; i >= 1; i--) {
    System.out.println(i);
}"""
        ],
        "correta": """for (int i = 1; i <= 10; i++) {
    System.out.println(i);
}""",
        "explicacao": "O laço começa em 1, vai até 10 e incrementa de 1 em 1."
    },
    {
        "id": "Q2",
        "titulo": "Contagem regressiva",
        "tipo": "radio",
        "enunciado": "Qual saída será produzida pelo código abaixo?",
        "codigo": """for (int i = 10; i >= 1; i--) {
    System.out.print(i + " ");
}""",
        "opcoes": [
            "1 2 3 4 5 6 7 8 9 10",
            "10 9 8 7 6 5 4 3 2 1",
            "10 8 6 4 2",
            "O código entra em loop infinito"
        ],
        "correta": "10 9 8 7 6 5 4 3 2 1",
        "explicacao": "O contador inicia em 10 e vai decrementando até 1."
    },
    {
        "id": "Q3",
        "titulo": "Soma de 1 até N",
        "tipo": "radio",
        "enunciado": "Se N = 5, qual será o valor final de soma?",
        "codigo": """int soma = 0;
for (int i = 1; i <= 5; i++) {
    soma = soma + i;
}
System.out.println(soma);""",
        "opcoes": ["5", "10", "15", "20"],
        "correta": "15",
        "explicacao": "1 + 2 + 3 + 4 + 5 = 15."
    },
    {
        "id": "Q4",
        "titulo": "Números pares",
        "tipo": "radio",
        "enunciado": "Qual condição mostra apenas números pares entre 1 e 20?",
        "codigo": """for (int i = 1; i <= 20; i++) {
    if ( ________ ) {
        System.out.println(i);
    }
}""",
        "opcoes": [
            "i % 2 == 0",
            "i % 2 == 1",
            "i > 2",
            "i == 20"
        ],
        "correta": "i % 2 == 0",
        "explicacao": "Números pares deixam resto 0 na divisão por 2."
    },
    {
        "id": "Q5",
        "titulo": "Validação com while",
        "tipo": "radio",
        "enunciado": "Em qual situação o while é a melhor escolha?",
        "codigo": None,
        "opcoes": [
            "Exibir exatamente 10 números",
            "Mostrar a tabuada do 7",
            "Pedir um número positivo até o usuário digitar corretamente",
            "Imprimir os números de 1 a 5"
        ],
        "correta": "Pedir um número positivo até o usuário digitar corretamente",
        "explicacao": "Use while quando a repetição depende de uma condição e a quantidade de tentativas não é fixa."
    },
    {
        "id": "Q6",
        "titulo": "Tabuada",
        "tipo": "radio",
        "enunciado": "Se o número lido for 3, qual saída representa corretamente a tabuada de 1 a 4?",
        "codigo": """int n = 3;
for (int i = 1; i <= 4; i++) {
    System.out.println(n + " x " + i + " = " + (n * i));
}""",
        "opcoes": [
            "3 x 1 = 3 / 3 x 2 = 6 / 3 x 3 = 9 / 3 x 4 = 12",
            "3 x 0 = 0 / 3 x 1 = 3 / 3 x 2 = 6 / 3 x 3 = 9",
            "1 x 3 = 3 / 2 x 3 = 6 / 3 x 3 = 9 / 4 x 3 = 12",
            "3 6 9"
        ],
        "correta": "3 x 1 = 3 / 3 x 2 = 6 / 3 x 3 = 9 / 3 x 4 = 12",
        "explicacao": "O laço percorre de 1 a 4 e imprime o produto de n por i."
    },
    {
        "id": "Q7",
        "titulo": "Soma de múltiplos",
        "tipo": "radio",
        "enunciado": "Qual código soma corretamente os múltiplos de 3 entre 1 e 10?",
        "codigo": None,
        "opcoes": [
            """int soma = 0;
for (int i = 1; i <= 10; i++) {
    if (i % 3 == 0) {
        soma += i;
    }
}""",
            """int soma = 0;
for (int i = 1; i <= 10; i++) {
    if (i % 3 == 1) {
        soma += i;
    }
}""",
            """int soma = 0;
for (int i = 3; i <= 10; i++) {
    soma = 3;
}""",
            """int soma = 0;
while (true) {
    soma++;
}"""
        ],
        "correta": """int soma = 0;
for (int i = 1; i <= 10; i++) {
    if (i % 3 == 0) {
        soma += i;
    }
}""",
        "explicacao": "Os múltiplos de 3 entre 1 e 10 são 3, 6 e 9."
    },
    {
        "id": "Q8",
        "titulo": "Contador de positivos",
        "tipo": "radio",
        "enunciado": "No problema 'ler números até digitar 0', o que deve encerrar o loop?",
        "codigo": None,
        "opcoes": [
            "Quando o número for negativo",
            "Quando o número for maior que 0",
            "Quando o número digitado for 0",
            "Quando o contador chegar em 10"
        ],
        "correta": "Quando o número digitado for 0",
        "explicacao": "O valor 0 funciona como sentinela para encerrar a repetição."
    },
    {
        "id": "Q9",
        "titulo": "Desafio — Número secreto",
        "tipo": "texto_livre",
        "enunciado": "Escreva um algoritmo ou código Java que peça tentativas ao usuário até ele acertar um número secreto. Ao errar, o programa deve informar se o valor digitado é maior ou menor. Ao acertar, deve mostrar a quantidade de tentativas.",
        "codigo": None,
        "explicacao": "Resposta aberta. O professor avaliará a lógica do loop, da comparação e do contador de tentativas."
    },
    {
        "id": "Q10",
        "titulo": "Desafio — Fibonacci",
        "tipo": "texto_livre",
        "enunciado": "Escreva um algoritmo ou código Java que imprima os N primeiros termos da sequência de Fibonacci. Exemplo: para N = 7, a saída esperada é 0, 1, 1, 2, 3, 5, 8.",
        "codigo": None,
        "explicacao": "Resposta aberta. O professor avaliará controle de variáveis, repetição e construção da sequência."
    }
]


# =========================================================
# FUNÇÕES DE APOIO
# =========================================================
def ensure_csv_exists():
    if not CSV_PATH.exists():
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp",
                "nome",
                "turma",
                "questao_id",
                "questao_titulo",
                "resposta_aluno",
                "correta",
                "acertou",
                "pontuacao_total"
            ])


def save_submission(nome, turma, respostas, score):
    ensure_csv_exists()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        for q in QUESTOES:
            qid = q["id"]
            titulo = q["titulo"]

            if q["tipo"] == "duplo_select":
                resposta_aluno = {
                    "condicao": respostas.get(f"{qid}_condicao"),
                    "incremento": respostas.get(f"{qid}_incremento")
                }
                correta = {
                    "condicao": q["correta_condicao"],
                    "incremento": q["correta_incremento"]
                }
                acertou = (
                    respostas.get(f"{qid}_condicao") == q["correta_condicao"]
                    and respostas.get(f"{qid}_incremento") == q["correta_incremento"]
                )
            else:
                resposta_aluno = respostas.get(qid)
                correta = q["correta"]
                acertou = resposta_aluno == q["correta"]

            writer.writerow([
                timestamp,
                nome,
                turma,
                qid,
                titulo,
                json.dumps(resposta_aluno, ensure_ascii=False),
                json.dumps(correta, ensure_ascii=False),
                "SIM" if acertou else "NÃO",
                score
            ])

    registro_json = {
        "timestamp": timestamp,
        "nome": nome,
        "turma": turma,
        "pontuacao_total": score,
        "total_questoes": TOTAL_QUESTOES,
        "respostas": respostas
    }

    with open(JSONL_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(registro_json, ensure_ascii=False) + "\n")


def init_session_state():
    defaults = {
        "submitted": False,
        "teacher_logged": False,
        "feedback_mostrado": False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

    for q in QUESTOES:
        if q["tipo"] == "duplo_select":
            st.session_state.setdefault(f"{q['id']}_condicao", None)
            st.session_state.setdefault(f"{q['id']}_incremento", None)
        else:
            st.session_state.setdefault(q["id"], None)


def calcular_resultado():
    score = 0
    respostas = {}

    for q in QUESTOES:
        qid = q["id"]

        if q["tipo"] == "duplo_select":
            condicao = st.session_state.get(f"{qid}_condicao")
            incremento = st.session_state.get(f"{qid}_incremento")

            respostas[f"{qid}_condicao"] = condicao
            respostas[f"{qid}_incremento"] = incremento

            if condicao == q["correta_condicao"] and incremento == q["correta_incremento"]:
                score += 1
        else:
            resposta = st.session_state.get(qid)
            respostas[qid] = resposta
            if resposta == q["correta"]:
                score += 1

    return score, respostas


def render_resultado(score):
    st.subheader("🏁 Resultado")
    st.metric("Pontuação final", f"{score}/{TOTAL_QUESTOES}")

    if score == TOTAL_QUESTOES:
        st.success("Excelente! Você dominou muito bem os conceitos básicos de repetição.")
        st.balloons()
    elif score == TOTAL_QUESTOES - 1:
        st.success("Muito bom! Você entendeu os principais conceitos.")
    elif score >= 2:
        st.warning("Bom começo! Revise as condições de parada e quando usar cada loop.")
    else:
        st.error("Vale revisar os conceitos e tentar novamente.")

    with st.expander("Ver correção comentada"):
        for q in QUESTOES:
            st.markdown(f"### {q['id']} — {q['titulo']}")

            if q["codigo"]:
                st.code(q["codigo"], language="java")

            if q["tipo"] == "duplo_select":
                aluno_cond = st.session_state.get(f"{q['id']}_condicao")
                aluno_inc = st.session_state.get(f"{q['id']}_incremento")

                st.write(f"**Sua condição:** {aluno_cond}")
                st.write(f"**Seu incremento:** {aluno_inc}")
                st.write(
                    f"**Correto:** condição = `{q['correta_condicao']}` | atualização = `{q['correta_incremento']}`"
                )
            else:
                st.write(f"**Sua resposta:** {st.session_state.get(q['id'])}")
                st.write(f"**Correta:** {q['correta']}")

            st.info(q["explicacao"])


def carregar_respostas():
    if not CSV_PATH.exists():
        return pd.DataFrame()
    return pd.read_csv(CSV_PATH)


def teacher_panel():
    st.header("👩‍🏫 Área do Professor")

    if not st.session_state.teacher_logged:
        with st.form("login_professor"):
            senha = st.text_input("Senha do professor", type="password")
            entrar = st.form_submit_button("Entrar")

        if entrar:
            if senha == TEACHER_PASSWORD:
                st.session_state.teacher_logged = True
                st.success("Acesso liberado.")
                st.rerun()
            else:
                st.error("Senha incorreta.")
        return

    if st.button("Sair da área do professor"):
        st.session_state.teacher_logged = False
        st.rerun()

    df = carregar_respostas()

    if df.empty:
        st.info("Ainda não há respostas registradas.")
        return

    st.subheader("Visão geral")
    tentativas = df[["timestamp", "nome", "turma", "pontuacao_total"]].drop_duplicates()

    c1, c2, c3 = st.columns(3)
    c1.metric("Tentativas enviadas", len(tentativas))
    c2.metric("Alunos únicos", tentativas["nome"].nunique())
    c3.metric("Média geral", round(tentativas["pontuacao_total"].mean(), 2))

    st.divider()
    st.subheader("Filtros")

    turmas = ["Todas"] + sorted(
        tentativas["turma"].fillna("").replace("", "(sem turma)").unique().tolist()
    )
    alunos = ["Todos"] + sorted(
        tentativas["nome"].fillna("").unique().tolist()
    )

    colf1, colf2 = st.columns(2)
    turma_sel = colf1.selectbox("Filtrar por turma", turmas)
    aluno_sel = colf2.selectbox("Filtrar por aluno", alunos)

    df_filtrado = df.copy()

    if turma_sel != "Todas":
        turma_real = "" if turma_sel == "(sem turma)" else turma_sel
        df_filtrado = df_filtrado[df_filtrado["turma"].fillna("") == turma_real]

    if aluno_sel != "Todos":
        df_filtrado = df_filtrado[df_filtrado["nome"] == aluno_sel]

    tentativas_filtradas = df_filtrado[
        ["timestamp", "nome", "turma", "pontuacao_total"]
    ].drop_duplicates()

    st.subheader("Tentativas registradas")
    st.dataframe(
        tentativas_filtradas.sort_values("timestamp", ascending=False),
        use_container_width=True
    )

    st.subheader("Detalhamento por questão")
    st.dataframe(
        df_filtrado.sort_values(
            ["timestamp", "nome", "questao_id"],
            ascending=[False, True, True]
        ),
        use_container_width=True
    )

    st.subheader("Acerto por questão")
    resumo_questao = (
        df_filtrado.groupby("questao_id")["acertou"]
        .apply(lambda s: round((s == "SIM").mean() * 100, 1) if len(s) > 0 else 0)
        .reset_index(name="% acerto")
    )
    st.dataframe(resumo_questao, use_container_width=True)

    csv_bytes = df_filtrado.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        "📥 Baixar respostas filtradas em CSV",
        data=csv_bytes,
        file_name="respostas_minidesafio_filtradas.csv",
        mime="text/csv"
    )


# =========================================================
# APP
# =========================================================
init_session_state()

tab_aluno, tab_professor = st.tabs(["🎓 Mini-desafio", "👩‍🏫 Professor"])

with tab_aluno:
    st.title("🔁 Mini-desafio Interativo — Estruturas de Repetição em Java")
    st.caption("Responda às questões e veja seu resultado ao final.")

    with st.container(border=True):
        col1, col2 = st.columns(2)
        nome = col1.text_input("Nome do estudante", key="nome_aluno")
        turma = col2.text_input("Turma", key="turma_aluno")

    st.markdown("""
### Missão
Você vai resolver 4 desafios rápidos sobre:
- `for`
- `while`
- `do-while`
- condição de parada
- leitura e interpretação de código
""")

    with st.form("form_desafio"):
        for q in QUESTOES:
            st.divider()
            st.subheader(f"{q['id']} — {q['titulo']}")
            st.write(q["enunciado"])

            if q["codigo"]:
                st.code(q["codigo"], language="java")

            if q["tipo"] == "radio":
                st.radio(
                    "Escolha uma alternativa:",
                    q["opcoes"],
                    key=q["id"]
                )

            elif q["tipo"] == "duplo_select":
                c1, c2 = st.columns(2)

                c1.selectbox(
                    "Condição:",
                    q["opcoes_condicao"],
                    index=None,
                    placeholder="Selecione a condição",
                    key=f"{q['id']}_condicao"
                )

                c2.selectbox(
                    "Atualização:",
                    q["opcoes_incremento"],
                    index=None,
                    placeholder="Selecione a atualização",
                    key=f"{q['id']}_incremento"
                )

        enviar = st.form_submit_button("✅ Enviar respostas", use_container_width=True)

    if enviar:
        if not nome.strip():
            st.error("Informe o nome do estudante antes de enviar.")
        else:
            score, respostas = calcular_resultado()
            save_submission(nome.strip(), turma.strip(), respostas, score)
            st.session_state.submitted = True
            st.session_state.feedback_mostrado = True
            st.success("Respostas enviadas com sucesso.")
            render_resultado(score)

    elif st.session_state.feedback_mostrado:
        score, _ = calcular_resultado()
        render_resultado(score)

with tab_professor:
    teacher_panel()
