import streamlit as st
import concurrent.futures
import internal_risk
import external_risk
import scoring_system
import decision_engine

st.set_page_config(page_title="Lycurgus AI", page_icon="🏛️", layout="wide")
st.title("🏛️ Lycurgus AI - Credit Appraisal Agent")
st.markdown("Automated fraud detection, risk scoring, and loan decisioning.")

col1, col2 = st.columns(2)
with col1:
    company_name = st.text_input("🏢 Company Name")
    financial_data = st.text_area("📊 Paste Financial Data (Revenue, Cash Flow, GST, etc.)", height=150)
with col2:
    officer_notes = st.text_area("📝 Credit Officer Observations", height=150)

if st.button("Generate Lycurgus AI Report", use_container_width=True):
    if not company_name or not financial_data:
        st.error("❌ Please enter a Company Name and Financial Data.")
    else:
        st.info(f"Lycurgus AI is auditing {company_name}... Running background checks concurrently!")
        
        # MASSIVE SPEED BOOST: Running Step 1 and 2 at the exact same time!
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_internal = executor.submit(internal_risk.check_internal_fraud, financial_data)
            future_external = executor.submit(external_risk.check_external_watchlists, company_name)
            
            st.warning("⏳ Steps 1 & 2: Running Internal & External Checks simultaneously...")
            
            # Wait for both to finish and grab their results
            internal_flags = future_internal.result()
            external_flags = future_external.result()
            
        st.success("✅ Steps 1 & 2 Complete!")
        
        st.warning("⏳ Step 3: Calculating Risk Score...")
        risk_score_report = scoring_system.calculate_risk_score(
            company_name, financial_data, internal_flags, external_flags, officer_notes
        )
        st.success("✅ Step 3 Complete!")
        
        st.warning("⏳ Step 4: Generating Final Decision...")
        final_decision = decision_engine.generate_decision(
            company_name, financial_data, risk_score_report
        )
        st.success("✅ Step 4 Complete!")

        
        
        # Display Results
        st.header("✅ Lycurgus AI Audit Complete!")
        
        st.subheader("🔍 Internal Fraud Analysis")
        st.info(internal_flags)
        
        st.subheader("🌍 Global Watchlist Analysis")
        st.warning(external_flags)
        
        st.subheader("⚖️ Risk Scoring")
        st.markdown(risk_score_report)
        
        st.subheader("💰 Final Loan Decision")
        st.markdown(final_decision)