import re
text = "The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs away."
pattern = r"fox"
match = re.search(pattern, text)
if match:
    print("Found a match:", match.group())
else:
    print("No match found")
all_matches = re.findall(pattern, text)
if all_matches:
    print("All matches:", all_matches)
else:
    print("No matches found")
match_iterator = re.finditer(pattern, text)
for match in match_iterator:
    print("Match found at index:", match.start())
pattern = r"the"
all_matches = re.findall(pattern, text, re.IGNORECASE)
print("Case-insensitive matches:", all_matches)
