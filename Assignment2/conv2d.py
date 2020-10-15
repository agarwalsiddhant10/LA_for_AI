import numpy as np 
from PIL import Image, ImageOps

# img = Image.open('cat3.jpg').convert('LA').resize((600, 400))
# img.show()

def conv(A, B):
    m = A.shape[0]
    n = A.shape[1]
    p = B.shape[0]
    q = B.shape[1]
    C = np.zeros((m+p-1, n+q-1))

    for r in range(C.shape[0]):
        for s in range(C.shape[1]):
            # print(r,s)
            for i in range(p):
                for j in range(q):
                    k = r+1-i
                    l = s+1-j

                    if k >=0 and k < m and l >=0 and l < n :
                        C[r, s] += A[k, l]*B[i, j]

    return C


def get_image(image_path, gray_name):
    img = Image.open(image_path).resize((224, 224))
    img = ImageOps.grayscale(img)
    img.save(gray_name)
    return np.array(img)

def normalize_img(final_img):
    final_img = final_img/np.max(final_img)
    final_img *= 255
    final_img = final_img.astype(np.uint8)
    return final_img


def get_kernel(size = None, verbose = 0):
    if verbose == 0:
        kernel = np.ones((size, size))*(1/(size**2))

    if verbose == 1:
        kernel = np.ones((1, 2))
        kernel[0, 1] = -1
    
    if verbose == 2:
        kernel = np.ones((2, 1))
        kernel[1, 0] = -1

    print(kernel)
    return kernel


def main():
    initial_image = get_image('cat3.jpg', 'cat_gray.jpg')
    print(initial_image.shape)
    print(initial_image)
    kernel = get_kernel(verbose=1)
    conv_image = conv(initial_image, kernel)
    print(conv_image)
    output = Image.fromarray((conv_image+125).clip(0, 255).astype(np.uint8))
    output.save('cat_b.jpg')

if __name__=='__main__':
    main()
        
    
                        