import streamlit as st
from data.reports import REPORTS, DEPARTMENTS, REPORT_TYPES, FREQUENCIES, FOLLOWUP_QUESTIONS

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="CMA CGM Active BI Catalog",
    page_icon="📊",
    layout="centered"
)

# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
    .catalog-eyebrow {
        font-size: 12px; font-weight: 600; color: #185FA5;
        text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 4px;
    }
    .section-label {
        font-size: 11px; font-weight: 600; color: #94A3B8;
        text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 6px;
    }
    .tag { display: inline-block; padding: 2px 10px; border-radius: 20px; font-size: 12px; font-weight: 500; margin-right: 4px; margin-bottom: 4px; }
    .tag-dept  { background:#E6F1FB; color:#0C447C; border:1px solid #85B7EB; }
    .tag-type  { background:#EEEDFE; color:#3C3489; border:1px solid #AFA9EC; }
    .tag-freq  { background:#FAEEDA; color:#633806; border:1px solid #EF9F27; }
    .tag-grain { background:#FAECE7; color:#712B13; border:1px solid #F0997B; }
    .tag-topic { background:#EAF3DE; color:#27500A; border:1px solid #97C459; }
    .match-best-banner {
        background:#E1F5EE; color:#085041; border-radius:6px;
        padding:8px 12px; font-size:13px; margin-bottom:12px;
    }
    .match-partial-banner {
        background:#FAEEDA; color:#633806; border-radius:6px;
        padding:8px 12px; font-size:13px; margin-bottom:12px;
    }
    .no-match-box {
        border:1px dashed #CBD5E1; border-radius:10px;
        padding:1.5rem; text-align:center; margin-top:1rem;
    }
    .followup-box {
        background:#F1F5F9; border:1px solid #E2E8F0;
        border-radius:10px; padding:1.2rem; margin-bottom:1rem;
    }
    .score-bar-bg {
        background:#E2E8F0; border-radius:4px; height:6px; width:100%;
    }
    .metric-card {
        background:white; border:1px solid #E2E8F0; border-radius:10px;
        padding:1rem; text-align:center;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
defaults = {
    "screen": "search",
    "search_dept": [],
    "search_type": [],
    "search_desc": "",
    "results": [],
    "followup_answer": None,
    "access_report": None,
    "show_followup": False,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ─────────────────────────────────────────────
# MATCHING LOGIC
# ─────────────────────────────────────────────
def match_reports(departments, report_types, description, followup_keywords=None):
    results = []
    desc_words = description.lower().split() if description else []
    all_keywords = desc_words + (followup_keywords or [])

    for report in REPORTS:
        score = 0
        reasons = []

        # Hard filter: department
        if departments:
            if report["department"] in departments:
                score += 4
                reasons.append(f"matches your {report['department']} department")
            else:
                continue

        # Hard filter: report type
        if report_types:
            if report["report_type"] in report_types:
                score += 2
                reasons.append(f"{report['report_type']} report type")
            else:
                continue

        # Keyword match
        searchable = " ".join([
            report["name"], report["description"],
            report["use_case"], report["scope"],
            " ".join(report["keywords"])
        ]).lower()

        matched = [w for w in all_keywords if len(w) > 3 and w.lower() in searchable]
        score += len(matched) * 2

        if matched:
            unique = list(dict.fromkeys(matched))[:3]
            reasons.append(f"covers: {', '.join(unique)}")

        # Follow-up bonus
        if followup_keywords:
            fu_matches = [w for w in followup_keywords if w.lower() in searchable]
            score += len(fu_matches) * 3
            if fu_matches:
                reasons.append("strongly aligns with your clarified need")

        if not departments and not report_types and not all_keywords:
            score = 1

        match_reason = ("✓ " + "; ".join(reasons).capitalize() + ".") if reasons else "Returned based on your selections."
        results.append((report, score, match_reason))

    results.sort(key=lambda x: x[1], reverse=True)
    return results

# ─────────────────────────────────────────────
# RENDER REPORT CARD
# ─────────────────────────────────────────────
def render_card(report, score, match_reason, rank, max_score):
    is_best = rank == 0
    badge = "🥇 Best match" if is_best else f"#{rank+1} Partial match"
    banner_class = "match-best-banner" if is_best else "match-partial-banner"

    with st.container():
        col_title, col_badge = st.columns([5, 1.5])
        with col_title:
            st.markdown(f"**{report['name']}**")
        with col_badge:
            st.markdown(f"<small>{badge}</small>", unsafe_allow_html=True)

        # Match reason
        st.markdown(f'<div class="{banner_class}">{match_reason}</div>', unsafe_allow_html=True)

        # Relevance bar
        if max_score > 0:
            pct = min(int((score / max_score) * 100), 100)
            st.markdown(
                f'<div class="score-bar-bg"><div style="width:{pct}%;background:#185FA5;height:6px;border-radius:4px;"></div></div>'
                f'<small style="color:#94A3B8;">Relevance: {pct}%</small>',
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # Content
        st.markdown(f"📌 **What it does:** {report['description']}")
        st.markdown(f"💡 **When to use it:** {report['use_case']}")

        with st.expander("View scope & data details"):
            st.markdown(f"🔍 **Scope:** {report['scope']}")

        # Tags
        tags_html = (
            f'<span class="tag tag-dept">{report["department"]}</span>'
            f'<span class="tag tag-type">{report["report_type"]}</span>'
            f'<span class="tag tag-freq">{report["frequency"]}</span>'
            f'<span class="tag tag-grain">{report["grain"]}</span>'
            + "".join(f'<span class="tag tag-topic">{t}</span>' for t in report["topics"])
        )
        st.markdown(tags_html, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        # Owner + actions
        col_owner, col_access, col_open = st.columns([3, 1.3, 1.3])
        with col_owner:
            st.markdown(f"👤 **{report['owner_name']}** · {report['owner_email']}")
        with col_access:
            if st.button("Request access", key=f"access_{report['id']}_{rank}"):
                st.session_state.access_report = report
                st.session_state.screen = "access"
                st.rerun()
        with col_open:
            st.link_button("Open report →", report["report_link"])

        st.markdown("---")

# ─────────────────────────────────────────────
# SCREEN: SEARCH
# ─────────────────────────────────────────────
def screen_search():
    st.markdown('<p class="catalog-eyebrow">CMA CGM · United States</p>', unsafe_allow_html=True)
    st.title("📊 Active BI catalog")
    st.markdown("Find existing reports and dashboards — or submit a request if you need something new.")
    st.markdown("---")

    # Nav to dashboard
    if st.button("📈 View catalog analytics"):
        st.session_state.screen = "dashboard"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<p class="section-label">Your department</p>', unsafe_allow_html=True)
    selected_depts = st.multiselect("Department", DEPARTMENTS,
        default=st.session_state.search_dept, label_visibility="collapsed",
        placeholder="Select one or more departments...")

    st.markdown('<p class="section-label">Report type</p>', unsafe_allow_html=True)
    selected_types = st.multiselect("Report type", REPORT_TYPES,
        default=st.session_state.search_type, label_visibility="collapsed",
        placeholder="Select report type...")

    st.markdown('<p class="section-label">Describe what you\'re trying to understand <span style="font-weight:400;text-transform:none;">(optional)</span></p>', unsafe_allow_html=True)
    description = st.text_area("Description", value=st.session_state.search_desc,
        placeholder="e.g. I need to track carrier delivery delays by region ahead of a logistics review...",
        height=100, label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔍  Find reports", type="primary"):
        st.session_state.search_dept = selected_depts
        st.session_state.search_type = selected_types
        st.session_state.search_desc = description
        st.session_state.followup_answer = None

        # Decide if follow-up is needed
        needs_followup = (
            len(description.strip()) < 15
            and len(selected_depts) == 1
            and selected_depts[0] in FOLLOWUP_QUESTIONS
        )
        if needs_followup:
            st.session_state.show_followup = True
            st.session_state.screen = "followup"
        else:
            st.session_state.show_followup = False
            st.session_state.results = match_reports(selected_depts, selected_types, description)
            st.session_state.screen = "results"
        st.rerun()

# ─────────────────────────────────────────────
# SCREEN: FOLLOW-UP
# ─────────────────────────────────────────────
def screen_followup():
    if st.button("← Back"):
        st.session_state.screen = "search"
        st.rerun()

    dept = st.session_state.search_dept[0]
    fu = FOLLOWUP_QUESTIONS[dept]

    st.markdown("### 🤔 One quick question before showing results")
    st.markdown(f'<div class="followup-box"><strong>{fu["question"]}</strong></div>', unsafe_allow_html=True)

    choice = st.radio("Select the option that best fits:", fu["options"], index=None, label_visibility="collapsed")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Show results →", type="primary"):
            st.session_state.followup_answer = choice
            # Add follow-up keywords to search
            extra_kw = fu["keyword_map"].get(choice, []) if choice else []
            st.session_state.results = match_reports(
                st.session_state.search_dept,
                st.session_state.search_type,
                st.session_state.search_desc,
                followup_keywords=extra_kw
            )
            st.session_state.screen = "results"
            st.rerun()
    with col2:
        if st.button("Skip, show all matches"):
            st.session_state.results = match_reports(
                st.session_state.search_dept,
                st.session_state.search_type,
                st.session_state.search_desc
            )
            st.session_state.screen = "results"
            st.rerun()

# ─────────────────────────────────────────────
# SCREEN: RESULTS
# ─────────────────────────────────────────────
def screen_results():
    if st.button("← Refine search"):
        st.session_state.screen = "search"
        st.rerun()

    results = st.session_state.results
    filters = ", ".join(st.session_state.search_dept + st.session_state.search_type) or "All"

    # Show follow-up answer if used
    if st.session_state.followup_answer:
        st.info(f"🎯 Refined by your answer: *\"{st.session_state.followup_answer}\"*")

    if results:
        max_score = results[0][1] if results else 1
        st.markdown(f"**{len(results)} report(s) matched** · Filters: {filters}")
        st.markdown("<br>", unsafe_allow_html=True)
        for rank, (report, score, match_reason) in enumerate(results):
            render_card(report, score, match_reason, rank, max_score)
    else:
        st.warning("No reports matched your filters. Try broadening your selection or submit a new request below.")

    st.markdown('<div class="no-match-box">', unsafe_allow_html=True)
    st.markdown("### 🙋 None of these fit your need?")
    st.markdown("Submit a request and the BI team will review it within 2 business days.")
    if st.button("Request a new report →", type="primary"):
        st.session_state.screen = "request"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SCREEN: DASHBOARD / ANALYTICS
# ─────────────────────────────────────────────
def screen_dashboard():
    import pandas as pd

    if st.button("← Back to catalog"):
        st.session_state.screen = "search"
        st.rerun()

    st.title("📈 Catalog analytics")
    st.markdown("A snapshot of what's in the catalog today.")
    st.markdown("---")

    df = pd.DataFrame(REPORTS)

    # Top metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total reports", len(REPORTS))
    col2.metric("Departments covered", df["department"].nunique())
    col3.metric("SSRS reports", len(df[df["report_type"] == "SSRS"]))
    col4.metric("C-Reports", len(df[df["report_type"] == "C-Report"]))

    st.markdown("---")

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("**Reports by department**")
        dept_counts = df["department"].value_counts().reset_index()
        dept_counts.columns = ["Department", "Count"]
        st.bar_chart(dept_counts.set_index("Department"))

    with col_right:
        st.markdown("**Reports by type**")
        type_counts = df["report_type"].value_counts().reset_index()
        type_counts.columns = ["Type", "Count"]
        st.bar_chart(type_counts.set_index("Type"))

    st.markdown("---")
    st.markdown("**Reports by refresh frequency**")
    freq_counts = df["frequency"].value_counts().reset_index()
    freq_counts.columns = ["Frequency", "Count"]
    st.bar_chart(freq_counts.set_index("Frequency"))

    st.markdown("---")
    st.markdown("**Full report catalog**")
    display_cols = ["name", "department", "report_type", "frequency", "owner_name"]
    st.dataframe(
        df[display_cols].rename(columns={
            "name": "Report name",
            "department": "Department",
            "report_type": "Type",
            "frequency": "Frequency",
            "owner_name": "Owner"
        }),
        use_container_width=True,
        hide_index=True
    )

# ─────────────────────────────────────────────
# SCREEN: ACCESS REQUEST
# ─────────────────────────────────────────────
def screen_access():
    if st.button("← Back to results"):
        st.session_state.screen = "results"
        st.rerun()

    report = st.session_state.get("access_report", {})
    st.subheader("🔑 Request access")
    st.markdown(f"**{report.get('owner_name', '')}** will be notified to grant you access to **{report.get('name', '')}**.")
    st.markdown("---")

    with st.form("access_form"):
        st.text_input("Report", value=report.get("name", ""), disabled=True)
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        dept = st.selectbox("Your department", DEPARTMENTS)
        reason = st.text_area("Brief reason for access (optional)", height=80)
        if st.form_submit_button("Submit request", type="primary"):
            if not name or not email:
                st.error("Please provide your name and email.")
            else:
                st.session_state.screen = "access_confirm"
                st.session_state.access_name = name
                st.rerun()

# ─────────────────────────────────────────────
# SCREEN: NEW REPORT REQUEST
# ─────────────────────────────────────────────
def screen_request():
    if st.button("← Back to results"):
        st.session_state.screen = "results"
        st.rerun()

    st.subheader("📝 Request a new report")
    st.markdown("We've pre-filled your search context. Add detail and submit — the BI team will follow up within 2 business days.")
    st.markdown("---")

    with st.form("request_form"):
        dept_index = DEPARTMENTS.index(st.session_state.search_dept[0]) if st.session_state.search_dept else 0
        dept = st.selectbox("Your department", DEPARTMENTS, index=dept_index)
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        need = st.text_area("What do you need to understand?", value=st.session_state.search_desc, height=100)
        decision = st.text_area("What decision will this report support?",
            placeholder="e.g. Deciding which carriers to renegotiate contracts with...", height=80)
        metrics = st.text_area("Key metrics or data points you need",
            placeholder="e.g. Revenue, TEU volume, yield per TEU...", height=80)
        frequency = st.selectbox("How often do you need it?", FREQUENCIES)
        report_type = st.selectbox("Report type preference", ["No preference"] + REPORT_TYPES)

        if st.form_submit_button("Submit request", type="primary"):
            if not name or not email or not need:
                st.error("Please fill in your name, email, and what you need.")
            else:
                st.session_state.screen = "confirm"
                st.session_state.request_name = name
                st.rerun()

# ─────────────────────────────────────────────
# CONFIRMATION SCREENS
# ─────────────────────────────────────────────
def screen_access_confirm():
    report = st.session_state.get("access_report", {})
    st.success("✅ Access request sent!")
    st.markdown(f"**{report.get('owner_name', 'The report owner')}** has been notified and will grant access shortly.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back to results"):
            st.session_state.screen = "results"
            st.rerun()
    with col2:
        if st.button("Back to catalog"):
            st.session_state.screen = "search"
            st.rerun()

def screen_confirm():
    st.success("✅ Request submitted!")
    st.markdown("The BI team will review your request and follow up within **2 business days**.")
    if st.button("Back to catalog"):
        st.session_state.screen = "search"
        st.rerun()

# ─────────────────────────────────────────────
# ROUTER
# ─────────────────────────────────────────────
screen = st.session_state.screen
if screen == "search":           screen_search()
elif screen == "followup":       screen_followup()
elif screen == "results":        screen_results()
elif screen == "dashboard":      screen_dashboard()
elif screen == "access":         screen_access()
elif screen == "access_confirm": screen_access_confirm()
elif screen == "request":        screen_request()
elif screen == "confirm":        screen_confirm()
