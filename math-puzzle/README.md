### Puzzle Question 
n people are coming into a room with n seats. Seats are pre-assigned, but the first person forgets where they are supposed to sit so they randomly pick a seat at uniform probability. Each of the following person tries to sit according to their assignments; however, if their seat is taken, they will randomly pick a seat uniformly as well. What's the probability that the last person get to sit in their assigned seat? 

### What the code does
Model the situation and solve for the asked probability. We see probability = 50% for N = 2, 3, 4, ... 18, 19. The algorithm is not efficent for N >= 20. This does not constitue a mathematically tractable proof  obviously but it was a fun excercise. 
