def longest(word_set, cache, word):
    if word not in cache:
        ret = 1
        for i in xrange(len(word)):
            w = word[:i] + word[i+1:]
            if w and w in word_set:
                cnt = longest(word_set, cache, w)
                ret = max(ret, 1 + cnt)

        cache[word] = ret

    return cache[word]


def longestChain(words):
    cache = {}
    word_set = set(words)
    gmax = 0
    for word in words:
        gmax = max(gmax, longest(word_set, cache, word))

    return gmax


if __name__ == "__main__":
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    assert longestChain(words) == 4


