import google.generativeai as genai
genai.configure(api_key="AIzaSyDAkrrhCiN1KiytH-uOwbB06rbhcYPwrLQ")

for m in genai.list_models():
    print(m.name)
