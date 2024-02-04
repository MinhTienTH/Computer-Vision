#Import Library
import cv2
import mediapipe as mp
import imageio
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands = 2)
mpDraw = mp.solutions.drawing_utils
deg = 0
#VideoCapture
video = cv2.VideoCapture(0)

#Setting size for the video
#video.set(3, 1000)
#video.set(4, 780)

#Read image concluded: foreground, background and elec
img_1 = cv2.imread('magic_circles/force.png', -1)
img_2 = cv2.imread('magic_circles/background.png', -1)

#Read GIF concluded: beam, globe, fire
beam_gif = imageio.mimread('magic_circles/beam_gif.gif')
globe_gif = imageio.mimread('magic_circles/globe_gif.gif')
power1_gif = imageio.mimread('magic_circles/power1.gif')
power2_gif = imageio.mimread('magic_circles/power2.gif')
power3_gif = imageio.mimread('magic_circles/power3.gif')
power4_gif = imageio.mimread('magic_circles/power4.gif')
power5_gif = imageio.mimread('magic_circles/power5.gif')
broken_gif = imageio.mimread('magic_circles/broken.gif')
elec_gif = imageio.mimread('magic_circles/Electricity_gif.gif')
explode_gif = imageio.mimread('magic_circles/explode.gif')
energyball_gif = imageio.mimread('magic_circles/energyball.gif')

#Read GIF:
nums_globe = len(globe_gif)
globe = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in globe_gif]
nums_beam = len(beam_gif)
beam = [cv2.cvtColor(img1, cv2.COLOR_RGB2BGR) for img1 in beam_gif]

nums_power1 = len(power1_gif)
power1 = [cv2.cvtColor(img2, cv2.COLOR_RGB2BGR) for img2 in power1_gif]
nums_power2 = len(power2_gif)
power2 = [cv2.cvtColor(img3, cv2.COLOR_RGB2BGR) for img3 in power2_gif]
nums_power3 = len(power3_gif)
power3 = [cv2.cvtColor(img4, cv2.COLOR_RGB2BGR) for img4 in power3_gif]
nums_power4 = len(power4_gif)
power4 = [cv2.cvtColor(img5, cv2.COLOR_RGB2BGR) for img5 in power4_gif]
nums_power5 = len(power5_gif)
power5 = [cv2.cvtColor(img6, cv2.COLOR_RGB2BGR) for img6 in power5_gif]
nums_elec = len(elec_gif)
elec = [cv2.cvtColor(img7, cv2.COLOR_RGB2BGR) for img7 in elec_gif]
nums_broken = len(broken_gif)
broken = [cv2.cvtColor(img8, cv2.COLOR_RGB2BGR) for img8 in broken_gif]
nums_eb = len(energyball_gif)
energyball = [cv2.cvtColor(img9, cv2.COLOR_RGB2BGR) for img9 in energyball_gif]
nums_explode = len(explode_gif)
explode = [cv2.cvtColor(img10, cv2.COLOR_RGB2BGR) for img10 in explode_gif]
def position_data(lmlist):
    global wrist, thumb_mcp, thumb_tip, index_mcp, index_tip, midle_pip, midle_mcp, midle_tip,ring_mcp, ring_tip, pinky_mcp,\
        pinky_tip, ring_pip
    wrist = (lmlist[0][0], lmlist[0][1])
    thumb_mcp = (lmlist[2][0], lmlist[2][1])
    thumb_tip = (lmlist[4][0], lmlist[4][1])
    index_mcp = (lmlist[5][0], lmlist[5][1])
    index_tip = (lmlist[8][0], lmlist[8][1])
    midle_mcp = (lmlist[9][0], lmlist[9][1])
    midle_pip = (lmlist[10][0], lmlist[10][1])
    midle_tip = (lmlist[12][0], lmlist[12][1])
    ring_mcp = (lmlist[13][0], lmlist[13][1])
    ring_tip = (lmlist[16][0], lmlist[16][1])
    ring_pip = (lmlist[14][0], lmlist[14][1])
    pinky_mcp = (lmlist[17][0], lmlist[17][1])
    pinky_tip = (lmlist[20][0], lmlist[20][1])

#DrawLine for Hand_Landmarks function:
def draw_line(p1, p2, size=5):
    cv2.line(img, p1, p2, (50, 50, 255), size)
    cv2.line(img, p1, p2, (255, 255, 255), round(size / 2))

#Calculate the distance between two points in the hand
def calculate_distance(p1, p2):
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    lenght = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1.0 / 2)
    return lenght


def transparent(targetImg, x, y, size=None):
    if size is not None:
        targetImg = cv2.resize(targetImg, size)

    newFrame = img.copy()
    b, g, r, a = cv2.split(targetImg)
    overlay_color = cv2.merge((b, g, r))
    mask = cv2.medianBlur(a, 1)
    h, w, _ = overlay_color.shape
    roi = newFrame[y:y + h, x:x + w]

    img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))
    img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)
    newFrame[y:y + h, x:x + w] = cv2.add(img1_bg, img2_fg)

    return newFrame

def transparent_gif(targetImg, x, y, size=None):
    if size is not None:
        targetImg = cv2.resize(targetImg, size)

    newFrame = img.copy()
    b, g, r = cv2.split(targetImg)
    overlay_color = cv2.merge((b, g, r))
    h, w, _ = overlay_color.shape
    roi = newFrame[y:y + h, x:x + w]
    img2gray = cv2.cvtColor(overlay_color, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(img2gray, 0, 255, cv2.THRESH_BINARY)

    img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))
    img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)

    newFrame[y:y + h, x:x + w] = cv2.add(img1_bg, img2_fg)

    return newFrame

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
bk = 0
eb = 0
ex = 0
el = 0
gl = 0
bm = 0
powerful = 0
while True:
    count_hand = 0
    ret, img = video.read()
    img = cv2.flip(img, 1)
    rgbimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgbimg)
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            count_hand = count_hand + 1
            lmList = []
            for id, lm in enumerate(hand.landmark):
                h, w, c = img.shape
                coorx, coory = int(lm.x * w), int(lm.y * h)
                lmList.append([coorx, coory])
                # cv2.circle(img, (coorx, coory),6,(50,50,255), -1)
            #mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)
            position_data(lmList)
            palm = calculate_distance(wrist, index_mcp)
            distance_1 = calculate_distance(index_tip, midle_tip)
            distance_2 = calculate_distance(midle_mcp, midle_tip)
            distance_3 = calculate_distance(thumb_tip, pinky_tip)
            distance_4 = calculate_distance(midle_pip, midle_mcp)
            distance_5 = calculate_distance(thumb_tip, pinky_tip)
            distance_8 = calculate_distance(thumb_tip, ring_tip)
            distance = distance_1 + distance_2
            ratio = distance / palm
            ratio1 = distance_3 / palm
            ratio2 = distance_4 / palm
            ratio3 = distance_5 / palm
            print(ratio)
            if (ratio >= 1.45):
                centerx = (index_tip[0] + midle_tip[0] - 30)/2
                centery = (index_tip[1] + midle_tip[1] - 50)/2
                shield_size = 1
                diameter = round(distance_1 * shield_size * 1.5)
                x1 = round(centerx - (diameter / 2))
                y1 = round(centery - (diameter / 2))
                h, w, c = img.shape
                if x1 < 0:
                    x1 = 0
                elif x1 > w:
                    x1 = w
                if y1 < 0:
                    y1 = 0
                elif y1 > h:
                    y1 = h
                if x1 + diameter > w:
                    diameter = w - x1
                if y1 + diameter > h:
                    diameter = h - y1
                shield_size = diameter, diameter
                ang_vel = 3
                deg = deg + ang_vel
                if deg > 360:
                    deg = 0
                hei, wid, col = img_1.shape
                cen = (wid // 2, hei // 2)
                M1 = cv2.getRotationMatrix2D(cen, round(deg), 1.0)
                M2 = cv2.getRotationMatrix2D(cen, round(360 - deg), 1.0)
                rotated1 = cv2.warpAffine(img_1, M1, (wid, hei))
                rotated2 = cv2.warpAffine(img_2, M2, (wid, hei))
                if (diameter != 0):
                    img = transparent(rotated1, x1, y1, shield_size)
                    img = transparent(rotated2, x1, y1, shield_size)
                if(distance_1>=180):
                    img = transparent_gif(energyball[eb], x1, y1, shield_size)
                eb = (eb+1) % nums_eb
            if (distance_1 >= 230):
                    centerx = 1440/2
                    centery = 2561/2
                    shield_size = 2
                    diameter = round(1280 * shield_size)
                    x1 = round(centerx - (diameter / 2))
                    y1 = round(centery - (diameter / 2))
                    if x1 < 0:
                        x1 = 0
                    elif x1 > w:
                        x1 = w
                    if y1 < 0:
                        y1 = 0
                    elif y1 > h:
                        y1 = h
                    if x1 + diameter > w:
                        diameter = w - x1
                    if y1 + diameter > h:
                        diameter = h - y1
                        shield_size = diameter, diameter
                    if (diameter != 0):
                        img = transparent_gif(broken[bk], x1, y1, shield_size)
                    bk = (bk+1) % nums_broken

            if (ratio1 <= 0.15):
                if(powerful<=250):
                    powerful = powerful + 3
                    centerx = wrist[0]
                    centery = wrist[1]

                    centerx_2 = midle_mcp[0]
                    centery_2 = midle_mcp[1]

                    shield_size = 1

                    diameter = round(palm * shield_size*2.5)
                    x1 = round(centerx - (diameter / 2))
                    y1 = round(centery - (diameter / 2))

                    x2 = round(centerx_2 - (diameter / 2))
                    y2 = round(centery_2 - (diameter / 2))

                    if x1 < 0:
                        x1 = 0
                    elif x1 > w:
                        x1 = w
                    if y1 < 0:
                        y1 = 0
                    elif y1 > h:
                        y1 = h
                    if x1 + diameter > w:
                        diameter = w - x1
                    if y1 + diameter > h:
                        diameter = h - y1

                    if x2 < 0:
                        x2 = 0
                    elif x2 > w:
                        x2 = w
                    if y2 < 0:
                        y2 = 0
                    elif y2 > h:
                        y2 = h
                    if x2 + diameter > w:
                        diameter = w - x2
                    if y2 + diameter > h:
                        diameter = h - y2

                    shield_size = diameter, diameter
                    if (diameter != 0):
                        img = transparent_gif(power3[p3], x1, y1, shield_size)
                        img = transparent_gif(power4[p4], x2, y2, shield_size)
                        img = transparent_gif(power5[p5], x2, y2, shield_size)
                    p3 = (p3+1) % nums_power3
                    p4 = (p4+1) % nums_power4
                    p5 = (p5+1) % nums_power5
            if (ratio2 <= 0.27):
                if(powerful>0):
                    alpha = 0.4
                    centerx = 1440/2
                    centery = 2560/2
                    shield_size = 2
                    diameter = round(1280 * shield_size)
                    x1 = round(centerx - (diameter / 2))
                    y1 = round(centery - (diameter / 2))
                    if x1 < 0:
                        x1 = 0
                    elif x1 > w:
                        x1 = w
                    if y1 < 0:
                        y1 = 0
                    elif y1 > h:
                        y1 = h
                    if x1 + diameter > w:
                        diameter = w - x1
                    if y1 + diameter > h:
                        diameter = h - y1
                        shield_size = diameter, diameter
                        hei, wid, col = img_1.shape
                    if (diameter != 0):
                        if(powerful>0):
                            img = transparent_gif(elec[el], x1, y1, shield_size)
                            powerful = powerful - 1
                        el = (el+1) % nums_elec
            if (ratio3 >= 1.85):
                if (count_hand == 2):
                    alpha = 0.4
                    centerx = 1440/2
                    centery = 2560/2
                    shield_size = 2
                    diameter = round(1280 * shield_size)
                    x1 = round(centerx - (diameter / 2))
                    y1 = round(centery - (diameter / 2))
                    if x1 < 0:
                        x1 = 0
                    elif x1 > w:
                        x1 = w
                    if y1 < 0:
                        y1 = 0
                    elif y1 > h:
                        y1 = h
                    if x1 + diameter > w:
                        diameter = w - x1
                    if y1 + diameter > h:
                        diameter = h - y1
                        shield_size = diameter, diameter
                        hei, wid, col = img_1.shape
                    if (diameter != 0):
                        if(powerful>0):
                            img = transparent_gif(explode[ex], x1, y1, shield_size)
                            powerful = powerful - 1
                        ex = (ex+1) % nums_explode
                if(powerful>0):
                    powerful = powerful - 1
                    shield_size = 1
                    centerx = (wrist[0] + index_mcp[0])/2
                    centery = (wrist[1] + index_mcp[1])/2

                    centerx_2 = (thumb_mcp[0] + index_mcp[0]+400)/2
                    centery_2 = (thumb_mcp[1] + index_mcp[1]+200)/2

                    diameter = round(distance_5 * shield_size)
                    x1 = round(centerx - (diameter / 2))
                    y1 = round(centery - (diameter / 2))

                    x2 = round(centerx_2 - (diameter / 2))
                    y2 = round(centery_2 - (diameter / 2))

                    if x1 < 0:
                        x1 = 0
                    elif x1 > w:
                        x1 = w
                    if y1 < 0:
                        y1 = 0
                    elif y1 > h:
                        y1 = h
                    if x1 + diameter > w:
                        diameter = w - x1
                    if y1 + diameter > h:
                        diameter = h - y1

                    if x2 < 0:
                        x2 = 0
                    elif x2 > w:
                        x2 = w
                    if y2 < 0:
                        y2 = 0
                    elif y2 > h:
                        y2 = h
                    if x2 + diameter > w:
                        diameter = w - x2
                    if y2 + diameter > h:
                        diameter = h - y2
                    hei, wid, col = img_1.shape
                    shield_size = diameter, diameter
                    if (diameter != 0):
                        img = transparent_gif(globe[gl], x1, y1, shield_size)
                        img = transparent_gif(beam[bm], x2, y2, shield_size)
                    gl = (gl+1) % nums_globe
                    bm = (bm+1) % nums_beam
    # print(result)
    cv2.imshow("Video Result", img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()