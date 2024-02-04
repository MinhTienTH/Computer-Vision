import cv2
import imageio
from PIL import Image, ImageSequence
import urllib.request

# Đọc ảnh foreground
foreground_image = cv2.imread(r'Force_Ground.png')

# Đọc ảnh effect
effect_image = cv2.imread(r'effect.png')

# Đọc ảnh mask
mask_image = cv2.imread(r'Mask.png', cv2.IMREAD_UNCHANGED)

# Resize lại kích thước
foreground_resize = cv2.resize(foreground_image, (mask_image.shape[1], mask_image.shape[0]))
effect_resize = cv2.resize(effect_image, (mask_image.shape[1], mask_image.shape[0]))

#Sao chép ảnh qua biến mới
force_copy = foreground_image.copy()
alpha = 0.6
force_copy[mask_image[:,:,2] != 0] = foreground_image[mask_image[:,:,2] != 0] * alpha \
    + effect_resize[mask_image[:,:,2] != 0] * (1 - alpha)

#cv2.imshow('Force Copy', force_copy)
#cv2.imwrite("img_result.png", result)
cv2.waitKey(0)

# Đọc ảnh background chứa hiệu ứng động dạng GIF
url = "https://media0.giphy.com/media/2vmiW6mcYgKst3QVDK/giphy.gif"
frames = imageio.mimread(imageio.core.urlopen(url).read(), '.gif')

# Cắt ảnh background cho khớp kích thước với ảnh foreground
fg_h, fg_w, fg_c = foreground_image.shape
bg_h, bg_w, bg_c = frames[0].shape
top = int((bg_h-fg_h)/2)
left = int((bg_w-fg_w)/2)
bgs = [frame[top: top + fg_h, left:left + fg_w, 0:3] for frame in frames]

#print('Kích thước theo từng kênh của foreground: ', foreground_image.shape)
#print('Kích thước theo từng kênh của GIF: ', frames.shape)
#print('Kích thước theo từng kênh của mask: ', mask_resize.shape)

# Tạo ảnh alpha mask
mask_alpha = cv2.imread('Mask.png')
mask_alpha[mask_image[:,:,2]==0] = 0
mask_alpha[mask_image[:,:,2]!=0] = 255
#cv2.imshow("Alpha Image", mask_alpha)
#cv2.waitKey(0)

# Tạo ảnh alpha mờ
alpha_blur = cv2.GaussianBlur(mask_alpha, (51, 51), 0)
#cv2.imwrite('Alpha_blur.jpg', alpha_blur)
#cv2.imshow("Alpha_blur", alpha_blur)
#cv2.waitKey(0)
dst = force_copy * (alpha_blur/255)
#cv2.imshow("fg_remark", dst)
#cv2.waitKey(0)
# Xử lý pha trộn ảnh và hiệu ứng
results = []
alpha = 0.6
for i in range(len(bgs)):
    result = dst.copy()
    result[mask_image[:,:,3] != 0] = alpha * result[mask_image[:,:,3] != 0]
    bgs[i][mask_image[:,:,3] == 0] = 0
    bgs[i][mask_image[:,:,3] != 0] = (1-alpha)*bgs[i][mask_image[:,:,3] != 0]
    result = result + bgs[i]
    results.append(result)
imageio.mimsave('Total_Result.gif', results)