import os
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from skimage.io import imread_collection
from skimage.transform import resize
from skimage import filters  # filters.sobel()
from tkinter import *

print('\nGLIOBLASTED\nv1.0B - by Aarav Dave')
print('\nTesting model... (est. wait time: 10s)')

malignant, benign = imread_collection(os.path.join('malignant', "*.jpeg")), imread_collection(os.path.join('benign', "*.jpeg"))
labels = [0] * len(malignant.files) + [1] * len(benign.files)

data = []
for image in malignant:
    new = resize(image, (100, 100), anti_aliasing=True)
    data.append(new.flatten())
for image in benign:
    new = resize(image, (100, 100), anti_aliasing=True)
    data.append(new.flatten())

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)
clf = svm.SVC(kernel='linear')
clf.fit(x_train, y_train)
prediction = clf.predict(x_test)
accuracy = accuracy_score(y_test, prediction)

print(f'''Accuracy: {round(accuracy * 100, 2)}%
{'-' * 10 if accuracy == 1 else 'Consider priming the model before usage.'}

Initiating software GUI...''')

window = Tk()
window.geometry('800x600')
window.title('Glioblasted')

# CODE OVER HERE

print('Software GUI initiated.\n\n----------\nLOG:')
window.mainloop()
print('''----------

Thank you for using Glioblasted.
Please star the repository: GITLINKHERE
If you use Glioblasted for academic research, please cite it.''')
quit()
