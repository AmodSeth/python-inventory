"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""


name = input("Enter your Name: ").strip()
age = int(input("Enter your Age: "))
city = input("Enter your City: ").strip()
profession = input("Enter your Profession: ").strip()
hobby = input("Enter your hobby: ").strip()

output_format = (
  f"Hello! My name is {name}. "
  f"I'm {age} years old and live in {city}. "
  f"I work as a {profession} and I absolutely enjoy {hobby} in my free time. "
  f"Nice to meet you! \n"
)
import datetime
current_time = datetime.date.today().isoformat()

intro_message = output_format + f"Logged In at: {current_time}"

border_string = "*" * 80

print(border_string + "\n" + intro_message +  "\n" + border_string)



