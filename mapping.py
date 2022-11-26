import cv2

items = set()


def detect_Qrcode():
    global frame
    global fp
    global det
    try:
        value, points, straight_qrcode = det.detectAndDecode(frame)
        if value and (value not in items):
            items.add(value)
            print("VALUE:", value)
            fp.write(value + "\n")
            fp.flush()
    except Exception as error:
        pass




vid = cv2.VideoCapture(0)
fp = open("object.txt", "w")
det = cv2.QRCodeDetector()
while True:
    ret, frame = vid.read()
    detect_Qrcode()
    if cv2.waitKey(1) & 0xFF == ord("q"):
        vid.release()
        break
