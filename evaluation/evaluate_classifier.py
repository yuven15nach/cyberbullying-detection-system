from utils.gemini_api import ask_gemini

#this is few shot prompt(new version code)
def classify_for_evaluation(text):

    return ask_gemini(f"""
You are an AI assistant for cyberbullying detection.

Classify the given message into ONE of the following categories only:

- not_cyberbullying
- gender
- religion
- age
- ethnicity
- other_cyberbullying

Important Rules:
- Return exactly ONE type.
- Never return multiple types.
- If the message is offensive but NOT targeted harassment, classify it as not_cyberbullying.
- If uncertain, choose the single most appropriate category.

-------------------------
Example 1

Message:
"You are stupid."

Output:
Bullying: Yes
Type: other_cyberbullying
Severity: Medium

-------------------------
Example 2

Message:
"I hate your religion. Go back where you came from."

Output:
Bullying: Yes
Type: religion
Severity: High

-------------------------
Example 3

Message:
"You are too old to understand anything."

Output:
Bullying: Yes
Type: age
Severity: Medium

-------------------------
Example 4

Message:
"Why is this TV show so white?"

Output:
Bullying: No
Type: not_cyberbullying
Severity: Low

-------------------------
Example 5

Message:
"I love watching football."

Output:
Bullying: No
Type: not_cyberbullying
Severity: Low
                      
-------------------------
Example 6

Message:
"Girls are so dumb. They shouldn't be allowed to vote."

Output:
Bullying: Yes
Type: gender
Severity: High  

-------------------------
Example 7

Message:
"People from your race are useless."

Output:
Bullying: Yes
Type: ethnicity
Severity: High                                       

-------------------------

Now classify this message:

"{text}"

Return ONLY in this format:

Bullying: Yes or No
Type: one label only
Severity: Low, Medium, or High
""")