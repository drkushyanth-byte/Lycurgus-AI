from google import genai
def check_external_watchlists(company_name):
    """Checks the company against global and local fraud databases."""
    
    # Initialize the new client (Paste your actual key here!)
    client = genai.Client(api_key="AIzaSyCSEuPu4yAIvjvRxgUO1G9rTLBaJTcq8e4")
    
    prompt = f"""
    You are an elite Corporate Due Diligence Investigator. 
    Investigate the company '{company_name}' for any history of corporate fraud, scams, or regulatory violations.
    
    Cross-reference your knowledge of this company against the following watchlists:
    1. FBI Corporate Fraud database
    2. SEC Litigation Releases
    3. DOJ Foreign Corrupt Practices Act (FCPA)
    4. RBI Defaulters & Bulletins (India)
    5. SEBI Enforcement actions (India)
    6. MCA Global (India)
    7. World Bank Sanctions
    8. OECD Anti-Bribery
    
    Output a short summary of any red flags. If none exist, state 'No major red flags found in these databases.'
    At the very end, provide an EXTERNAL RISK SCORE from 0 (perfectly clean) to 10 (massive fraud/sanctions).
    """
    
    try:
        
        response = client.models.generate_content(
            model='gemini-3-flash-preview',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"❌ Error checking external sources: {str(e)}"