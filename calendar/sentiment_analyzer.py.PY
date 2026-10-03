from textblob import TextBlob

def analyze_sentiment(text):
    # تحلیل متن ورودی
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # عددی بین -1 تا +1

    print("\n" + "=" * 40)
    print(f"📝 Text: {text}")
    
    if polarity > 0.1:
        sentiment = "😊 Positive (مثبت)"
    elif polarity < -0.1:
        sentiment = "😡 Negative (منفی)"
    else:
        sentiment = "😐 Neutral (خنثی)"

    # محاسبه امتیاز به درصد
    score = round((polarity + 1) * 50, 2)
    print(f"🔍 Result: {sentiment}")
    print(f"📊 Positivity Score: {score}%")
    print("=" * 40 + "\n")

print("✨ AI Sentiment Analyzer is ready! (type 'exit' to quit) ✨")

while True:
    user_input = input("Enter an English sentence: ")
    if user_input.lower() == 'exit':
        print("Goodbye! 👋")
        break
    if user_input.strip():
        analyze_sentiment(user_input)
