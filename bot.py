from chatterbot import ChatBot

def bot():
    chatbot = ChatBot(
        'Norman',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3'
    )

    history = []
    history_dialogue = []
    exit_conditions = ("q", "quit", "sair")

    print("\n\nFinancial Bot 🏦 =======================")
    print("Opções no chat:")
    print(" ▶️ h: para acessar o Histórico.")
    print(" ▶️ sair: para encerrar.")
    print(" ▶️ ajuda: para pedir ajuda ao Bot.\n")
    while True:
        query = input("😀 > ")
        history.append(query)
        history_dialogue.append(query)

        if query.lower() == 'h':
            print("Histórico:")
            i = 0
            for ask in history:
                print(f" {i}. {ask}")
                i += 1
            continue
        
        if query.lower() in exit_conditions:
            print(f"   🤖 Adeus 👋")
            break
        else:
            response = chatbot.get_response(query)
            history_dialogue.append(response)

            print(f"   🤖 {response}")
    
    with open("history_dialogue.txt", "+w") as file:
        for line in history_dialogue:
            file.write(str(f"{line}\n"))

if __name__ == "__main__":
    bot()