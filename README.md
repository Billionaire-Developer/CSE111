��C S E 1 1 1 
 
 Write the second half of a Python program that generates simple English sentences that you began in the prove milestone. As part of the previous lesson’s prove milestone, you wrote a program that generates English sentences with three parts: a determiner, a noun, and a verb. During this prove assignment, you will add functions so that your program generates sentences with four parts:

a determiner
a noun
a verb
a prepositional phrase
For example:

One girl talked for the car.
A bird drinks off one child.
The child will run on the car.
Some dogs drank above many rabbits.
Some children laugh at many dogs.
Some rabbits will talk about some cats.
To complete this prove assignment, your program must include at least these seven functions:

main
make_sentence
get_determiner
get_noun
get_verb
get_preposition
get_prepositional_phrase
You may add other functions if you find them helpful. The get_preposition function must randomly choose a preposition from a list and return the randomly chosen preposition. The get_prepositional_phrase function must make a prepositional phrase by calling the get_preposition, get_determiner, and get_noun functions.
