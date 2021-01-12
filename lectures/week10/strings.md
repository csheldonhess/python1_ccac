# Strings!

String manipulation is one of the places where Python really shines. We have so many string methods available to us that, often, Python programs end up shorter and easier to write than programs in many other languages.

You have looped through strings, character-by-character, already. You may even have thought to yourself, "looping through strings and looping through lists: these processes seem really similar." They are!

And just like you can slice a list with square brackets, you can also slice a string!

Notation:
```Python
my_string_slice = my_string[start : end + 1 : count_by] # same parameters as range()
```

Let's have a look:


```python
# a reminder about slicing lists

def main():
    my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', \
               'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', \
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', \
               'x', 'y', 'z']

    # first 10 - start at 0, end at 9
    print("my_list[0:10]:", my_list[0:10])

    # same thing, but a reminder that we don't need 0
    print("my_list[:10]:", my_list[:10])

    # print the last 10 characters
    print("my_list[-10:]:", my_list[-10:])

    # print every other character
    print("my_list[::2]", my_list[::2])
    
main()
```

    my_list[0:10]: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    my_list[:10]: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    my_list[-10:]: ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    my_list[::2] ['a', 'c', 'e', 'g', 'i', 'k', 'm', 'o', 'q', 's', 'u', 'w', 'y']
    


```python
# doing pretty much exactly the same thing to a string
def main():
    my_string = "abcdefghijklmnopqrstuvwxyz"

    # print the first 10 characters
    print("my_string[0:10]:", my_string[0:10]) 

    # same thing, but a reminder that we don't need 0
    print("my_string[:10]:", my_string[:10])

    # print the last 10 characters
    print("my_string[-10:]:", my_string[-10:])

    # print every other character
    print("my_string[::2]:", my_string[::2])

main()
```

    my_string[0:10]: abcdefghij
    my_string[:10]: abcdefghij
    my_string[-10:]: qrstuvwxyz
    my_string[::2]: acegikmoqsuwy
    

We've also seen that we can iterate through a string, in much the same way as we iterate through a list.


```python
def print_with_spaces(a_string):
    """takes in a string and prints it with spaces between characters"""
    # (we don't loop through strings to print them often, no)
    for letter in a_string:
        # print each letter with a space between them
        print(letter, end=" ")
        
        
def main():
    # set up and print our string
    my_string = "abcdefghijklmnopqrstuvwxyz"
    print(my_string)
    print("") # adding a little space
    print_with_spaces(my_string)



main()
```

    abcdefghijklmnopqrstuvwxyz
    
    a b c d e f g h i j k l m n o p q r s t u v w x y z 


```python
def pretty_print(a_list):
    """takes in a list and prints each item with spaces between them"""
    for item in a_list:
        print(item, end=" ")
      
    
def main():
    # the same operation with a list
    my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', \
               'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', \
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', \
               'x', 'y', 'z']
    print(my_list)
    print("") # just adding some spacing
    pretty_print(my_list)
        
main()
```

    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    a b c d e f g h i j k l m n o p q r s t u v w x y z 

But there is a very big difference between strings and lists, besides the obvious extra brackets and commas.


```python
def main():
    my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', \
               'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', \
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', \
               'x', 'y', 'z']

    # add an item to a list
    my_list.append("1")
    pretty_print(my_list)
    
main()
```

    a b c d e f g h i j k l m n o p q r s t u v w x y z 1 


```python
def main():
    my_string = "abcdefghijklmnopqrstuvwxyz"
    # add an item to a string
    my_string.append("1")
    print(my_string)
    
main()
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-7-9617b8e2423f> in <module>
          5     print(my_string)
          6 
    ----> 7 main()
    

    <ipython-input-7-9617b8e2423f> in main()
          2     my_string = "abcdefghijklmnopqrstuvwxyz"
          3     # add an item to a string
    ----> 4     my_string.append("1")
          5     print(my_string)
          6 
    

    AttributeError: 'str' object has no attribute 'append'


You can't append to a string, because, while lists are *mutable*, strings are *immutable*. 

This means that (as previously mentioned,) you can *change a list in place*, but the only way of "changing" a string is reassigning/overwriting it&mdash;the same way we did with everything, right up until we met lists. 

Let me prove it to you. We'll print a string, call `.upper()` on it (which returns the same string, but uppercase), and then we'll print our string again to see if it has changed. (It will not have changed.)

Then we'll actually change the string, using an assignment statement. 

And then we'll compare that to what happens when you print a list, call `.reverse()` on it, and print it again. (It _will_ have changed, because list methods change a list in place.)


```python
#strings: immutable
def main():
    science_string = "Hello, I would like to science please!"

    # print string, uppercase it, and print again
    print(science_string)
    science_string.upper()
    print(science_string)

main()
```

    Hello, I would like to science please!
    Hello, I would like to science please!
    


```python
# print string, replace it with uppercase, and print again
# (just like we've always done things, until we got to lists)
def main():
    science_string = "Hello, I would like to science please!"
    print(science_string)
    science_string = science_string.upper()
    print(science_string)
    
main()
```

    Hello, I would like to science please!
    HELLO, I WOULD LIKE TO SCIENCE PLEASE!
    


```python
#lists: mutable

def main():
    science_list = ["Hello", "I", "would", "like", "to", "science", "please!"]

    # print list, reverse it, and print again
    print(science_list)
    science_list.reverse()
    print(science_list)
    
main()

# want to talk about why we didn't call .upper()?
```

    ['Hello', 'I', 'would', 'like', 'to', 'science', 'please!']
    ['please!', 'science', 'to', 'like', 'would', 'I', 'Hello']
    

Hopefully, that reminder about the similarities and the differences between lists and strings was helpful. It trips people up, entirely understandably&mdash;enough so that sometimes the similiarities in syntax between strings and lists seem more like a curse than a blessing.

We were discussing **string splicing**, before we had our little chat about lists.

Remember you can pull a single character from a string:


```python
my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string[3])
```

    d
    

You can pull a substring:


```python
print(my_string[3:8])
```

    defgh
    

And you can even reverse a string. First, because we should all occasionally take a moment to appreciate how great Python is, let me remind you how we this when we only had loops as a tool -- which is mostly all you get with other programming languages:


```python
def reverse_string(a_string):
    """reverse a string using loops"""
    top_index = len(a_string)
    new_string = ""

    # work backwards through the string
    for index in range(top_index-1, -1, -1):
        new_string = new_string + a_string[index]
    return new_string


def main():
    my_string = input("Please give me a string: ")
    
    reversed_string = reverse_string(my_string)

    print("Your string has", len(my_string), "characters. Backwards, it reads:")
    print(reversed_string)


main()
```

    Please give me a string: i love birds!
    Your string has 13 characters. Backwards, it reads:
    !sdrib evol i
    

Several weeks later, here's an even faster way to reverse a string in Python:


```python
def faster_reverse_string(a_string):
    """reverse a string with the power of string slices!"""
    new_string = a_string[::-1]
    return new_string


def main():
    my_string = input("Please give me a string: ")
    
    reversed_string = faster_reverse_string(my_string)

    print("Your string has", len(my_string), "characters. Backwards, it reads:")
    print(reversed_string)

main()
```

    Please give me a string: i love birds!
    Your string has 13 characters. Backwards, it reads:
    !sdrib evol i
    

It's just so beautiful.

Still, no reasonable person will get upset with you if you do it the longer way. In the (honestly pretty rare) cases when you need to reverse a string, it's fine to do it whichever way you're comfortable with.

Let me give you some more string methods. We'll go through them pretty quickly, and then we'll do a practice problem where you can choose whether you'd like to work with loops or with string slicing.

## A bunch of string methods

### First, checking what's in our strings (conditionals):

We'll set up a bunch of strings that we can check with all of these string-checking functions.


```python
# first, let's set up some strings for testing
lc_alpha_char = "a" # lowercase alphabetical
uc_alpha_car = "A" # uppercase alphabetical
num_char = "1" # numeric, but still a character
space_char = " " # a space
punct_char = "." # a punctuation character
endline_char = "\n" # a different kind of space - the endline

print("Just showing we ran this block. Coral forgets sometimes.")
```

    Just showing we ran this block. Coral forgets sometimes.
    

#### `.isalpha()` - returns a `True` or `False` answering "is this alphabetic?"


```python
# which ones are alphabet characters?
print(".isalpha() checks for alphabetic characters:")
print(lc_alpha_char, "isalpha?", lc_alpha_char.isalpha())
print(uc_alpha_car, "isalpha?", uc_alpha_car.isalpha())
print(num_char, "isalpha?", num_char.isalpha())
print("space isalpha?", space_char.isalpha())
print(punct_char, "isalpha?", punct_char.isalpha())
print("endline isalpha?", endline_char.isalpha())
```

    .isalpha() checks for alphabetic characters:
    a isalpha? True
    A isalpha? True
    1 isalpha? False
    space isalpha? False
    . isalpha? False
    endline isalpha? False
    

#### `.isdigit()` or `.isnumeric()` - returns `True` or `False` answering "is this a digit or digits?"


```python
# which ones are digits?
print(".isdigit() checks for digits:")
print(lc_alpha_char, "isdigit?", lc_alpha_char.isdigit())
print(uc_alpha_car, "isdigit?", uc_alpha_car.isdigit())
print(num_char, "isdigit?", num_char.isdigit())
print("space isdigit?", space_char.isdigit())
print(punct_char, "isdigit?", punct_char.isdigit())
print("endline isdigit?", endline_char.isdigit())
```

    .isdigit() checks for digits:
    a isdigit? False
    A isdigit? False
    1 isdigit? True
    space isdigit? False
    . isdigit? False
    endline isdigit? False
    


```python
# which ones are digits?
print(".isnumeric() checks for numbers:")
print(lc_alpha_char, "isnumeric?", lc_alpha_char.isnumeric())
print(uc_alpha_car, "isnumeric?", uc_alpha_car.isnumeric())
print(num_char, "isnumeric?", num_char.isnumeric())
print("space isnumeric?", space_char.isnumeric())
print(punct_char, "isnumeric?", punct_char.isnumeric())
print("endline isnumeric?", endline_char.isnumeric())
```

    .isnumeric() checks for numbers:
    a isnumeric? False
    A isnumeric? False
    1 isnumeric? True
    space isnumeric? False
    . isnumeric? False
    endline isnumeric? False
    


```python
# check one other thing
neg_one = "-1"
print(neg_one, "is digit?", neg_one.isdigit())
print(neg_one, "is numeric?", neg_one.isnumeric())
# ah well
```

    -1 is digit? False
    -1 is numeric? False
    


```python
# so... what is the difference?
# usually nothing, EXCEPT

wu = "五" # Chinese character for five

print("Is 五 a digit?", wu.isdigit())
print("Is 五 numeric?", wu.isnumeric())

```

    Is 五 a digit? False
    Is 五 numeric? True
    

#### `.isalnum()` - `True` or `False` to "is this alphabetic or numeric?"


```python
# which ones are alphanumeric?
print(".isalnum() checks for alphanumeric characters:")
print(lc_alpha_char, "isalnum?", lc_alpha_char.isalnum())
print(uc_alpha_car, "isalnum?", uc_alpha_car.isalnum())
print(num_char, "isalnum?", num_char.isalnum())
print("space isalnum?", space_char.isalnum())
print(punct_char, "isalnum?", punct_char.isalnum())
print("endline isalnum?", endline_char.isalnum())
```

    .isalnum() checks for alphanumeric characters:
    a isalnum? True
    A isalnum? True
    1 isalnum? True
    space isalnum? False
    . isalnum? False
    endline isalnum? False
    


```python
# what do we think?
print(neg_one, "is alnum?", neg_one.isalnum())
```

    -1 is alnum? False
    

#### `.islower()` - lowercase character(s)? `True`/`False`


```python
# which ones are lowercase?
print(".islower() checks for lowercase characters:")
print(lc_alpha_char, "islower?", lc_alpha_char.islower())
print(uc_alpha_car, "islower?", uc_alpha_car.islower())
print(num_char, "islower?", num_char.islower())
print("space islower?", space_char.islower())
print(punct_char, "islower?", punct_char.islower())
print("endline islower?", endline_char.islower())
```

    .islower() checks for lowercase characters:
    a islower? True
    A islower? False
    1 islower? False
    space islower? False
    . islower? False
    endline islower? False
    

#### `.isupper()` - uppercase character(s)? `True`/`False`


```python
# which ones are uppercase?
print(".isupper() checks for uppercase characters:")
print(lc_alpha_char, "isupper?", lc_alpha_char.isupper())
print(uc_alpha_car, "isupper?", uc_alpha_car.isupper())
print(num_char, "isupper?", num_char.isupper())
print("space isupper?", space_char.isupper())
print(punct_char, "isupper?", punct_char.isupper())
print("endline isupper?", endline_char.isupper())
```

    .isupper() checks for uppercase characters:
    a isupper? False
    A isupper? True
    1 isupper? False
    space isupper? False
    . isupper? False
    endline isupper? False
    

#### `.isspace()` - is this string made up of whitespace? `True`/`False`


```python
# which ones are spaces?
print(".isspace() checks for space characters:")
print(lc_alpha_char, "isspace?", lc_alpha_char.isspace())
print(uc_alpha_car, "isspace?", uc_alpha_car.isspace())
print(num_char, "isspace?", num_char.isspace())
print("space isspace?", space_char.isspace())
print(punct_char, "isspace?", punct_char.isspace())
print("endline isspace?", endline_char.isspace())
```

    .isspace() checks for space characters:
    a isspace? False
    A isspace? False
    1 isspace? False
    space isspace? True
    . isspace? False
    endline isspace? True
    


```python
# checking one other thing
tab = "\t"
print("tab is space?", tab.isspace())
```

    tab is space? True
    

I don't know about you, but what I've wanted, at various points in my life, is some kind of .ispunct() method, to test if a character is a piece of punctuation. That's ... not a thing, but we can make an is_punctuation() function!


```python
import string # yep, we have a module for this

# we didn't set this up as a method on string
# (more on that in a minute) but as a function, so
# we call it differently
def is_punctuation(characters):
    """checks one or more characters; 
    returns True if they are all punctuation, False otherwise"""
    # an empty space is not punctuation
    if len(characters) == 0:
        return False
    
    # this will run at least once, now
    for character in characters:
        # punctuation is a constant belonging to string
        # if we find any non-punctuation, we immediately return False
        if character not in string.punctuation:
            return False
    
    # if len > 0 and we didn't find any non-punctuation characters
    return True


def main():
    print("Testing our own is_punctuation() function:")
    print(lc_alpha_char, "is punctuation?", is_punctuation(lc_alpha_char))
    print(uc_alpha_car, "is punctuation?", is_punctuation(uc_alpha_car))
    print(num_char, "is punctuation?", is_punctuation(num_char))
    print("space is punctuation?", is_punctuation(space_char))
    print(punct_char, "is punctuation?", is_punctuation(punct_char))
    print("endline is punctuation?", is_punctuation(endline_char))
    print("empty string is punctuation?", is_punctuation(""))

    print("") # give ourselves some space
    print("What's in string.punctuation:")
    print(string.punctuation)

main()
```

    Testing our own is_punctuation() function:
    a is punctuation? False
    A is punctuation? False
    1 is punctuation? False
    space is punctuation? False
    . is punctuation? True
    endline is punctuation? False
    empty string is punctuation? False
    
    What's in string.punctuation:
    !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    

For other fun string constants, see [the Python 3.7 documentation](https://docs.python.org/3.7/library/string.html)

### A note on the above!

All of the string conditional statements we've looked at so far are a little cleaner when you run them on **a single character**. They absolutely _work_ on multi-character strings, but it's a good way to trip yourself up, if you aren't careful.


```python
# save a bunch of alpha characters
coffee_string = "i love coffee"
print(coffee_string.isalpha())
# what?
```

    False
    


```python
# ohhhh, riiiight
coffee_string2 = "ilovecoffee"
print(coffee_string2.isalpha())
# spaces aren't alpha
```

    True
    


```python
# is_punctuation() will work on multi-character strings, too
punct_string = string.punctuation
not_punct_string = "5" + string.punctuation

print(punct_string, "is punctuation?", is_punctuation(punct_string))
print(not_punct_string, "is punctuation?", is_punctuation(not_punct_string))
```

    !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ is punctuation? True
    5!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ is punctuation? False
    

### A few useful string transformation methods
#### `.replace(string1, string2)`

Finds `string1` in the string you call it on and replaces it with `string2`; does nothing if it doesn't find `string1`


```python
emperor = "The only emperor is the emperor of ice-cream."
print(emperor)

emperor_nospace = emperor.replace(" ", "")
print(emperor_nospace)

emperor_of_penguins = emperor.replace("ice-cream", "penguins")
print(emperor_of_penguins)

emperor_of_what = emperor.replace("king", "monarch")
print(emperor_of_what)
```

    The only emperor is the emperor of ice-cream.
    Theonlyemperoristheemperorofice-cream.
    The only emperor is the emperor of penguins.
    The only emperor is the emperor of ice-cream.
    

We'll do more string methods below, but I want to remind you about two that you've seen before and that are going to be relevant to your interests immediately:

#### `.lower()` and `.upper()`

We've seen these before, at least in passing. They do what you'd think.
* `.lower()` lowercases every character in the string
* `.upper()` uppercases every character in the string


```python
coffee_string = "I lIkE cOfFeE"

print(coffee_string)

print(coffee_string.upper())

print(coffee_string.lower())
```

    I lIkE cOfFeE
    I LIKE COFFEE
    i like coffee
    

## Practice time!

Using string slicing (or a loop if you prefer) and string transformation, write a program to check if a string is a palindrome. A string is a palindrome if it is the same forward as it is backward, ignoring spaces and capitalization. (If you get done with this before the rest of the class, go ahead and have it ignore punctuation, too.)

For instance, "Was it a cat I saw" is a palindrome. "Anna" and "racecar" are both palindromes, too. If you arrange the letters backwards, ignoring spaces and capitalization, they're the same.

(Hint: I keep saying "ignoring spaces," which is important for reasons that are maybe obvious. Remember, also, that the statement `"a" == "A"` evaluates to `False`.)

### Some multi-character string checking methods

#### `.endswith(substring)`

Evaluates to `True` if the string you call it on ends with the string you pass in; evalutes to `False` if not


```python
my_string = "abcdefghijklmnopqrstuvwxyz"
coffee_string = "I like coffee"
coffee_string2 = "I like coffee!"

# which one ends with "coffee"?
print(my_string, "ends with coffee:", my_string.endswith("coffee"))
print(coffee_string, "ends with coffee:", coffee_string.endswith("coffee"))
print(coffee_string2, "ends with coffee:", coffee_string2.endswith("coffee"))
```

    abcdefghijklmnopqrstuvwxyz ends with coffee: False
    I like coffee ends with coffee: True
    I like coffee! ends with coffee: False
    

#### `.startswith(substring)`

Returns `True` if the string you call it on begins with the string you pass in; returns `False` if not


```python
print(my_string, "starts with i:", my_string.startswith("i"))
print(coffee_string, "starts with i:", coffee_string.startswith("i"))
```

    abcdefghijklmnopqrstuvwxyz starts with i: False
    I like coffee starts with i: True
    

#### in, not in 

Checks to see if a string is inside another string; returns True or False as appropriate


```python
# remind ourselves what we have
print(my_string)
print(coffee_string)

print("lmno is in", my_string, "-", "lmno" in my_string)
print("lmno is in", coffee_string, "-", "lmno" in coffee_string)
print("lmno is NOT in", my_string, "-", "lmno" not in my_string)
print("lmno is NOT in", coffee_string, "-", "lmno" not in coffee_string)
```

    abcdefghijklmnopqrstuvwxyz
    I like coffee
    lmno is in abcdefghijklmnopqrstuvwxyz - True
    lmno is in I like coffee - False
    lmno is NOT in abcdefghijklmnopqrstuvwxyz - False
    lmno is NOT in I like coffee - True
    

#### find(substr), rfind(substr)
Returns the index of the first and last places the substring is found


```python
emperor_string = "The only emperor is the emperor of ice-cream."
                 #012345678901234567890123456789012345
                 #__________1_________2_________3_____

# find & rfind a string that appears twice:
print(emperor_string.find("emperor"))
print(emperor_string.rfind("emperor"))
print("")

# find & rfind a string that appears once:
print(emperor_string.find("ice"))
print(emperor_string.rfind("ice"))
```

    9
    24
    
    35
    35
    

### Now, some (more) methods for transforming strings

#### `.capitalize()`

Just capitalizes the first letter


```python
print(coffee_string.capitalize())
```

#### `.title()`
Capitalizes the first letter in every word


```python
print(coffee_string.title())

# but, like, EVERY word
an_actual_title = "frankenstein; or the modern prometheus"
print(an_actual_title.title())

print("\nProperly, that title should be: Frankenstein; or the Modern Prometheus")
```

    I Like Coffee
    Frankenstein; Or The Modern Prometheus
    
    Properly, that title should be: Frankenstein; or the Modern Prometheus
    

#### `.strip()`, `.rstrip()`, `.lstrip()` 

Take off spaces **or optional included substring** from your string. Will remove _all spaces_ or _all copies_ of the substring you feed it. 

* `.strip()` - off both sides
* `.rstrip()` - off the right side
* `.lstrip()` - off the left side


```python
a_string = "  birds are great  "

# print with some underscores to show where the spaces are
print("_", a_string, "_", sep="")
print("_", a_string.lstrip(), "_", sep="")
print("_", a_string.rstrip(), "_", sep="")
print("_", a_string.strip(), "_", sep="")
```

    _  birds are great  _
    _birds are great  _
    _  birds are great_
    _birds are great_
    


```python
# stripping other characters

exciting = "WOW!!!!!"
# strips any number of things off the end
less_exciting = exciting.rstrip("!")
# not really the point, but let's do this.
less_exciting = less_exciting.lower()
print(less_exciting)
```

    wow
    


```python
even_less_exciting = less_exciting.strip("w")
print(even_less_exciting)
```

    o
    

# Moving back and forth between strings and lists

It's pretty common to have a list that you wish you could make into a string, or vice versa. Maybe even more so, it's common to have a string that would be easier to work with if you broke it into a list, did some work on it, and then made it a string again.

You've seen this before. :) 

Imagine you wanted to write a function that would do _actual_ title capitalization, keeping words like "and" and "the" lowercase (unless they're the first word ... it's actually a little bit involved, to write that function properly). You'd need a way to loop over the words and do some processing on them, right? And then you'd have to make them back into a string at the end.

The two methods we're going to need for this are
* `.split()`
* `.join()`

#### `.split()`


```python
# splitting a string into a list of words
raven_string = "Once upon a midnight dreary, while I pondered weak and weary"
raven_list = raven_string.split(" ")

print(raven_string)
print(raven_list)
```

    Once upon a midnight dreary, while I pondered weak and weary
    ['Once', 'upon', 'a', 'midnight', 'dreary,', 'while', 'I', 'pondered', 'weak', 'and', 'weary']
    

It's worth pointing out: you can split on anything. Spaces and endlines are the most common choices, in part because splitting on a character also strips it out. See what happens when we split on the character "e" to understand:


```python
nonsense_raven_list = raven_string.split("e")
print(nonsense_raven_list)
```

    ['Onc', ' upon a midnight dr', 'ary, whil', ' I pond', 'r', 'd w', 'ak and w', 'ary']
    

Now, once we have our string split up, we can do whatever processing we need to do. Let's do the title thing, but I'm going to simplify it just a little bit.


```python
def make_real_title_case(string):
    # using US GPO list of uncapitalized words
    # (AP, Chicago, and MLA style are more involved)
    stopwords = ["a", "an", "the", "at", "by", "for", \
                 "in", "of", "on", "to", "up", "and", \
                 "as", "but", "or", "nor"]
    list_of_words = string.split(" ")
    for index in range(len(list_of_words)):
        # first word of title and non-stopwords need to be capitalized
        if index == 0 or list_of_words[index] not in stopwords:
            list_of_words[index] = list_of_words[index].capitalize()
        # getting rid of capitalization in words that don't need it
        else:
            list_of_words[index] = list_of_words[index].lower()
    # we'll talk about this next!
    new_string = " ".join(list_of_words)
    return new_string

print(make_real_title_case(raven_string))
print(make_real_title_case(an_actual_title))
```

    Once Upon a Midnight Dreary, While I Pondered Weak and Weary
    Frankenstein; or the Modern Prometheus
    

#### `.join()`

The syntax for `.join()` is not especially intuitive, at least for me. If I go too long without using it, I have to look up the syntax again. 

If it helps, remember that this is a *string method, not a list method*, and that's why we have to call it on a string. (If I could remember that consistently, I would not need to look it up.)

The syntax pattern is

`some_string_variable = "your glue string".join(your_list)`

So if you have a lot of words in a list, that you want to be put together into a string with a space between them, it'll look like

`some_string_variable = " ".join(your_list_name)`


```python
# remind ourselves what's in raven_list
print(raven_list)

raven_string_with_dashes = "-".join(raven_list)
raven_string_with_spaces = " ".join(raven_list)

print(raven_string_with_dashes)
print(raven_string_with_spaces)
```

    ['Once', 'upon', 'a', 'midnight', 'dreary,', 'while', 'I', 'pondered', 'weak', 'and', 'weary']
    Once-upon-a-midnight-dreary,-while-I-pondered-weak-and-weary
    Once upon a midnight dreary, while I pondered weak and weary
    

## A non-apology

While we're talking about The Raven, anyway...

### `.count(substring)` - counts occurrences of substring in string


```python
# this piece is a preview for next week; you don't need it now
# I just didn't want to fill this notebook with a big, long poem
with open('the_raven.txt', 'r') as raven_file_object:
    the_raven = raven_file_object.read();

# this is the relevant part
# as you can see, though: use with caution!
nevermores = the_raven.count("nevermore") + the_raven.count("Nevermore")
ravens = the_raven.count("raven") + the_raven.count("Raven")

print("There are", nevermores, "occurrences of 'Nevermore' in The Raven")
print("There are", ravens, "occurrences of 'raven' in The Raven") # also counted "craven"
```

    There are 11 occurrences of 'Nevermore' in The Raven
    There are 11 occurrences of 'raven' in The Raven
    

#### `.splitlines()`
Split a string into a list by lines (each line becomes one string)


```python
raven_list = the_raven.splitlines()

# ugly-print the first 10 lines
print(raven_list[:10])

# notice what happens between "Only this and nothing more." and "Ah, distinctly I remember..."
```

    ['Once upon a midnight dreary, while I pondered, weak and weary,', 'Over many a quaint and curious volume of forgotten lore—', 'While I nodded, nearly napping, suddenly there came a tapping,', 'As of some one gently rapping, rapping at my chamber door.', '"\'Tis some visitor," I muttered, "tapping at my chamber door—', 'Only this and nothing more."', '', 'Ah, distinctly I remember it was in the bleak December;', 'And each separate dying ember wrought its ghost upon the floor.', 'Eagerly I wished the morrow;—vainly I had sought to borrow']
    


```python
# we can operate on each line as an individual string, now

# pretty-print the first ten lines
for index in range(0,10):
    print(raven_list[index])
```

    Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    "'Tis some visitor," I muttered, "tapping at my chamber door—
    Only this and nothing more."
    
    Ah, distinctly I remember it was in the bleak December;
    And each separate dying ember wrought its ghost upon the floor.
    Eagerly I wished the morrow;—vainly I had sought to borrow
    


```python
# skip the empty lines
for index in range(0, 10):
    # the one empty line we looked at was an empty string
    # but let's deal with the case where there's stray whitespace too
    if raven_list[index] != "" and not raven_list[index].isspace():
        print(raven_list[index])
```

    Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    "'Tis some visitor," I muttered, "tapping at my chamber door—
    Only this and nothing more."
    Ah, distinctly I remember it was in the bleak December;
    And each separate dying ember wrought its ghost upon the floor.
    Eagerly I wished the morrow;—vainly I had sought to borrow
    


```python

```
