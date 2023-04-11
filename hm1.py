with open('1.txt', 'r', encoding='utf-8') as file1:
    a1 = file1.readlines()
    with open('2.txt', 'r', encoding='utf-8') as file2:
        a2 = file2.readlines()
        with open('itog.txt', 'w', encoding='utf-8') as itog:
            if len(a1) < len(a2):
                itog.write('1.txt\n')
                itog.write(str(len(a1)+1))
                itog.write('\n')
                for i in range(len(a1)):
                    itog.write(a1[i])
                itog.write('\n')
                itog.write('2.txt\n')
                itog.write(str(len(a2) + 1))
                itog.write('\n')
                for i in range(len(a2)):
                    itog.write(a2[i])
            else:
                itog.write('2.txt\n')
                itog.write(str(len(a2) + 1))
                itog.write('\n')
                for i in range(len(a2)):
                    itog.write(a2[i])
                itog.write('\n')
                itog.write('1.txt\n')
                itog.write(str(len(a1) + 1))
                itog.write('\n')
                for i in range(len(a1)):
                    itog.write(a1[i])

