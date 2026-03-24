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
        "enunciado": "Qual código imprime corretamente os números de 1 até 10?",
        "codigo": None,
        "opcoes": [
            "for (int i = 0; i < 10; i++) { System.out.println(i); }",
            "for (int i = 1; i <= 10; i++) { System.out.println(i); }",
            "for (int i = 1; i < 10; i++) { System.out.println(i); }",
            "for (int i = 10; i >= 1; i--) { System.out.println(i); }"
        ],
        "correta": "for (int i = 1; i <= 10; i++) { System.out.println(i); }",
        "explicacao": "O laço começa em 1, vai até 10 e incrementa corretamente."
    },
    {
        "id": "Q2",
        "titulo": "Contagem regressiva",
        "tipo": "radio",
        "enunciado": "Qual será a saída do código abaixo?",
        "codigo": """for (int i = 5; i >= 1; i--) {
    System.out.print(i + " ");
}""",
        "opcoes": [
            "1 2 3 4 5",
            "5 4 3 2 1",
            "5 3 1",
            "Loop infinito"
        ],
        "correta": "5 4 3 2 1",
        "explicacao": "O contador começa em 5 e decrementa até 1."
    },
    {
        "id": "Q3",
        "titulo": "Soma de valores",
        "tipo": "radio",
        "enunciado": "Qual será o valor final de soma?",
        "codigo": """int soma = 0;
for (int i = 1; i <= 4; i++) {
    soma += i;
}""",
        "opcoes": [
            "4",
            "6",
            "10",
            "8"
        ],
        "correta": "10",
        "explicacao": "1 + 2 + 3 + 4 = 10."
    },
    {
        "id": "Q4",
        "titulo": "Números pares",
        "tipo": "radio",
        "enunciado": "Qual condição imprime apenas números pares?",
        "codigo": None,
        "opcoes": [
            "i % 2 == 1",
            "i % 2 == 0",
            "i / 2 == 0",
            "i == 2"
        ],
        "correta": "i % 2 == 0",
        "explicacao": "Números pares têm resto 0 na divisão por 2."
    },
    {
        "id": "Q5",
        "titulo": "Uso do while",
        "tipo": "radio",
        "enunciado": "Quando devemos usar while?",
        "codigo": None,
        "opcoes": [
            "Quando sabemos quantas vezes repetir",
            "Quando depende de uma condição",
            "Quando executa apenas uma vez",
            "Quando não há condição"
        ],
        "correta": "Quando depende de uma condição",
        "explicacao": "while é usado quando não sabemos o número de repetições."
    },
    {
        "id": "Q6",
        "titulo": "Tabuada",
        "tipo": "radio",
        "enunciado": "Qual será a saída do código?",
        "codigo": """int n = 2;
for (int i = 1; i <= 3; i++) {
    System.out.print(n * i + " ");
}""",
        "opcoes": [
            "2 4 6",
            "1 2 3",
            "2 3 4",
            "2 6 12"
        ],
        "correta": "2 4 6",
        "explicacao": "2x1=2, 2x2=4, 2x3=6."
    },
    {
        "id": "Q7",
        "titulo": "Múltiplos de 3",
        "tipo": "radio",
        "enunciado": "Qual condição identifica múltiplos de 3?",
        "codigo": None,
        "opcoes": [
            "i % 3 == 1",
            "i % 3 == 0",
            "i / 3 == 0",
            "i == 3"
        ],
        "correta": "i % 3 == 0",
        "explicacao": "Múltiplos de 3 deixam resto 0."
    },
    {
        "id": "Q8",
        "titulo": "Condição de parada",
        "tipo": "radio",
        "enunciado": "O que faz um loop parar?",
        "codigo": None,
        "opcoes": [
            "Incremento",
            "Condição falsa",
            "Print",
            "Início do loop"
        ],
        "correta": "Condição falsa",
        "explicacao": "O loop termina quando a condição não é mais verdadeira."
    },
    {
        "id": "Q9",
        "titulo": "Desafio — análise de loop",
        "tipo": "radio",
        "enunciado": "Qual será a saída?",
        "codigo": """int x = 1;

while (x < 5) {
    System.out.print(x + " ");
    x = x + 2;
}""",
        "opcoes": [
            "1 2 3 4",
            "1 3 5",
            "1 3",
            "Loop infinito"
        ],
        "correta": "1 3",
        "explicacao": "x começa em 1 e incrementa de 2 em 2: 1 → 3 → para antes do 5."
    },
    {
        "id": "Q10",
        "titulo": "Desafio — erro lógico",
        "tipo": "radio",
        "enunciado": "O que acontece com o código?",
        "codigo": """int x = 10;

while (x > 0) {
    System.out.print(x + " ");
}""",
        "opcoes": [
            "Imprime 10 até 1",
            "Loop infinito",
            "Erro de compilação",
            "Imprime apenas 10"
        ],
        "correta": "Loop infinito",
        "explicacao": "x nunca é alterado, então a condição sempre será verdadeira."
    }
    {
        "id": "Q11",
        "titulo": "Transformação — for para while",
        "tipo": "radio",
        "enunciado": "Qual alternativa representa corretamente a conversão do loop for para while?",
        "codigo": """for (int i = 1; i <= 3; i++) {
        System.out.println(i);
    }""",
        "opcoes": [
            """int i = 1;
    while (i <= 3) {
        System.out.println(i);
    }""",
            """int i = 1;
    while (i <= 3) {
        System.out.println(i);
        i++;
    }""",
            """int i = 0;
    while (i < 3) {
        System.out.println(i);
    }""",
            """while (i <= 3) {
        System.out.println(i);
        i++;
    }"""
        ],
        "correta": """int i = 1;
    while (i <= 3) {
        System.out.println(i);
        i++;
    }""",
        "explicacao": "O for possui inicialização, condição e incremento. No while, precisamos declarar a variável antes e atualizar manualmente dentro do bloco."
    },
    {
        "id": "Q12",
        "titulo": "Transformação — while para for",
        "tipo": "radio",
        "enunciado": "Qual alternativa representa corretamente a conversão do while para for?",
        "codigo": """int i = 1;
    
    while (i <= 3) {
        System.out.println(i);
        i++;
    }""",
        "opcoes": [
            """for (int i = 1; i <= 3; i++) {
        System.out.println(i);
    }""",
            """for (int i = 0; i < 3; i++) {
        System.out.println(i);
    }""",
            """for (i = 1; i <= 3; i++) {
        System.out.println(i);
    }""",
            """for (int i = 1; i < 3; i++) {
        System.out.println(i);
    }"""
        ],
        "correta": """for (int i = 1; i <= 3; i++) {
        System.out.println(i);
    }""",
        "explicacao": "O for reúne inicialização, condição e incremento em uma única linha."
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
