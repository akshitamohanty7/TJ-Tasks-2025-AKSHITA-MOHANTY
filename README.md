# TJ-Tasks-2025-AKSHITA-MOHANTY
This repository contains beginner-level DSA solutions focusing on arrays, sequences, and string manipulation. It demonstrates basic problem-solving techniques, such as minimal operations, alternating patterns, and string transformations, aimed at building a strong foundation in algorithmic thinking.

HERE'S MY APPROACH FOR EACH QUESTION:

1️⃣ Make the Product Positive
💡 The Problem

We’ve got an array filled with -1, 0, and 1.
In one move, you can increase any element by 1.
Goal? Make the product of all elements strictly positive using as few moves as possible.

⚙️ My Thought Process

Count how many -1s and 0s we’ve got.

Each 0 → needs 1 operation (0 → 1)

Each -1 → needs 2 operations (-1 → 0 → 1)

Add them up:
ops = count_zero + 2 * count_negative

But if the number of -1s is odd and there’s no zero to flip, we need one more step to fix the sign.

✅ In short: turn the mess of negatives and zeros into a team of happy positives with minimum effort.

<img width="271" height="245" alt="task0" src="https://github.com/user-attachments/assets/d38d372a-eeae-4008-9730-6b67cd26cac5" />



2️⃣ 
💡 The Problem

Farmer John alternates x and -x for n terms:
like x, -x, x, -x, …
We need the sum of this funky little sequence.

⚙️ My Thought Process

Notice the pattern:

If n is even → all terms cancel out → sum = 0

If n is odd → one extra x survives → sum = x

No need to actually build the array. Just check if n is even or odd.

✅ In short: pure observation + math beats looping any day.
<img width="521" height="419" alt="task1" src="https://github.com/user-attachments/assets/1a8a5892-640e-452a-b13b-1f1d217b7052" />



3️⃣ 
💡 The Problem

Each country’s ancient name has three words.
The modern name = first letter of each, stuck together in uppercase.

⚙️ My Thought Process

Split the line into 3 words

Grab their first letters

Join them, uppercase the result, and boom = modern name formed.

✅ In short: simple string slicing and a bit of style because even countries deserve rebranding.

<img width="306" height="356" alt="task2" src="https://github.com/user-attachments/assets/75dbe400-3c4a-4f02-84e2-cd25821f7915" />

