# program To Find The Most Reputated Charactor in a sentence

sentence = ""
while sentence.lower() != "quit":
    sentence = input("Enter a Sentence to be Sorted : ")
    
    char_frequency = {}
    
    for char in sentence:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    
    char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

    char, times = char_frequency_sorted[0]

    print("The Most Reputed Charactor Is : ", char, "And It Reputed : ", times, "Times")
print("Program End")
