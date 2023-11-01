import cv2

cv2.imread("solar-system.jpg")
cv2.waitKey(0)

cv2.putText(img
            "Sun",
            (20,300),
            cv2.Font_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img
            "Venus"
            (30,400)
            cv2.FONT_HERSHEY_COMPLEX
            0.6,
            (255,255,255)
            )

cv2.putText(img
            "Earth"
            (20,200)
            cv2.FONT_HERSHEY_COMPLEX
            0.7,
            (255,255,255)
            ) 

cv2.putText(img
            "Neptune"
            (40,200)
            cv2.FONT_HERSHEY_COMPLEX
            0.8,
            (255,255,255)
            ) 

cv2.putText(img
            "Saturn"
            (20,100)
            cv2.FONT_HERSHEY_COMPLEX
            0.9,
            (255,255,255)
            ) 

cv2.putText(img
            "Mars"
            (10,100)
            cv2.FONT_HERSHEY_COMPLEX
            0.10,
            (255,255,255)
            ) 

cv2.putText(img
            "Mercury"
            (10,100)
            cv2.FONT_HERSHEY_COMPLEX
            0.1,
            (255,255,255)
            ) 

cv2.putText(img
            "Jupiter"
            (40,500)
            cv2.FONT_HERSHEY_COMPLEX
            0.2,
            (255,255,255)
            ) 

cv2.putText(img
            "Uranus"
            (20,100)
            cv2.FONT_HERSHEY_COMPLEX
            0.3,
            (255,255,255)
            ) 

cv2.imshow("output",img)
cv2.imwrite("Solar_systemwithname.jpg",img)
