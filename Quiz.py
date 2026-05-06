print(" Welcome to  Quiz!")
score = 0
#Physics:

# Question 1
print("\n1. SI unit of force is?")
print("a) Joule")
print("b) Newton")
print("c) Watt")
ans = input("Your answer: ").lower()

if ans == "b":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 2
print("\n2. Speed = ?")
print("a) Distance / Time")
print("b) Time / Distance")
print("c) Force / Mass")
ans = input("Your answer: ").lower()

if ans == "a":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 3
print("\n3. Unit of electric current?")
print("a) Volt")
print("b) Ampere")
print("c) Ohm")
ans = input("Your answer: ").lower()

if ans == "b":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 4
print("\n4. Acceleration due to gravity on Earth?")
print("a) 9.8 m/s²")
print("b) 8.9 m/s²")
print("c) 10.8 m/s²")
ans = input("Your answer: ").lower()

if ans == "a":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 5
print("\n5. Work = ?")
print("a) Force × Distance")
print("b) Mass × Velocity")
print("c) Power × Time")
ans = input("Your answer: ").lower()

if ans == "a":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 6
print("\n6. Light travels fastest in?")
print("a) Water")
print("b) Air")
print("c) Vacuum")
ans = input("Your answer: ").lower()

if ans == "c":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 7
print("\n7. Ohm’s Law is?")
print("a) V = IR")
print("b) P = VI")
print("c) F = ma")
ans = input("Your answer: ").lower()

if ans == "a":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 8
print("\n8. Unit of power?")
print("a) Watt")
print("b) Joule")
print("c) Newton")
ans = input("Your answer: ").lower()

if ans == "a":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 9
print("\n9. Momentum = ?")
print("a) Mass × Velocity")
print("b) Force × Time")
print("c) Energy × Time")
ans = input("Your answer: ").lower()

if ans == "a":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 10
print("\n10. Unit of energy?")
print("a) Watt")
print("b) Joule")
print("c) Newton")
ans = input("Your answer: ").lower()

if ans == "b":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

#Biology

# Question 11
print("\n11. Which is the basic unit of life?")
print("a) Tissue")
print("b) Cell")
print("c) Organ")
ans = input("Your answer: ").lower()

if ans == "b":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 12
print("\n12. DNA is found in?")
print("a) Nucleus")
print("b) Ribosome")
print("c) Cytoplasm")
ans = input("Your answer: ").lower()

if ans == "a":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 13
print("\n13. Photosynthesis occurs in?")
print("a) Mitochondria")
print("b) Chloroplast")
print("c) Nucleus")
ans = input("Your answer: ").lower()

if ans == "b":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 14
print("\n14. Human heart has how many chambers?")
print("a) 2")
print("b) 3")
print("c) 4")
ans = input("Your answer: ").lower()

if ans == "c":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 15
print("\n15. Which is the powerhouse of the cell?")
print("a) Ribosome")
print("b) Mitochondria")
print("c) Golgi body")
ans = input("Your answer: ").lower()

if ans == "b":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 16
print("\n16. Blood is a?")
print("a) Tissue")
print("b) Organ")
print("c) Cell")
ans = input("Your answer: ").lower()

if ans == "a":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 17
print("\n17. Largest organ of human body?")
print("a) Heart")
print("b) Liver")
print("c) Skin")
ans = input("Your answer: ").lower()

if ans == "c":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 18
print("\n18. Oxygen is transported by?")
print("a) RBC")
print("b) WBC")
print("c) Platelets")
ans = input("Your answer: ").lower()

if ans == "a":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 19
print("\n19. Enzyme is a?")
print("a) Lipid")
print("b) Protein")
print("c) Carbohydrate")
ans = input("Your answer: ").lower()

if ans == "b":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Question 20
print("\n20. Genetic material is?")
print("a) RNA")
print("b) DNA")
print("c) Both DNA and RNA")
ans = input("Your answer: ").lower()

if ans == "c":
    print("Correct! ")
    score += 1
else:
    print("Wrong! ")

# Final Score
print("\n Your Final Score:", score, "/ 20")

if score == 20:
    print("Excellent! ")
elif score >= 17:
    print("Very Good! ")
elif score >= 12:
    print("Good, but need more practice .")
else:
    print("Very bad! ")



again = input("\nPlay again? (yes/no): ").lower()

if again == "yes":
    print("Run the program again ")
else:
    print("Thanks for playing! ")
