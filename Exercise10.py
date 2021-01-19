tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
fat_cat2 = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
all_cats = tabby_cat + persian_cat + backslash_cat + fat_cat + fat_cat2
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(all_cats, end = " ")