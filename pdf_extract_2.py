import re
import pandas as pd
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams

def extract_text_from_pdfs(docs):
    text = ""
    for doc in docs:
        try:
            extracted_text = extract_text(doc, laparams=LAParams()) 
            text += extracted_text
        except Exception as e:
            print(f"Error processing {doc}: {e}")
    return text

def parse_transactions(text):
    transaction_pattern = re.compile(r'(\d{2}-[A-Za-z]{3}-\d{4})\s+(.+?)\s+([\d,]+\.\d{2})\s*(Dr|Cr)?', re.MULTILINE)

    transactions = []
    last_type = ""  

    for match in transaction_pattern.finditer(text):
        date, description, amount, transaction_type = match.groups()
        if transaction_type:  
            last_type = transaction_type  
        else:
            transaction_type = last_type 

        transactions.append([date, description.strip(), amount, transaction_type])

    return transactions

def save_to_excel(transactions, output_file):
    df = pd.DataFrame(transactions, columns=["Date", "Description", "Amount", "Type"])
    df.to_excel(output_file, index=False)
    print(f"Transactions saved to {output_file}")


docs = ['test3_(1).pdf']
all_text = extract_text_from_pdfs(docs)


with open('extracted_pdf/extracted_text.txt', 'w', encoding='utf-8') as f:
    f.write(all_text)
print("Text extracted and saved to extracted_text.txt")


transactions = parse_transactions(all_text)


output_excel = "extracted_pdf/extracted_transactions.xlsx"
save_to_excel(transactions, output_excel)
