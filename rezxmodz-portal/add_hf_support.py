with open('C:/Users/hs792/.gemini/antigravity/scratch/rezxmodz-portal/server.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    "('trycloudflare', 'netlify', 'onrender', 'koyeb', 'pages.dev', 'app')",
    "('trycloudflare', 'netlify', 'onrender', 'koyeb', 'pages.dev', 'app', 'hf.space', 'huggingface.co')"
)

with open('C:/Users/hs792/.gemini/antigravity/scratch/rezxmodz-portal/server.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Added hf.space support to server.py!")
