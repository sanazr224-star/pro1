height = int(input("height: "))
for i in range(1, height + 1):
        left_spaces = height - i
        left_blocks=i
        right_block=i

        print(" " *left_spaces + "۲" * left_blocks + "    " + "۲" * right_block )

              