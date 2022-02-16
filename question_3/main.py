'''
Developer: Carlos Acácio de Campos Júnior
LinkedIn: https://www.linkedin.com/in/carlos-campos-a0486a11b/
GitHub: https://github.com/Carlos6654
Instagram: https://www.instagram.com/carlos_camposjr/


### Question 3 ###

Steps:
0 - palavra de entrada: 'ifailuhkqq'
1 - fatiar a palavra para identificar pares: i,f,a,i,l,u,h,k,q,q
    verificar anagramas pares: [i,i] e [q,q] = 2
2 - Adicionar letra: if, fa, ai, il, lu, uh, hk, kq, qq
    verificar anagramas pares: ---
3 - Adicionar letra: ifa, fai, ail, ilu, luh, uhk, hkq, kqq
    verificar anagramas pares: [ifa, fai] = 1
4 - ...
5 - Saída: 2+1 = 3
'''

if __name__ == '__main__':
    try:
        word = input("Enter a word to identify anagrams: ")
        anagrams_found = 0

        def is_anagram(sub_string1, sub_string2):
            list1 = list(sub_string1)
            list1.sort()
            list2 = list(sub_string2)
            list2.sort()
            if list1 == list2:
                return True
            return False

        for i in range(1, len(word)):  # character number for each substring
            anagrams_list = []
            for j in range(0, len(word)):  # Creating anagrams
                substring = word[j:j+i]
                if len(substring) == i:
                    anagrams_list.append(substring)

            for p in range(0, len(anagrams_list)):  # Verifying anagram pairs
                for q in range(p+1, len(anagrams_list)):
                    if is_anagram(anagrams_list[p], anagrams_list[q]):
                        anagrams_found += 1

        print(anagrams_found)

    except Exception as e:
        print(f'Error while running. Message: {e}')
