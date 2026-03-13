from google import genai
import time

def calculate_risk_score(company_name, financial_data, internal_flags, external_flags, officer_notes):
    """Calculates the 0-10 risk score based on all gathered data."""
    
    client = genai.Client(api_key="AIzaSyCjjJQlPaOYWzpjC_BlBOgnji5lcCNodYI")
    
    prompt = f"""
    You are the Chief Risk Officer evaluating {company_name}. 
    Review the following evidence:
    - Financials: {financial_data}
    - Internal Audit Flags: {internal_flags}
    - External Watchlist Flags: {external_flags}
    - Officer Notes: {officer_notes}
    
    Provide a strict score from 0 to 10 (where 10 is perfectly safe and 0 is massive fraud/risk) for these five categories:
    1. Financial Performance
    2. Promoter Credibility
    3. Industry Outlook
    4. Legal Risk
    5. Operational Observations
    
    Then, calculate and output the FINAL AVERAGE SCORE. Format this clearly so the math is easy to read.
    """
    
    # Auto-retry loop to beat the 503 traffic!
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model='gemini-3-flash-preview',
                contents=prompt
            )
            return response.text
        except Exception as e:
            if attempt == 2:
                return f"❌ Error calculating score after 3 attempts: {str(e)}"
            time.sleep(2)