This was my breaking challenge this year. <br />
I got very dissapointed in myself on this challenge. I did not search long enough for this challenge. I realy like crypto which made it even harder that i failed.

We get a pdf and a msg.txt file<br />
The pdf explains this is an RSA encoded message. We get a restriction for the primes that are used for the encoding and decoding.
The restiction is:<br />
A\*p - B\*q < 10000<br />
and<br />
1 <= A, B <= 1000<br />

I was not sure if this ment that A is bigger than 1 and B is smaller than 1000 or bot A en B are between 1 and 1000. This is not clarified in the text but the second one seems like the more logical option.

the N of this challenge is 617 digets long. I tought the restiction ment that the search space of for the primes was reduced to primes of 301 to 315 digets.<br />
As the restiction means the 2 primes need to be at max 7 digets apart from each other. I tought that this might be enough reduction in search space that this was breakable. <br />
I spent quite a long time trying to find a way to generate all these primes. I also looked for a way to get the square root of the N number as this would give me a good starting point to check the primes middel out. I didn't find a way to get the square root of sutch a large number.

When I finaly started generating prime numbers within the bounds I quickly realized that there are just to many. It was quite late in the day at this point and I had completed almost all other challenges which probably made me to tired to push on as here I just gave up and looked up the solution :(

The solution is the only other sensible thing to do. Try and solve the equations to P or Q. To do so we need to change the unequality to an equality:<br />
A\*p - x = B\*q with |x| <1000<br />
then multiply both sided with p:<br />
A\*p² - x\*p = B\*q\*p<br />
As p\*q = N we can write:<br />
A\*p² - x\*p = B\*N<br />
or<br />
A\*p² - x\*p - B\*N = 0 <br />
We can now solve this second degree equation to p. as b, a and x are all fairly small we can loop trough all posible values of them and find the correct p and q pair:<br />
d = x² - 4\*A\*B\*N<br />
p = ( -x \* sqrt(d) )/(2\*A)<br />

Here I again came across the issue of taking square roots of very large numbers. I found in the write-up I read that there are algorithms for "nth root". This finds the integer x where x to the nth is as close as possible to the input number. As p and q need to be integers. the nth root will give a number that is only 0,x away from the actual root which is not that relevant for the huge numbers we are working with here.

The guide also gave a way to speed up the brute forcing. As x² is negligable small in comparison with 4*A*B*N we can drop it and stil find a reasonable value for d.<br />
I took the code from the guide instead of reimplementing it myself and made sure I understood it. Idealy I would reimplement it but as mentioned not finding this myself broke me a bit and I did not feel like doing a lot more effort other than making sure I understood the solution so I would be able to find it myself next time.


