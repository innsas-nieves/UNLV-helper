import streamlit as st

# ---- Page config ----
st.set_page_config(
    page_title="UNLV IT – Internal AI Helper (Prototype)",
    layout="wide"
)

# ---- UNLV IT branding ----
st.markdown(
    """
    <style>
        .unlv-header {
            color: #B10202; /* UNLV Red */
            font-weight: 700;
        }
        .unlv-subtext {
            color: #5A5A5A; /* UNLV Gray */
            font-size: 0.95rem;
        }
        .section-header {
            color: #5A5A5A;
            font-weight: 600;
            margin-top: 1rem;
        }
        .step-box {
            background-color: #F7F7F7;
            border-left: 4px solid #B10202;
            padding: 1rem;
            margin-top: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='unlv-header'>UNLV IT – Internal AI Helper</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='unlv-subtext'>Prototype tool for internal IT use to explore what information helps guide troubleshooting and escalation. Not a ticketing system.</p>",
    unsafe_allow_html=True
)

# ---- Layout ----
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<h3 class='section-header'>Describe the issue</h3>", unsafe_allow_html=True)

    problem_description = st.text_area(
        label="",
        placeholder=(
            "Include relevant keywords, exact error messages, system names, feature labels, "
            "or UI text if available. Specific details help surface better troubleshooting steps."
        ),
        height=180
    )

    affected_service = st.selectbox(
        "Affected service / tool",
        [
            "Select one",
            "Zoom",
            "Panopto",
            "Canvas / WebCampus",
            "Email / Google Workspace",
            "VPN",
            "AI tools",
            "Other / Not sure"
        ]
    )

    user_role = st.selectbox(
        "User role / affiliation",
        [
            "Select one",
            "Faculty",
            "Staff",
            "Student",
            "Researcher",
            "IT staff",
            "Admin / Leadership"
        ]
    )

    issue_category = st.selectbox(
        "Issue category",
        [
            "Select one",
            "Access / permissions",
            "Error or system failure",
            "How-to / workflow",
            "Integration issue",
            "Policy or compliance",
            "Possible outage"
        ]
    )

    task_intent = st.text_input(
        "What is the user trying to accomplish?",
        placeholder="e.g., record a lecture, share a video, schedule a meeting"
    )

    include_screenshot = st.checkbox("Upload a screenshot for context (optional)")

    if include_screenshot:
        st.file_uploader(
            "Screenshot (internal context only)",
            type=["png", "jpg", "jpeg"]
        )

    analyze = st.button("Analyze and review troubleshooting steps")

with col2:
    st.markdown("<h3 class='section-header'>Guided review</h3>", unsafe_allow_html=True)

    if analyze:
        # Step 1
        st.markdown("**Step 1: Review likely troubleshooting steps**")

        st.markdown(
            """
            <div class="step-box">
                <strong>Common issue pattern</strong><br>
                """
            + (issue_category if issue_category != "Select one" else "Pattern unclear based on current inputs")
            + """
                <br><br>
                <strong>Relevant documentation to review</strong>
                <ul>
                    <li>Panopto: Recording permissions overview</li>
                    <li>Zoom: Scheduling meetings for others</li>
                    <li>Canvas: Course tool visibility settings</li>
                </ul>
                Try the steps in the documentation above to see if they resolve the issue.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Step 2
        st.markdown("**Step 2: If the issue persists, escalate**")

        st.markdown(
            """
            <div class="step-box">
                If the troubleshooting steps above do not resolve the issue, this would likely be escalated to:
                <br><br>
                <strong>UNLV IT – Instructional Technology (Tier II)</strong>
                <br><br>
                When escalating, include:
                <ul>
                    <li>What you were trying to accomplish</li>
                    <li>What troubleshooting steps were attempted</li>
                    <li>Any error messages or screenshots</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.info("Fill out the fields on the left and click **Analyze and review troubleshooting steps**.")
