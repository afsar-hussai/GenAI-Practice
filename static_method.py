class OrderChai:
    @staticmethod
    def print_chai(text):
        return [x.strip() for x in text.split("-")]
    

text2="ginger-garlic-spinach-cold-   heavy-    something-lotsmore   "

result=OrderChai.print_chai(text2)

print(result)