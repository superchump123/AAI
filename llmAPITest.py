import google.generativeai as genai

genai.configure(api_key="AIzaSyAA2A1hw9FtphJpX3fDm1Co4_lS4BLIR_U")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Recommend me a alcaholic drink that coffee drinkers would like")
print(response.text)
print("HELLO KAI")