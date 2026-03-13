from google import genai
import time  # We need this to pause between retries [1]

def generate_decision(company_name, financial_data, risk_score):
    """Calculates final loan amount and interest rate based on the risk score."""
    
    client = genai.Client(api_key="AIzaSyBkhoXXCQrnlpsPA-Q-O753guftWdV_iXk")
    
    prompt = f"""
    You are the Final Approving Authority for a corporate loan to {company_name}.
    
    DATA:
    - Financials: {financial_data}
    - Final Risk Score (out of 10): {risk_score}
    
    APPLY THESE EXACT BANKING RULES:
    1. Find the "Cash Flow" in the financials.
    2. Calculate Max Safe Loan: Cash Flow / 1.5
    3. Calculate Final Loan: Max Safe Loan * ({risk_score} / 10)
    4. Calculate Interest Rate: Base rate is 6%. 
       - If Risk Score is 9 to 10: Add +1%
       - If Risk Score is 7 to 8.9: Add +2%
       - If Risk Score is 5 to 6.9: Add +4%
       - If Risk Score is < 5: REJECT the loan entirely.
    
    OUTPUT FORMAT (Markdown):
    - **Final Decision:** (Approve / Reject)
    - **Max Safe Loan capacity:** [Amount]
    - **Approved Final Loan:** [Amount]
    - **Approved Interest Rate:** [Rate]%
    - **Justification:** Briefly explain the math.
    """
    
    # Try up to 3 times before giving up [1]
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model='gemini-3-flash-preview',
                contents=prompt
            )
            return response.text
        except Exception as e:
            if attempt == 2:  # If it fails on the 3rd try, show the error
                return f"❌ Error generating decision after 3 attempts: {str(e)}"
            time.sleep(2)  # Take a 2-second breather before retrying [1]