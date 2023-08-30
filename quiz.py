#! C:\Python39-32\python.exe
import cgi

# Function to generate the HTML page with the quiz results
def generate_result_page(score):
    print("Content-Type:text/html\n\n")
    print("<html>")
    print("<head>")
    print("<title>Quiz Results</title>")
    print("</head>")
    print("<body>")
    print("<h1>Quiz Results</h1>")
    print("<p>Your score is: " + str(score) + "</p>")
    print("</body>")
    print("</html>")

# Process the form data
form = cgi.FieldStorage()

# Retrieve the answers from the form data
q1_answer = form.getvalue("q1")
q2_answer = form.getvalue("q2")
q3_answer = form.getvalue("q3")
q4_answer = form.getvalue("q4")
q5_answer = form.getvalue("q5")

# Calculate the score
score = 0
if q1_answer == "c":
    score += 1
if q2_answer == "b":
    score += 1
if q3_answer == "c":
    score += 1
if q4_answer == "c":
    score += 1
if q5_answer == "a":
    score += 1

# Generate the quiz result
generate_result_page(score)
