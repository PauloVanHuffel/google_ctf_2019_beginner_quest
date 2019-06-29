from bs4 import BeautifulSoup

import requests


def get_palingdrome_primes(page_num, num_needed):
    palings = []
    while len(palings) < num_needed:
        url = "https://www.bigprimes.net/archive/prime/" + str(page_num) + "/"

        r  = requests.get(url)

        data = r.text

        soup = BeautifulSoup(data, "lxml")

        for link in soup.find_all('a'):
            link_text = link.get('href')
            if "cruncher" in link_text:
                number = link_text.split("cruncher/")[1].replace("/" , "")
                if number and str(number) == str(number)[::-1]:
                    palings.append(number)
        page_num += 1

    return palings


def extend_word(to_solve, palingdrome_primes):
    result = ""
    for i, solv in enumerate(to_solve):
        try:
            result += chr(solv ^ int(palingdrome_primes[i]))
        except:
            result += "." # in 2 cases it seems to fail. The end string is still easily guessable though
    return result
    
def main(): 
    solution = ""
    
    #find the page that has the prime numbers closely before to the first to solve number manualy 
    first_set_page_nums = 6594 
    to_solve = [9916239, 9918082, 9919154, 9921394, 9923213, 9926376, 9927388, 9931494, 9932289, 9935427, 9938304, 9957564, 9965794, 9978842, 9980815, 9981858, 9989997] # first set of numbers, botom to top from the program 
    palingdrome_primes = get_palingdrome_primes(first_set_page_nums, len(to_solve))
    solution += extend_word(to_solve, palingdrome_primes)
    second_set_page_nums = 57631 # there is a *100 size increase in the solve numbers 
    to_solve = [100030045, 100049982, 100059926, 100111100, 100131019, 100160922, 100404094, 100656111, 100707036, 100767085, 100887990, 100998966, 101030055, 101060206, 101141058]
    palingdrome_primes = get_palingdrome_primes(second_set_page_nums, len(to_solve))
    solution += extend_word(to_solve, palingdrome_primes)
    print(solution)


if __name__ == '__main__':
    main()
