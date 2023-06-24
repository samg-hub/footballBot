import cv2

cap = cv2.VideoCapture(0)

# frame_w = int(cap.get(3))
# frame_h = int(cap.get(4))
counter = 1
while True:
    ret , frame = cap.read()
    if ret == True:
        cv2.imshow("f" , frame)
        if cv2.waitKey(2) & 0xFF == ord("q"):
         break
        elif cv2.waitKey(1) & 0xFF == ord('s'):
           cv2.imwrite(f'/home/mound/Desktop/Test/ballblue{counter}.png',frame)
           print("Saved!")
    else:
        break
    counter +=1
cap.release()
cv2.destroyAllWindows()
