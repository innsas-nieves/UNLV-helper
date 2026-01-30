import streamlit as st

st.set_page_config(page_title="Internal IT AI Helper (Prototype)", layout="wide")

st.title("Internal IT AI Helper")
st.caption("Prototype UI for exploring inputs that improve retrieval and routing. Not a ticketing system.")

# ---- Layout ----
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Describe the issue")

    problem_description = st.text_area(
        "What’s going on?",
        placeholder="What are you trying to do? What’s not working? Any error messages?",
        height=150
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

    impact = st.radio(
        "Impact",
        ["Blocking work", "Workaround exists", "General question"],
        horizontal=True
    )

    include_screenshot = st.checkbox("Upload a screenshot for context (optional)")

    if include_screenshot:
        screenshot = st.file_uploader(
            "Screenshot (internal context only)",
            type=["png", "jpg", "jpeg"]
        )

    analyze = st.button("Analyze and suggest")

# ---- Output / Mocked AI Response ----
with col2:
    st.subheader("AI-assisted suggestions")

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
        st.write("Instructional Technology → Media Systems")

        st.markdown("**Notes**")
        st.write(
            "Based on the selected service and task intent, this appears to be a common access or configuration issue."
        )

    else:
        st.info("Fill out the fields on the left and click **Analyze and suggest**.")

# ---- Ticket Handoff ----
st.divider()

st.subheader("Next step")
st.caption("This does not create a ticket.")

st.button("Create ticket in TDX (not wired)")
st.caption(
    "This would pass a clean summary, suggested routing, and metadata to TDX/Salesforce."
)
