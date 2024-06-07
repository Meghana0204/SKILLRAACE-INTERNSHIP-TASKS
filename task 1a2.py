import demoji

# Sample text with emojis
text = "I love Python 😊 and coding 💻"

# Convert emojis to their descriptions
text_with_descriptions = demoji.replace_with_desc(text)

print(text_with_descriptions)
