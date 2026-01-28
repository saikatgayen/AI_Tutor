from ollama import chat
from datetime import datetime

print("AI TUITOR")
print("Type 'exit' to quit.\n")

conversation = []                                                  #----Conversation Memory----
max_memory_messages = 6

def save_to_file(question, answer):                              #--------Save Notes----- 
    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 50 + "\n")
        file.write(f"Time: {datetime.now()}\n")
        file.write(f"Question: {question}\n\n")
        file.write(f"Answer:{answer}\n\n")

while True:                                           #------Maiin Loop---------
    question = input("Ask a study question: ")

    if question.lower() == "exit":
        print("Good luck with your studies! ")
        break

						        #---------ADD user question to memory------
    conversation.append({
        "role": "user",
        "content": question
    })

	#send FULL conversation to the model

    response = chat(
        model="llama3",
        messages= conversation
    )

    answer = response["message"]["content"]

	                                                   #----------add AI answer to memory-----------

    conversation.append({
        "role": "assistant",
        "content": answer
    })
								
    if len(conversation) > max_memory_messages:		#--------Memory Mangament---------------
        conversation = conversation[-max_memory_messages:]


    print("\n Answer:\n")
    print(answer)
    print("\n" + "-" * 147 + "\n")

    save_to_file(question, answer)
