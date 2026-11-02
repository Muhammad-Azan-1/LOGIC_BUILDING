//* 1. Write a function that takes a string and returns the longest word in it.

//? -----
// Big O notation (O) = how the cost grows when the input grows.
// n = the size of the input (characters in a string, items in a list).

// O(...) describes how the cost grows when the input grows, and the “cost” can be two things:
// Time: how many steps the code takes.
// Space: how much extra memory the code uses.

// Time O(n):  steps grow in a straight line with the input.
//             10x bigger input -> about 10x more steps.
// Space O(n): extra memory grows in a straight line with the input.
//             10x bigger input -> about 10x more memory.

// Linear scan means you go through the values once, from start to end. One pass means the time grows in a straight line with the input, so Time: O(n).
//? -----


// Problem: Longest Word in a String (JS #1)
// Pattern: Linear scan + "best so far" variable (running max)
// Trick: Split into words, loop once, and keep the longest word seen so far.
//        Replace it only when the new word is strictly longer (so ties keep the first one).
// Time: O(n) where n = number of characters (split and the loop each touch the text once)
// Space: O(n) for the words array


function longest_word(str){
    let words_array = str.split(" ")
    let longest_word = ""
    for (let word of words_array){
        longest_word =  longest_word.length < word.length ? word : longest_word
    }
    return longest_word
}

// console.log(longest_word("My name is Muhammmad Azan"))



//* 2. Given an array of integers, move all zeros to the end while maintaining the relative order of the non-zero elements.

// Problem: Move all zeros to end & maintine non zero elements order (JS #2)
// Pattern: Two pointer (reader and writer), in place
// Trick : The reader scans every item. The writer marks the next spot for a non-zero.
//       The writer never gets ahead of the reader, so nothing unread is overwritten.
//       After the scan, fill from the writer to the end with zeros.

// Time: O(n), steps grow in a straight line with the input.
//             10x bigger input -> about 10x more steps.

// Space: O(1), only two position variables, no new array
        // so even if the input gets bigger the memory not increases
        // memory remain same we are changing the original array in place


let arr = [0, 1, 0, 3, 12]

function move_zeros(array){
    writer = 0
    reader = 0
    for (let value of array){

        if (value != 0){
            arr[writer] = value
            writer+=1
        }   
    reader+=1
    }

    while (writer < reader){
        array[writer] = 0
        writer+=1
    }
    return array
}

// console.log(move_zeros(arr))


//* 3. Write a function to deeply flatten an array of arbitrarily nested arrays (e.g., `[1, [2, [3, 4]]]`).

// problem : flatte a nested array
// pattern : recursion
// Base case (stop): a value that is NOT an array is added straight to the result.
// Recursive case: a value that IS an array -> call the same function on it,   get back a flat list, and merge it into the result.
// trick : the function trusts that every recursive call returns an already-flat list, so each level only has to merge flat lists together.
// Time: O(n * d) in the worst case, where n = total number of items and d = how deep the nesting goes.
//       The spread [...a, ...b] builds a new array and copies everything collected so far,
//       so with deep nesting the same items get copied again and again.
//       In the worst case (very deep nesting) this can grow toward O(n^2).
// space : O(n) (for the result, plus the recursion depth) as input increase the space (memory) also increase to store new flatted array

nested_array = [1,2,[3,4,[5,6]]]
function flatten_array(array){
    let flattenArray = []

    for (let val of array){
        
        if(Array.isArray(val)){
            let result = flatten_array(val)
            flattenArray = [...flattenArray , ... result]

        }else{
            flattenArray.push(val)
        }
    }

    return flattenArray
}
// console.log(flatten_array(nested_array))