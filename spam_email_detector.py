spam_words = ["free", "win", "winner", "cash", "prize", "money", "deal", "discount",
    "offer", "gift", "bonus", "trial", "lifetime", "access", "click", "buy",
    "order", "cheap", "promo", "best", "price", "shop", "now", "save",
    "voucher", "coupon", "exclusive", "giveaway", "winning", "selected",
    "investment", "crypto", "bitcoin", "profit", "earn", "income", "credit",
    "loan", "debt", "interest", "rate", "guarantee", "risk-free", "million",
    "billion", "wealth", "payment", "transfer", "deposit", "withdraw",
    "refund", "transaction", "wallet", "inheritance", "beneficiary",
    "verify", "account", "suspended", "blocked", "restricted", "compromised",
    "unauthorized", "login", "password", "username", "update", "confirm",
    "security", "alert", "fraud", "identity", "audit", "investigation",
    "urgent", "immediate", "action", "required", "expire", "termination",
    "warrant", "arrest", "legal", "lawsuit", "police", "irs", "tax",
    "government", "claim", "final", "notice", "warning", "critical",
    "failure", "limit", "deadline", "attention"]
def check_spam(text):
    score = 0
    words = text.lower().split()
    found_words = []
    for word in words:
        if word in spam_words:
            score = score + 1
            found_words.append(word)
    return score, found_words
def main():
    print("Welcome to my Spam Detection Project")
    print("Type exit to close the program")
    while True:
        user_input = input("\nEnter your message here: ")
        if user_input == "exit":
            print("See you later!")
            break
        if len(user_input) == 0:
            print("You didn't type anything. Please try again.")
            continue
        risk_score, detected_keywords = check_spam(user_input)
        print("Bad words found:", detected_keywords)
        print("Total Risk Score:", risk_score)
        if risk_score >= 3:
            print("Result: DANGER! This looks like a Scam.")
        elif risk_score >= 1:
            print("Result: WARNING. Be careful with this message.")
        else:
            print("Result: SAFE. This message looks okay.")
if __name__ == "__main__":
    main()