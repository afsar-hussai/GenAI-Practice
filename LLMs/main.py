import tiktoken

enc=tiktoken.encoding_for_model("gpt-4o")
text = "tiktoken is great!"

tokens=enc.encode(text)

print("tokens are: ",tokens)

decoded_text=enc.decode(tokens)

print("Decoded Text is: ",decoded_text)