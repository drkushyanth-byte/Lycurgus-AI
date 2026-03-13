from google import genai

def check_internal_fraud(financial_data):
    """Cross-checks uploaded financial data for internal inconsistencies."""
    
   
    client = genai.Client(api_key="AIzaSyCHBEvWa0dqaJfwdlCYgvlKMotpM3N8Clg")
    
    prompt = f"""
    You are an elite Bank Internal Auditor. 
    Review the following extracted financial data:
    
    {financial_data}
    
    Perform the following strict checks:
    1. GST vs Bank Mismatch: Flag if GST sales differ significantly from Bank deposits (possible fake invoices or circular trading).
    2. Abnormal Revenue Growth: Flag any sudden, unrealistic spikes in revenue year-over-year.
    3. Related-Party Transactions: Flag high volumes of suspicious transactions.
    
    Output a short summary of the specific red flags found. If the math checks out, state 'Data appears consistent.'
    At the very end, provide an INTERNAL RISK SCORE from 0 (perfectly clean) to 10 (massive data inconsistencies).
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-3-flash-preview',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"❌ Error checking internal data: {str(e)}"