# sentiment analysis and named entity recognition
import spacy

# Load English tokenizer, tagger, parser, and NER
nlp = spacy.load("en_core_web_sm")

# Function to process incoming messages and suggest actions
def process_message(message):
    # Analyze the message using spaCy
    doc = nlp(message)
    
    # Initialize variables to store title, description, and time
    title = ""
    description = ""
    time = ""
    
    # Extract title, description, and time from the analyzed message
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
        if ent.label_ == "TIME" or ent.text.lower() in ["today", "tomorrow", "tonight"]:
            time = ent.text
        elif ent.label_ == "EVENT":
            if title == "":
                title = ent.text
            else:
                description = ent.text
    
    # If time is identified, suggest creating an event with title, description, and time
    if time:
        return f"Create Event with title: '{title}', description: '{description}', at time: {time}"
    else:
        return None

# Example usage
message = "Let's meet at the coffee shop at 6 PM to discuss the project"
action = process_message(message)
if action:
    print(f"Suggested action: {action}")
else:
    print("No action suggested for this message.")
