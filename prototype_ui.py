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
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='unlv-header'>UNLV IT – Internal AI Helper</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='unlv-subtext'>Prototype tool for internal IT use to explore documentation, troubleshoot issues, and suggest routing. Not a ticketing system.</p>",
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
            "or UI text if available. Specific details help surface better documentation and next steps."
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

    analyze = st.button("Analyze and suggest")

with col2:
    st.markdown("<h3 class='section-header'>AI-assisted suggestions</h3>", unsafe_allow_html=True)

    if analyze:
        st.markdown("**Likely issue type**")
        st.write(issue_category if issue_category != "Select one" else "Needs clarification")

        st.markdown("**Relevant documentation**")
        st.write(
            "- Panopto: Recording permissions overview\n"
            "- Zoom: Scheduling meetings for others\n"
            "- Canvas: Course tool visibility settings"
        )

        st.markdown("**Suggested routing**")
        st.write("UNLV IT → Instructional Technology")

        st.markdown("**Notes**")
        st.write(
            "Based on the selected service and task intent, this appears to be a common configuration or access-related issue."
        )
    else:
        st.info("Fill out the fields on the left and click **Analyze and suggest**.")

# ---- Ticket handoff (explicitly non-functional) ----
st.divider()

st.markdown("<h3 class='section-header'>Next step</h3>", unsafe_allow_html=True)
st.markdown(
    "<p class='unlv-subtext'>This prototype does not create a ticket. "
    "In a future state, a clean summary and suggested routing could be passed to TDX or Salesforce.</p>",
    unsafe_allow_html=True
)

st.button("Create ticket (not connected)")
