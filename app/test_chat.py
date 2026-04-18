from app.chat_engine import generate_answer

query = "Which warehouse currently has inventory shortage?"

answer = generate_answer(query)

print(answer)