import pandas as pd

def extract_text(uploaded_file):
    """Extracts text or data from the uploaded financial/GST file."""
    if uploaded_file is None:
        return "No financial documents uploaded. Proceeding with basic info."

    try:
        # Handle CSV files
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            return f"Extracted Financial Data:\n{df.to_string()}"
            
        # Handle plain text files
        elif uploaded_file.name.endswith('.txt'):
            return f"Extracted Document Text:\n{uploaded_file.read().decode('utf-8')}"
            
        else:
            return "Unsupported file format. Please upload .txt or .csv for the demo."
            
    except Exception as e:
        return f"Error reading file: {str(e)}"