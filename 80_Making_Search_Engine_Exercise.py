def MathingWords(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score

if __name__ == "__main__":

    sentences = ["I am Saad", "Python is very strong Language", "Python is good", "My Nick Name is Saadi"                                                                                  "I am not intelligent",
                 "I am Study at UCP", "University of Central Punjab"]

    query = input("Search Here: ")
    scores = [MathingWords(query, sentence) for sentence in sentences]

    # print(scores)
    sortedSentScore = [sentScore for sentScore in sorted(
        zip(scores, sentences), reverse=True) if sentScore[0] !=0 ]
    # print(sortedSentScore)

    print(f"{len(sortedSentScore)} results found!")
    for score, item in sortedSentScore:
        print(f" \"{item}\": with a score of {score}")