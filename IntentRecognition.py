import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to extract intents and entities from user messages
def extract_intents_entities(message):
    # Process the message with spaCy
    doc = nlp(message)
    
    # Initialize variables to store intents and entities
    intents = []
    entities = []
    
    # Extract intents and entities from the analyzed message
    for token in doc:
        print(token)
        print(token.pos_)
        # print(token.label_)
        # Extract intents based on verb tokens
        if token.pos_ == "VERB":
            intents.append(token.text)
        
        # Extract entities based on named entities
        if token.ent_type_ != "":
            entities.append((token.text, token.ent_type_))
    
    return intents, entities

# Example usage
message = "Book a table for two at the Italian restaurant"
intents, entities = extract_intents_entities(message)
print("Intents:", intents)
print("Entities:", entities)
