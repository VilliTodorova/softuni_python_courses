def find_palindromes(initial_string, searched_palindrome):
    palindromes = [palindrome for palindrome in initial_string if palindrome == ''.join(reversed(palindrome))]
    count = palindromes.count(searched_palindrome)
    return palindromes, count


initial_string = input().split()
searched_palindrome = input()
results = find_palindromes(initial_string, searched_palindrome)

print(results[0])
print(f'Found palindrome {results[1]} times')
