
#* 1. Implement basic string compression (e.g., "aabcccccaaa" becomes "a2b1c5a3").

# Problem: String Compression (Python #1)
# Pattern: Linear scan + group counting
# Trick: Keep the current char and a count. When the next char differs, save "char+count", then reset.
#        Don't forget to save the last group after the loop.
# Time: O(n) one pass
# Space: O(n) for the result

def compress_str(value):
    if not value:
        return ""
    parts = []    
    count = 1
    curr = value[0]
    for ch in value[1:]:
        if ch == curr:
            count += 1
        else:
            parts.append(f'{curr}{str(count)}')
            count = 1
            curr = ch
   
    parts.append(f'{curr}{str(count)}')
    return "".join(parts)
  
 
print(compress_str("aabcccccaa"))
print(compress_str("ttzzxxttzzxx"))
print(compress_str(""))

