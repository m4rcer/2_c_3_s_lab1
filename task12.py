signal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_frames(signal, size, overlap):
    newSize = int(size * overlap)

    framesCount = len(signal) // newSize

    for i in range(framesCount):
        yield signal[(i)*newSize:(i+1)*newSize]


for frame in get_frames(signal, size=6, overlap=0.5):
    print(frame)
