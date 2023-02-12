p, b, g, e = list(input())
text = ""
while s := input():
    text += "\n" + s

p_dict, e_dict = {}, {}
text = text.split()
for idx, word in enumerate(text):
    if word and word[-1] == e and word[0] == g:
        e_dict.setdefault(word, 0)
        e_dict[word] += 1
    if word and idx and word[0] == b and text[idx-1][-1] == p:
        p_dict.setdefault(word, 0)
        p_dict[word] += 1

ans = [max(p_dict, key=lambda x: p_dict[x], default=""), max(e_dict, key=lambda x: e_dict[x], default="")]
ans[0] = (ans[0], p_dict[ans[0]]) if ans[0] else ("...", 0)
ans[1] = (ans[1], e_dict[ans[1]]) if ans[1] else ("...", 0)
print(*ans[0], "-", *ans[1])
