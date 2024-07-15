import cv2

# Replace this URL with your IP webcam's stream URL
stream_url = 'http://192.168.237.28:8080/video'
cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
from pyzbar.pyzbar import decode

def scan_codes(frame):
    codes = decode(frame)
    for code in codes:
        x, y, w, h = code.rect
        # Draw a rectangle around the code
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # This will print the type of code and the decoded content
        barcode_info = code.data.decode('utf-8')
        barcode_type = code.type
        cv2.putText(frame, f"{barcode_type}: {barcode_info}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Optionally, you could do something with the barcode_info like storing it or sending it somewhere
    return frame
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Process each frame
    processed_frame = scan_codes(frame)
    
    # Display the resulting frame
    cv2.imshow('QR & Barcode Scanner', processed_frame)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
     break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
