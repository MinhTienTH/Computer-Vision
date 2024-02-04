import cv2

# Đọc ảnh foreground
foreground_image = cv2.imread(r'Force_Ground.png')

# Đọc ảnh effect
effect_image = cv2.imread(r'Effect.png')

# Đọc ảnh mask
mask_image = cv2.imread(r'Mask.png', cv2.IMREAD_UNCHANGED)

# Hiển thị kích thước
print('Kích thước theo từng kênh của foreground: ', foreground_image.shape)
print('Kích thước theo từng kênh của eff: ', effect_image.shape)
print('Kích thước theo từng kênh của mask: ', mask_image.shape)

# Hiện thị hai ảnh lên màn hình
#cv2.imshow('Foreground', foreground_image)
#cv2.imshow('Background', effect_image)
#cv2.imshow('Mask', mask_image)
#cv2.waitKey(0)

# Chuẩn hoá ảnh Force ground, mask, effect
eff_resize = cv2.resize(effect_image, (foreground_image.shape[1], foreground_image.shape[0]))
mask_resize = cv2.resize(mask_image, (foreground_image.shape[1], foreground_image.shape[0]))

#Sao chép ảnh qua biến mới
result = foreground_image.copy()
alpha = 0.6
result[mask_resize[:,:,2] != 0] = foreground_image[mask_resize[:,:,2] != 0] * alpha \
    + eff_resize[mask_resize[:,:,2] != 0] * (1 - alpha)

cv2.imshow('Result', result)
cv2.imwrite("img_result.png", result)
cv2.waitKey(0)


