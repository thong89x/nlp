
import re

# Function to process incoming messages and suggest actions
def process_message(message):
    # Define time-related patterns in Vietnamese
    time_patterns = [
        r'\b(1[0-2]|[1-9])([ ]?giờ|:[0-5][0-9])?\b',  # Matches hours (e.g., "6 giờ", "10:30")
        r'\b(1[0-9]|2[0-3]|0?[1-9]):[0-5][0-9]\b',  # Matches hours and minutes (e.g., "6:00", "13:45")
        r'\bhôm nay\b',  # Matches "hôm nay"
        r'\bngày mai\b',  # Matches "ngày mai"
        r'\btối nay\b'  # Matches "tối nay"
    ]
    
    # Define keywords for event title extraction
    title_keywords = ["gặp nhau", "đi ăn", "họp", "thảo luận", "tổ chức"]
    
    # Find time-related patterns in the message
    time_matches = []
    for pattern in time_patterns:
        matches = re.findall(pattern, message)
        if matches:
            # Convert tuples to strings and append to time_matches
            time_matches.extend([match[0] for match in matches])
    
    # Find keywords for event title extraction
    title_candidates = []
    for keyword in title_keywords:
        if keyword in message:
            title_candidates.append(keyword)
    
    # If title candidates are found, suggest creating an event with a title
    if title_candidates:
        title = ", ".join(title_candidates)
        if time_matches:
            time = ", ".join(time_matches)
            return f"Tạo sự kiện '{title}' vào thời gian: {time}"
        else:
            return f"Tạo sự kiện '{title}'"
    else:
        return None

# Example usage with Vietnamese message
message = "Chúng ta hãy gặp nhau ở quán cà phê vào lúc 6 giờ chiều để thảo luận về dự án"
action = process_message(message)
if action:
    print(f"Hành động đề xuất: {action}")
else:
    print("Không có hành động nào được đề xuất cho tin nhắn này.")
