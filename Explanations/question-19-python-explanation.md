Aasan zuban mein samajhte hain, bilkul tension na lo!

Graph ko aap **cities (shehar)** aur **roads (sadkon)** ki tarah samjho:

* `1`, `2`, aur `3` teen alag alag shehar hain.
* Har pair jaise `(1, 2)` ka matlab hai: **Shehar 1 aur Shehar 2 ke darmiyan ek road hai.**

Aapko yeh list di gayi hai:
`[(1, 2), (2, 3), (1, 3)]`

---

### Step by Step Road Map Dekhein:

1. **Pehli road: `(1, 2)**`
* Iska matlab: `1` se road ja rahi hai `2` ko.


2. **Dusri road: `(2, 3)**`
* Iska matlab: `2` se road ja rahi hai `3` ko.


3. **Teesri road: `(1, 3)**`
* Iska matlab: `1` se ek aur direct road ja rahi hai `3` ko!



---

### Ab "Node 1" Par Khare Ho Kar Socho:

Agar aap shehar `1` par kharay ho, aur dekhna chahte ho ke aap yahan se **seedha (directly)** kahan kahan ja sakte ho:

* Road `(1, 2)` ke zariye aap **`2`** ja sakte ho.
* Road `(1, 3)` ke zariye aap **`3`** ja sakte ho.

Toh `1` ke padosi (neighbors) kaun huay? **`2` aur `3**`.
Isi liye dictionary mein `1` ke samne list aayegi: `1: [2, 3]`

---

### Graph Traversal Kya Cheez Hai?

Traversal ka matlab hota hai **"safar karna"** ya **"har jagah ghoomna"**.

Agar aapko computer ko bolna ho ke *"Shehar 1 se chal kar Shehar 3 tak ka rasta dhoondo"*, toh computer ko har shehar ke samne uske connected sheharon ki list chahiye hoti hai taake wo foran dekh sake ke agla qadam kahan lena hai.

Aapka kaam sirf yeh phone directory jaisi dictionary banana hai:

```python
{
    1: [2, 3],  # 1 se 2 aur 3 ja sakte hain
    2: [3],     # 2 se 3 ja sakte hain
    # (agar two-way road ho toh 2 se 1 aur 3 dono)
}

```

Ab baat clear hui?



Bilkul 100% sahi pakde hain!

Computer ke liye raw edges par kaam karna buhat slow hota hai. Adjacency list bana kar hum computer ko ek **quick lookup map** 
de dete hain taake traversal (jaise GPS ka shortest route dhoondna ya social network mein mutual friends nikalna) $O(1)$ fast ho jaye.

Ab is logic ko code mein convert karke dekhein.

### Python ke liye Hints:

* Input: `edges = [(1, 2), (2, 3), (1, 3)]`
* Har pair `(u, v)` ko loop karein.
* Har key ke samne ek list honi chahiye.
* `defaultdict(list)` ya `.setdefault()` use karke code bohot clean ho jata hai.

Agar two-way (undirected) road consider karein:

* `u` ki list mein `v` ko append karein.
* `v` ki list mein `u` ko append karein.

Isko Python mein implement karke try karein!