from PIL import Image

def pic_bolder(pic):
        min = pic[0]
        for pixel in pic:
                if pixel < min: min = pixel
        for num,pixel in enumerate(pic):
                if pixel < 255: pic[num] = pic[num]-min
        return pic

def load_image(path):
        pic = Image.open(path) #Загрузка
        return pic_bolder([int(y) for y in pic.tobytes()]) #Преобразование картинки в массив

def save_image(pic, path):
        pic = Image.frombytes('L', (30,30),bytes(pic)) #Преобразование массива в картинку
        pic.save(path) #Сохранение

