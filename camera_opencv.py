import cv2

# Öffnen der virtuellen Kamera von OBS
vid = cv2.VideoCapture(1)  # Die Nummer "0" steht normalerweise für die erste angeschlossene Webcam, möglicherweise musst du die Nummer anpassen
                           # Für OBS ich habe "1" verwendet.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                   
while True:
    # Erfassen eines Frames von der virtuellen Kamera von OBS
    ret, frame = vid.read()

    # Wenn der Frame erfolgreich erfasst wurde
    if ret:
        # Anzeigen des Frames in einem OpenCV-Fenster
        cv2.imshow('frame', frame)

        # Überprüfen auf Drücken der Taste 'q' zum Beenden
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Freigeben des Videoerfassungsobjekts
vid.release()

# Schließen der OpenCV-Fenster
cv2.destroyAllWindows()
