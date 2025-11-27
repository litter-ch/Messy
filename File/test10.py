# with open('1.jpeg', 'rb') as from_file:
#     with open('2.jpeg', 'wb') as to_file:
#         from_contents = from_file.read()
#         to_file.write(from_contents)

with open('1.jpeg', 'rb') as from_file, open('2.jpeg', 'wb') as to_file:
    from_contents = from_file.read()
    to_file.write(from_contents)