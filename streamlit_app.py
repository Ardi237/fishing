import textwrap

import numpy as np
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Alur Analisis Data",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
    :root {
        --bg: #191919;
        --sidebar: #202020;
        --panel: #242424;
        --panel-active: #2c2c2c;
        --ink: #f2f2f2;
        --muted: #a8a8a8;
        --line: #333333;
        --line-strong: #464646;
        --accent: #31b7e8;
        --accent-soft: #153540;
    }

    .stApp {
        background: var(--bg);
        color: var(--ink);
        font-family: "Segoe UI Variable", "Segoe UI", sans-serif;
    }

    [data-testid="stSidebar"] {
        background: var(--sidebar);
        border-right: 1px solid var(--line);
    }

    [data-testid="stSidebarCollapseButton"],
    [data-testid="collapsedControl"] {
        display: none !important;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.1rem;
    }

    [data-testid="stSidebar"] [role="radiogroup"] {
        gap: 0.28rem;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label {
        border-radius: 3px;
        padding: 0.62rem 0.7rem;
        transition: background 120ms ease;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label:hover {
        background: #282828;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
        background: var(--panel-active);
        box-shadow: inset 3px 0 0 var(--accent);
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
        color: var(--muted);
    }

    .block-container {
        max-width: 1320px;
        padding-top: 1.15rem;
        padding-bottom: 3rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    h1, h2, h3 {
        color: var(--ink);
        letter-spacing: -0.02em;
        font-weight: 500;
    }

    h1 {
        font-size: 2rem;
        line-height: 1.18;
        margin-bottom: 0.35rem;
    }

    h2, h3 {
        font-size: 1rem;
        letter-spacing: 0;
    }

    .eyebrow {
        color: var(--muted);
        font-size: 0.8rem;
        font-weight: 400;
        margin-bottom: 0.25rem;
    }

    .lead {
        color: var(--muted);
        font-size: 0.9rem;
        line-height: 1.55;
        max-width: 760px;
        margin-bottom: 1.2rem;
    }

    .appbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        min-height: 48px;
        border-bottom: 1px solid var(--line);
        margin: -1.15rem -2rem 1.45rem;
        padding: 0 2rem;
        color: var(--ink);
    }

    .appbar-title {
        font-size: 0.96rem;
        font-weight: 500;
    }

    .appbar-meta {
        color: var(--muted);
        font-size: 0.8rem;
    }

    .task-row {
        display: grid;
        grid-template-columns: 42px 1fr auto;
        gap: 0.75rem;
        align-items: center;
        min-height: 68px;
        border-bottom: 1px solid var(--line);
        background: transparent;
        padding: 0.65rem 0.25rem;
    }

    .task-row:hover {
        background: #1d1d1d;
    }

    .task-index {
        color: var(--accent);
        font-size: 0.8rem;
        font-variant-numeric: tabular-nums;
    }

    .task-title {
        color: var(--ink);
        font-size: 0.96rem;
        font-weight: 500;
    }

    .task-copy, .card-copy {
        color: var(--muted);
        font-size: 0.82rem;
        line-height: 1.45;
        margin-top: 0.16rem;
    }

    .task-state {
        color: var(--muted);
        font-size: 0.76rem;
        font-variant-numeric: tabular-nums;
    }

    .note {
        border-top: 1px solid var(--line);
        border-bottom: 1px solid var(--line);
        background: transparent;
        color: var(--muted);
        padding: 0.65rem 0;
        margin: 1rem 0 1.25rem;
        font-size: 0.84rem;
    }

    .note strong {
        color: var(--ink);
        font-weight: 500;
    }

    .step-row {
        border-top: 1px solid var(--line);
        padding: 0.72rem 0;
    }

    .step-label {
        color: var(--accent);
        font-size: 0.74rem;
        font-variant-numeric: tabular-nums;
    }

    .step-title {
        color: var(--ink);
        font-size: 0.94rem;
        font-weight: 500;
        margin-top: 0.12rem;
    }

    div[data-testid="stMetric"] {
        border: 0;
        border-top: 1px solid var(--line-strong);
        border-radius: 0;
        padding: 0.65rem 0;
        background: transparent;
    }

    div[data-testid="stMetricValue"] {
        color: var(--ink);
        font-variant-numeric: tabular-nums;
        font-weight: 400;
    }

    div[data-testid="stExpander"] {
        border: 1px solid var(--line);
        border-radius: 2px;
        background: var(--panel);
        box-shadow: none;
    }

    .status-done {
        color: var(--accent);
        font-weight: 400;
        font-size: 0.82rem;
    }

    .status-open {
        color: var(--muted);
        font-size: 0.82rem;
    }

    .footer {
        border-top: 1px solid var(--line);
        color: var(--muted);
        font-size: 0.76rem;
        margin-top: 2.5rem;
        padding-top: 1rem;
    }

    [data-testid="stProgress"] > div > div {
        background-color: var(--accent);
    }

    [data-testid="stProgress"] > div {
        border-radius: 0;
    }

    .stButton > button,
    .stDownloadButton > button {
        border-radius: 2px;
        border-color: var(--line-strong);
        background: var(--panel);
        color: var(--ink);
        box-shadow: none;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        border-color: var(--accent);
        color: var(--ink);
    }

    .stButton > button[kind="primary"],
    .stDownloadButton > button[kind="primary"] {
        background: var(--accent);
        border-color: var(--accent);
        color: #071216;
    }

    [data-baseweb="select"] > div,
    [data-testid="stFileUploaderDropzone"],
    [data-testid="stDataFrame"] {
        border-radius: 2px !important;
    }

    [data-testid="stTabs"] [role="tablist"] {
        gap: 1.25rem;
        border-bottom: 1px solid var(--line);
    }

    [data-testid="stTabs"] [role="tab"] {
        padding-left: 0;
        padding-right: 0;
    }

    hr {
        border-color: var(--line) !important;
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def build_demo_data() -> pd.DataFrame:
    """Create deterministic sample data for the UI simulation."""
    rng = np.random.default_rng(42)
    size = 120
    age = rng.integers(18, 65, size=size)
    bmi = np.clip(rng.normal(30.5, 5.8, size=size), 17, 49)
    smoker = rng.choice(["no", "yes"], size=size, p=[0.79, 0.21])
    sex = rng.choice(["female", "male"], size=size)
    children = rng.integers(0, 6, size=size)
    region = rng.choice(
        ["northeast", "northwest", "southeast", "southwest"],
        size=size,
    )
    charges = (
        1200
        + age * 230
        + bmi * 105
        + children * 420
        + (smoker == "yes") * (15000 + bmi * 260)
        + rng.normal(0, 2100, size=size)
    )
    charges = np.clip(charges, 1100, None)

    return pd.DataFrame(
        {
            "age": age,
            "sex": sex,
            "bmi": bmi.round(2),
            "children": children,
            "smoker": smoker,
            "region": region,
            "charges": charges.round(2),
        }
    )


def page_heading(kicker: str, title: str, description: str) -> None:
    st.markdown(f'<div class="eyebrow">{kicker}</div>', unsafe_allow_html=True)
    st.title(title)
    st.markdown(f'<div class="lead">{description}</div>', unsafe_allow_html=True)


def task_card(number: str, title: str, copy: str) -> None:
    st.markdown(
        f"""
        <div class="task-row">
            <div class="task-index">{number}</div>
            <div>
                <div class="task-title">{title}</div>
                <div class="task-copy">{copy}</div>
            </div>
            <div class="task-state">siap</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def step_row(label: str, title: str, copy: str) -> None:
    st.markdown(
        f"""
        <div class="step-row">
            <div class="step-label">{label}</div>
            <div class="step-title">{title}</div>
            <div class="card-copy">{copy}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def mark_task_done(task_number: int) -> None:
    if st.button(
        "Tandai bagian ini selesai",
        key=f"complete_{task_number}",
        type="primary",
        width="content",
    ):
        st.session_state.completed.add(task_number)
        st.toast(f"Task {task_number} ditandai selesai")


if "completed" not in st.session_state:
    st.session_state.completed = set()

if "show_collection" not in st.session_state:
    st.session_state.show_collection = False


demo = build_demo_data()

PAGES = [
    "Gambaran umum",
    "Task 1 · Data collecting",
    "Task 2 · Deskripsi data",
    "Task 3 · Statistika deskriptif",
    "Task 4 · Visualisasi data",
    "Ringkasan akhir",
]


with st.sidebar:
    st.markdown("### Analisis Asuransi")
    st.caption("Alur kerja data kesehatan")
    st.space("small")

    page = st.radio(
        "Pilih bagian",
        PAGES,
        label_visibility="collapsed",
    )

    st.divider()
    progress_value = len(st.session_state.completed) / 4
    st.caption("Progres tugas")
    st.progress(progress_value)
    st.caption(f"{len(st.session_state.completed)} dari 4 task selesai")

    for number in range(1, 5):
        if number in st.session_state.completed:
            st.markdown(
                f'<div class="status-done">Task {number} · selesai</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="status-open">Task {number} · belum selesai</div>',
                unsafe_allow_html=True,
            )

    st.divider()
    st.caption("Dataset")
    st.markdown("Biaya asuransi kesehatan")
    st.caption("Mode simulasi · bukan hasil final")


st.markdown(
    """
    <div class="appbar">
        <div class="appbar-title">Analisis Data</div>
        <div class="appbar-meta">Biaya asuransi kesehatan · simulasi</div>
    </div>
    """,
    unsafe_allow_html=True,
)


if page == "Gambaran umum":
    page_heading(
        "Gambaran umum",
        "Analisis biaya asuransi kesehatan",
        "Alur kerja untuk memeriksa struktur data, membersihkan temuan, menghitung statistik deskriptif, "
        "dan menyusun visualisasi. Angka pada layar ini merupakan data simulasi.",
    )

    st.markdown(
        '<div class="note"><strong>Fokus:</strong> deskripsi dan visualisasi data. Tidak ada pemodelan, prediksi, atau evaluasi machine learning.</div>',
        unsafe_allow_html=True,
    )

    process_col, signal_col = st.columns([0.42, 0.58], gap="large")
    with process_col:
        st.subheader("Urutan kerja")
        task_card("01", "Data collecting", "Sumber, unit observasi, dan struktur dataset.")
        task_card("02", "Deskripsi data", "Audit nilai kosong, duplikat, tipe, dan cleaning.")
        task_card("03", "Statistika", "Pusat, sebaran, kuartil, skewness, dan pencilan.")
        task_card("04", "Visualisasi", "Grafik yang menjawab pertanyaan dan interpretasinya.")
    with signal_col:
        st.subheader("Cuplikan biaya")
        st.caption("60 observasi simulasi · variabel charges")
        signal = demo[["charges"]].head(60).rename(columns={"charges": "Charges"})
        st.line_chart(signal, color="#31b7e8", height=330)
        s1, s2, s3 = st.columns(3)
        s1.metric("Observasi", "60")
        s2.metric("Rata-rata", f"{signal['Charges'].mean():,.0f}")
        s3.metric("Maksimum", f"{signal['Charges'].max():,.0f}")

    st.subheader("Cara membaca simulasi")
    step_row("Langkah 1", "Pilih task dari sidebar", "Setiap halaman menjelaskan tujuan, proses, contoh kode, dan keluaran yang perlu dibaca.")
    step_row("Langkah 2", "Ubah kontrol interaktif", "Gunakan pilihan variabel, skenario cleaning, ukuran sampel, dan jenis grafik.")
    step_row("Langkah 3", "Tandai task selesai", "Progres tersimpan selama sesi Streamlit masih aktif.")


elif page == "Task 1 · Data collecting":
    page_heading(
        "Task 1",
        "Data collecting",
        "Tahap pertama memastikan data layak digunakan dan dapat dijelaskan asal-usulnya. "
        "Kita belum menghitung apa pun; kita menetapkan konteks dan batas analisis.",
    )

    source_choice = st.selectbox(
        "Sumber data",
        ["Kaggle · Medical Insurance Cost", "Unggah CSV sendiri"],
    )

    left, right = st.columns([1.1, 1])
    with left:
        st.subheader("Yang perlu dicatat")
        step_row("01", "Jenis data", "Data sekunder yang diperoleh dari sumber publik.")
        step_row("02", "Unit observasi", "Satu baris merepresentasikan satu individu peserta asuransi.")
        step_row("03", "Variabel", "Empat numerik dan tiga kategorikal, dengan charges sebagai variabel dependen.")
        step_row("04", "Batas data", "Tidak ada variabel tanggal, sehingga tidak dapat digunakan untuk tren waktu.")

    with right:
        st.subheader("Rancangan pemuatan")
        if source_choice.startswith("Kaggle"):
            st.code(
                textwrap.dedent(
                    """
                    path = kagglehub.dataset_download(
                        "hetmengar/medical-insurance-cost-prediction"
                    )
                    csv_files = list(Path(path).rglob("*.csv"))
                    df = pd.read_csv(csv_files[0])
                    """
                ).strip(),
                language="python",
            )
        else:
            st.code(
                "uploaded = st.file_uploader('Pilih CSV', type='csv')\n"
                "if uploaded is not None:\n"
                "    df = pd.read_csv(uploaded)",
                language="python",
            )

        if st.button("Simulasikan pemuatan data", width="stretch"):
            st.session_state.show_collection = True

    if st.session_state.show_collection:
        st.divider()
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Baris", "1.338")
        m2.metric("Kolom", "7")
        m3.metric("Numerik", "4")
        m4.metric("Kategorikal", "3")
        st.caption("Tabel berikut adalah cuplikan data simulasi untuk memperagakan antarmuka.")
        st.dataframe(demo.head(8), width="stretch", hide_index=True)

    mark_task_done(1)


elif page == "Task 2 · Deskripsi data":
    page_heading(
        "Task 2",
        "Audit, cleaning, dan deskripsi kondisi data",
        "Cleaning tidak berarti menghapus sebanyak mungkin. Setiap perubahan harus memiliki alasan dan hasilnya harus dapat diperiksa kembali.",
    )

    add_duplicate = st.toggle("Sisipkan contoh baris duplikat", value=True)
    add_missing = st.toggle("Sisipkan contoh nilai kosong", value=True)

    before = demo.head(12).copy()
    if add_duplicate:
        before = pd.concat([before, before.iloc[[0]]], ignore_index=True)
    if add_missing:
        before.loc[2, "bmi"] = np.nan

    after = before.drop_duplicates().copy()
    if after["bmi"].isna().any():
        after["bmi"] = after["bmi"].fillna(after["bmi"].mean())

    m1, m2, m3 = st.columns(3)
    m1.metric("Baris sebelum", len(before))
    m2.metric("Duplikat", int(before.duplicated().sum()))
    m3.metric("Nilai kosong", int(before.isna().sum().sum()))

    tab_before, tab_after, tab_decision = st.tabs(
        ["Sebelum cleaning", "Sesudah cleaning", "Keputusan"]
    )
    with tab_before:
        st.dataframe(before, width="stretch", hide_index=True)
    with tab_after:
        st.dataframe(after, width="stretch", hide_index=True)
    with tab_decision:
        step_row("Duplikat", "Hapus salinan identik", "Satu observasi hanya dihitung satu kali.")
        step_row("Numerik kosong", "Imputasi mean jika diperlukan", "Diterapkan hanya jika benar-benar ada nilai kosong.")
        step_row("Kategori kosong", "Gunakan modus, bukan mean", "Mean tidak memiliki makna untuk kategori nominal.")
        step_row("Pencilan", "Deteksi dahulu, jangan otomatis hapus", "Biaya tinggi bisa menjadi kejadian valid dan penting.")

    with st.expander("Lihat potongan kode cleaning"):
        st.code(
            textwrap.dedent(
                """
                df_clean = df.drop_duplicates().copy()

                for column in numeric_cols:
                    if df_clean[column].isna().any():
                        df_clean[column] = df_clean[column].fillna(
                            df_clean[column].mean()
                        )
                """
            ).strip(),
            language="python",
        )

    mark_task_done(2)


elif page == "Task 3 · Statistika deskriptif":
    page_heading(
        "Task 3",
        "Statistika deskriptif",
        "Statistik merangkum pusat, sebaran, bentuk distribusi, dan posisi nilai ekstrem. "
        "Tujuannya bukan sekadar menghasilkan tabel, tetapi menjelaskan apa yang berarti dari tabel tersebut.",
    )

    variable = st.selectbox("Pilih variabel numerik", ["charges", "age", "bmi", "children"])
    series = demo[variable]
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = ((series < lower) | (series > upper)).sum()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Mean", f"{series.mean():,.2f}")
    c2.metric("Median", f"{series.median():,.2f}")
    c3.metric("Std. deviasi", f"{series.std():,.2f}")
    c4.metric("Skewness", f"{series.skew():,.2f}")

    summary_table = pd.DataFrame(
        {
            "Statistik": ["Minimum", "Q1", "Median", "Q3", "Maksimum", "IQR", "Pencilan IQR"],
            "Nilai": [series.min(), q1, series.median(), q3, series.max(), iqr, outliers],
        }
    )

    left, right = st.columns([1, 1.15])
    with left:
        st.dataframe(summary_table, width="stretch", hide_index=True)
    with right:
        if series.mean() > series.median():
            shape_text = "Rata-rata berada di atas median; distribusi cenderung memiliki ekor ke kanan."
        elif series.mean() < series.median():
            shape_text = "Rata-rata berada di bawah median; distribusi cenderung memiliki ekor ke kiri."
        else:
            shape_text = "Rata-rata dan median berdekatan; distribusi relatif seimbang."
        st.markdown(
            f'<div class="note"><strong>Cara membaca:</strong> {shape_text} '
            f'Metode IQR mendeteksi {int(outliers)} nilai ekstrem pada data simulasi.</div>',
            unsafe_allow_html=True,
        )
        st.caption("Pencilan adalah sinyal untuk diperiksa, bukan instruksi otomatis untuk menghapus data.")

    group_variable = st.selectbox(
        "Bandingkan charges berdasarkan",
        ["smoker", "sex", "region", "children"],
    )
    grouped = (
        demo.groupby(group_variable, observed=True)["charges"]
        .agg(["count", "mean", "median", "std"])
        .round(2)
    )
    st.dataframe(grouped, width="stretch")

    with st.expander("Lihat potongan kode statistik"):
        st.code(
            "summary = df[numeric_cols].describe().T\n"
            "summary['IQR'] = summary['75%'] - summary['25%']\n"
            "summary['skewness'] = df[numeric_cols].skew()",
            language="python",
        )

    mark_task_done(3)


elif page == "Task 4 · Visualisasi data":
    page_heading(
        "Task 4",
        "Visualisasi dan interpretasi",
        "Grafik dipilih berdasarkan pertanyaan. Satu grafik yang tepat lebih berguna daripada banyak grafik yang tidak memiliki tujuan.",
    )

    sample_size = st.slider(
        "Ukuran sampel simulasi",
        min_value=30,
        max_value=len(demo),
        value=70,
        step=10,
    )
    sampled = demo.sample(n=sample_size, random_state=42)

    chart_choice = st.selectbox(
        "Pilih pertanyaan visual",
        [
            "Bagaimana distribusi charges?",
            "Bagaimana biaya menurut status merokok?",
            "Bagaimana hubungan umur dan biaya?",
            "Bagaimana hubungan BMI dan biaya?",
            "Bagaimana perbandingan wilayah?",
        ],
    )

    if chart_choice == "Bagaimana distribusi charges?":
        counts, edges = np.histogram(sampled["charges"], bins=12)
        labels = [f"{edges[i] / 1000:.0f}-{edges[i + 1] / 1000:.0f}k" for i in range(len(counts))]
        histogram = pd.DataFrame({"Rentang": labels, "Frekuensi": counts}).set_index("Rentang")
        st.bar_chart(histogram, color="#31b7e8")
        st.markdown(
            '<div class="note"><strong>Interpretasi:</strong> lihat apakah frekuensi terkonsentrasi pada biaya rendah dan memiliki ekor panjang ke biaya tinggi.</div>',
            unsafe_allow_html=True,
        )

    elif chart_choice == "Bagaimana biaya menurut status merokok?":
        smoker_chart = sampled.groupby("smoker")["charges"].mean().to_frame("Rata-rata charges")
        st.bar_chart(smoker_chart, color="#31b7e8")
        st.markdown(
            '<div class="note"><strong>Interpretasi:</strong> bandingkan tinggi batang perokok dan nonperokok, lalu periksa median dan sebarannya pada analisis lengkap.</div>',
            unsafe_allow_html=True,
        )

    elif chart_choice == "Bagaimana hubungan umur dan biaya?":
        st.scatter_chart(sampled, x="age", y="charges", color="smoker")
        st.markdown(
            '<div class="note"><strong>Interpretasi:</strong> amati arah pola titik dan pisahkan pembacaan berdasarkan warna status merokok.</div>',
            unsafe_allow_html=True,
        )

    elif chart_choice == "Bagaimana hubungan BMI dan biaya?":
        st.scatter_chart(sampled, x="bmi", y="charges", color="smoker")
        st.markdown(
            '<div class="note"><strong>Interpretasi:</strong> hubungan BMI dengan biaya dapat berbeda antara perokok dan nonperokok.</div>',
            unsafe_allow_html=True,
        )

    else:
        region_chart = sampled.groupby("region")["charges"].mean().sort_values().to_frame("Rata-rata charges")
        st.bar_chart(region_chart, color="#31b7e8")
        st.markdown(
            '<div class="note"><strong>Interpretasi:</strong> perbedaan wilayah perlu dibaca bersama komposisi umur, BMI, dan status merokok; jangan langsung dianggap sebagai pengaruh wilayah.</div>',
            unsafe_allow_html=True,
        )

    st.caption(f"Grafik menggunakan {sample_size} observasi simulasi. Statistik laporan tetap sebaiknya dihitung dari seluruh data bersih.")

    with st.expander("Panduan memilih grafik"):
        chart_guide = pd.DataFrame(
            {
                "Pertanyaan": [
                    "Distribusi satu variabel numerik",
                    "Pencilan dan kuartil",
                    "Perbandingan kategori",
                    "Hubungan dua numerik",
                    "Korelasi banyak numerik",
                ],
                "Grafik": ["Histogram", "Boxplot", "Bar chart / boxplot", "Scatter plot", "Heatmap"],
            }
        )
        st.dataframe(chart_guide, width="stretch", hide_index=True)

    mark_task_done(4)


else:
    page_heading(
        "Penutup",
        "Ringkasan akhir",
        "Bagian terakhir mengubah hasil teknis menjadi susunan laporan yang singkat, dapat diperiksa, dan tidak melebih-lebihkan temuan.",
    )

    status_rows = []
    task_names = {
        1: "Data collecting",
        2: "Deskripsi dan cleaning data",
        3: "Statistika deskriptif",
        4: "Visualisasi data",
    }
    for number, name in task_names.items():
        status_rows.append(
            {
                "Task": f"Task {number}",
                "Bagian": name,
                "Status": "Selesai" if number in st.session_state.completed else "Belum selesai",
            }
        )
    st.dataframe(pd.DataFrame(status_rows), width="stretch", hide_index=True)

    st.subheader("Susunan narasi laporan")
    step_row("01", "Perkenalkan data", "Sebutkan sumber, tanggal akses, unit observasi, jumlah baris, dan jenis variabel.")
    step_row("02", "Jelaskan cleaning", "Laporkan kondisi sebelum dan sesudah, serta alasan setiap tindakan.")
    step_row("03", "Baca statistik", "Jelaskan mean, median, standar deviasi, kuartil, skewness, dan pencilan dalam konteks data.")
    step_row("04", "Hubungkan grafik dengan pertanyaan", "Setiap visualisasi harus memiliki satu pesan utama yang didukung data.")
    step_row("05", "Tulis keterbatasan", "Gunakan bahasa asosiasi dan hindari klaim sebab-akibat.")

    report_template = """JUDUL\nAnalisis Deskriptif Faktor yang Berkaitan dengan Biaya Asuransi Kesehatan\n\n1. Sumber dan kondisi data\n2. Proses cleaning\n3. Statistik deskriptif\n4. Visualisasi dan interpretasi\n5. Kesimpulan\n6. Keterbatasan\n"""
    st.download_button(
        "Unduh kerangka laporan",
        data=report_template,
        file_name="kerangka_laporan.txt",
        mime="text/plain",
        type="primary",
    )

    if len(st.session_state.completed) == 4:
        st.success("Seluruh alur simulasi sudah selesai.")
    else:
        st.info("Selesaikan task dari sidebar untuk melihat progres penuh.")


st.markdown(
    '<div class="footer">Simulasi antarmuka pembelajaran · data contoh tidak menggantikan hasil analisis pada notebook utama.</div>',
    unsafe_allow_html=True,
)

