import tensorflow as tf
import numpy as np

from tkinter import *
import os
from tkinter import filedialog
import cv2
import time
from matplotlib import pyplot as plt
from tkinter import messagebox




def endprogram():
	print ("\nProgram terminated!")
	sys.exit()






def file_sucess():
    global file_success_screen
    file_success_screen = Toplevel(training_screen)
    file_success_screen.title("File Upload Success")
    file_success_screen.geometry("150x100")
    file_success_screen.configure(bg='pink')
    Label(file_success_screen, text="File Upload Success").pack()
    Button(file_success_screen, text='''ok''', font=(
        'Verdana', 15), height="2", width="30").pack()


global ttype

def training():
    global training_screen

    global clicked

    training_screen = Toplevel(main_screen)
    training_screen.title("Training")
    # login_screen.geometry("400x300")
    training_screen.geometry("600x450+650+150")
    training_screen.minsize(120, 1)
    training_screen.maxsize(1604, 881)
    training_screen.resizable(1, 1)
    training_screen.configure()
    # login_screen.title("New Toplevel")



    Label(training_screen, text='''Upload Image ''', background="#d9d9d9", disabledforeground="#a3a3a3",
          foreground="#000000",  width="300", height="2", font=("Calibri", 16)).pack()
    Label(training_screen, text="").pack()


    options = [
        'Alpinia Galanga (Rasna)', 'Amaranthus Viridis (Arive-Dantu)', 'Artocarpus Heterophyllus (Jackfruit)', 'Azadirachta Indica (Neem)', 'Basella Alba (Basale)', 'Brassica Juncea (Indian Mustard)', 'Butterfly Pea', 'Carissa Carandas (Karanda)', 'Citrus Limon (Lemon)', 'Ficus Auriculata (Roxburgh fig)', 'Ficus Religiosa (Peepal Tree)', 'Hibiscus Rosa-sinensis', 'Jasminum (Jasmine)', 'Mangifera Indica (Mango)', 'Mentha (Mint)', 'Moringa Oleifera (Drumstick)', 'Muntingia Calabura (Jamaica Cherry-Gasagase)', 'Murraya Koenigii (Curry)', 'Nerium Oleander (Oleander)', 'Nyctanthes Arbor-tristis (Parijata)', 'Ocimum Tenuiflorum (Tulsi)', 'Piper Betle (Betel)', 'Plectranthus Amboinicus (Mexican Mint)', 'Pongamia Pinnata (Indian Beech)', 'Psidium Guajava (Guava)', 'Punica Granatum (Pomegranate)', 'Santalum Album (Sandalwood)', 'Syzygium Cumini (Jamun)', 'Syzygium Jambos (Rose Apple)', 'Tabernaemontana Divaricata (Crape Jasmine)'




    ]

    # datatype of menu text
    clicked = StringVar()


    # initial menu text
    clicked.set("Corn_(maize)_healthy")

    # Create Dropdown menu
    drop = OptionMenu(training_screen, clicked, *options )
    drop.config(width="30")

    drop.pack()

    ttype=clicked.get()

    Button(training_screen, text='''Upload Image''', font=(
        'Verdana', 15), height="2", width="30", command=imgtraining).pack()




def imgtraining():
    name1 = clicked.get()

    print(name1)

    import_file_path = filedialog.askopenfilename()
    import os
    s = import_file_path
    os.path.split(s)
    os.path.split(s)[1]
    splname = os.path.split(s)[1]


    image = cv2.imread(import_file_path)
    #filename = 'Test.jpg'
    filename = 'Data/'+name1+'/'+splname


    cv2.imwrite(filename, image)
    print("After saving image:")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Original image', image)
    cv2.imshow('Gray image', gray)
    # import_file_path = filedialog.askopenfilename()
    print(import_file_path)
    fnm = os.path.basename(import_file_path)
    print(os.path.basename(import_file_path))

    from PIL import Image, ImageOps

    im = Image.open(import_file_path)
    im_invert = ImageOps.invert(im)
    im_invert.save('lena_invert.jpg', quality=95)
    im = Image.open(import_file_path).convert('RGB')
    im_invert = ImageOps.invert(im)
    im_invert.save('tt.png')
    image2 = cv2.imread('tt.png')
    cv2.imshow("Invert", image2)

    """"-----------------------------------------------"""

    img = image

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original image', img)
    #cv2.imshow('Gray image', gray)
    #dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    dst = cv2.medianBlur(img, 7)
    cv2.imshow("Nosie Removal", dst)




def fulltraining():
    import model as mm








def testing():
    global testing_screen
    testing_screen = Toplevel(main_screen)
    testing_screen.title("Testing")
    # login_screen.geometry("400x300")
    testing_screen.geometry("600x450+650+150")
    testing_screen.minsize(120, 1)
    testing_screen.maxsize(1604, 881)
    testing_screen.resizable(1, 1)
    testing_screen.configure()
    # login_screen.title("New Toplevel")

    Label(testing_screen, text='''Upload Image''', disabledforeground="#a3a3a3",
          foreground="#000000", width="300", height="2",bg='pink', font=("Calibri", 16)).pack()
    Label(testing_screen, text="").pack()
    Label(testing_screen, text="").pack()
    Label(testing_screen, text="").pack()
    Button(testing_screen, text='''Upload Image''', font=(
        'Verdana', 15), height="2", width="30", command=imgtest).pack()


global affect
def imgtest():


    import_file_path = filedialog.askopenfilename()

    image = cv2.imread(import_file_path)
    print(import_file_path)
    filename = 'Output/Out/Test.jpg'
    cv2.imwrite(filename, image)
    print("After saving image:")
    #result()

    #import_file_path = filedialog.askopenfilename()
    print(import_file_path)
    fnm = os.path.basename(import_file_path)
    print(os.path.basename(import_file_path))

   # file_sucess()

    print("\n*********************\nImage : " + fnm + "\n*********************")
    img = cv2.imread(import_file_path)
    if img is None:
        print('no data')

    img1 = cv2.imread(import_file_path)
    print(img.shape)
    img = cv2.resize(img, ((int)(img.shape[1] / 5), (int)(img.shape[0] / 5)))
    original = img.copy()
    neworiginal = img.copy()
    cv2.imshow('original', img1)
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    img1S = cv2.resize(img1, (960, 540))

    cv2.imshow('Original image', img1S)
    grayS = cv2.resize(gray, (960, 540))
    cv2.imshow('Gray image', grayS)

    dst = cv2.fastNlMeansDenoisingColored(img1, None, 10, 10, 7, 21)
    cv2.imshow("Nosie Removal", dst)

    thresh = 127
    im_bw = cv2.threshold(grayS, thresh, 255, cv2.THRESH_BINARY)[1]
    #cv2.imshow("affect Removal", im_bw)
    number_of_black_pix = np.sum(im_bw == 0)
    #print(number_of_black_pix)
    #if(number_of_black_pix<5000):
        #affect =


    result()







def result():
    import warnings
    warnings.filterwarnings('ignore')

    import tensorflow as tf
    classifierLoad = tf.keras.models.load_model('leafmodel.h5')

    import numpy as np
    from keras.preprocessing import image

    base_dir = 'Data/'
    catgo = os.listdir(base_dir)

    test_image = image.load_img('Output/Out/Test.jpg', target_size=(200, 200))
    img1 = cv2.imread('Output/Out/Test.jpg')
    # test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifierLoad.predict(test_image)
    ind = np.argmax(result)

    print(catgo[ind])

    out = ''
    pre=''
    predicted_class = catgo[ind]

    if (predicted_class == "Alpinia Galanga (Rasna)"):
        messagebox.showinfo("Predict", predicted_class)

        messagebox.showinfo("Uses", 'Treating rheumatism and inflammatory disorders,Treating coughs and colds,Treating fever, muscle spasms, intestinal gas, and swelling,Killing bacteria,Stimulating the digestive power and appetite,Acting as a purgative,Relaxing smooth muscles,Loosening constricted tissues,Lowering pain, soreness, and inflammation in muscles,Removing toxins from the body ')

    elif (predicted_class == "Amaranthus Viridis (Arive-Dantu)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", ' Medicinal herb in traditional Ayurvedic medicine as antipyretic agents, also for the treatment of inflammation, ulcer, diabetic, asthma and hyperlipidemia.')


    elif (predicted_class == "Artocarpus Heterophyllus (Jackfruit)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Anticarcinogenic, antimicrobial, antifungal, anti-inflammatory, wound healing, and hypoglycemic effects.')

    elif (predicted_class == "Azadirachta Indica (Neem)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'neem leaves are used to treat dental and gastrointestinal disorders, malaria fevers, skin diseases, and as insects repellent, while the Balinese used neem leaves as a diuretic and for diabetes, headache, heartburn, and stimulating the appetite.')
    elif (predicted_class == "Basella Alba (Basale)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", ' improve testosterone levels in males, thus boosting libido. Decoction of the leaves is recommended as a safe laxative in pregnant women and children. Externally, the mucilaginous leaf is crushed and applied in urticaria, burns and scalds.')

    elif (predicted_class == "Brassica Juncea (Indian Mustard)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'extracted from the seeds of brown Indian mustard plant (Brassica juncea), is commonly used for cooking purposes and is rich in the content of special sulfur compounds called glucosinolates which has been reported to exhibit medicinal properties')

    elif (predicted_class == "Carissa Carandas (Karanda)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Medicine, Ayurvedic, to treat acidity, indigestion, fresh and infected wounds, skin diseases, urinary disorders and diabetic ulcer, as well as biliousness, stomach pain, constipation, anemia, skin conditions, anorexia and insanity.')
        messagebox.showinfo("Uses", 'Medicine, Ayurvedic, to treat acidity, indigestion, fresh and infected wounds, skin diseases, urinary disorders and diabetic ulcer, as well as biliousness, stomach pain, constipation, anemia, skin conditions, anorexia and insanity.')

    elif (predicted_class == "Citrus Limon (Lemon)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses",'Weight loss and reduce your risk of heart disease, anemia, kidney stones, digestive issues, and cancer')

    elif (predicted_class == "Ficus Auriculata (Roxburgh fig)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Stem bark juice is effective for diarrhea, cuts and wounds. Fruits are edible and can be made into jams and curries. Roasted figs are taken for diarrhea and dysentery. Root latex is used in mumps, cholera, diarrhea and vomiting.')


    elif (predicted_class == "Ficus Religiosa (Peepal Tree)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Antiulcer, antibacterial, antidiabetic, in the treatment of gonorrhea and skin diseases.')

    elif (predicted_class == "Hibiscus Rosa-sinensis"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Consumed in teas made from its flowers, leaves, and roots. In addition to casual consumption, Hibiscus is also used as an herbal medicine to treat hypertension, cholesterol production, and cancer progression.')

    elif (predicted_class == "Jasminum (Jasmine)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Jasmine is used to flavor beverages, frozen dairy desserts, candy, baked goods, gelatins, and puddings.')

    elif (predicted_class == "Mangifera Indica (Mango)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Invigorating and freshening. The juice is restorative tonic and used in heat stroke. The seeds are used in asthma and as an astringent. Fumes from the burning leaves are inhaled for relief from hiccups and affections of the throat.')

    elif (predicted_class == "Mentha (Mint)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'antimicrobial, carminative, stimulant, antispasmodic and for the treatment of various diseases such as headaches and digestive disorders ')

    elif (predicted_class == "Moringa Oleifera (Drumstick)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Treating edema,Protecting the liver,Preventing and treating cancer,Treating stomach upset,Fighting foodborne bacterial,infections,Preventing rheumatoid arthritis,Treating digestive problems,Controlling diabetes and high blood pressure,Fortifying bones,Improving skin health,Treating erectile dysfunction,Enhancing libido')

    elif (predicted_class == "Muntingia Calabura (Jamaica Cherry-Gasagase)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Anti-inflammatory activity,Antipyretic activity,Antiulcer activity,Anti-diabetic activity,Anti-hypertensive activity,Cardioprotective activity,Anti-bacterial activity,Insecticidal activity')

    elif (predicted_class == "Murraya Koenigii (Curry)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Treating piles, inflammation, itching, fresh cuts, bruises, and edema,Treating common body aches,Treating stomachaches,Acting as a carminative and analgesic ')

    elif (predicted_class == "Nerium Oleander (Oleander)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Treatment of diverse ailments such as heart failure, asthma, corns, cancer, diabetes, and epilepsy. Less well appreciated are the skin care benefits of extracts of N. oleander that include antibacterial, antiviral, immune, and even antitumor properties associated with topical use.')

    elif (predicted_class == "Nyctanthes Arbor-tristis (Parijata)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Treat a different kind of fevers, cough, arthritis, worm infestation, etc. The leaves juice is bitter and works as a tonic. The kadha or decoction is excellent for arthritis, constipation, worm infestation.')

    elif (predicted_class == "Ocimum Tenuiflorum (Tulsi)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Hand sanitizer, mouthwash and water purifier as well as in animal rearing, wound healing, the preservation of food stuffs and herbal raw materials and travelers health.')

    elif (predicted_class == "Piper Betle (Betel)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Prevents halitosis, improves vocalization, and strengthens gum, treat indigestion, constipation, congestion, coughs and asthma.')

    elif (predicted_class == "Plectranthus Amboinicus (Mexican Mint)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Treatment in folkloric medicines (syrup). It can also be used in other diseases such as flu, bronchitis, and epilepsy.')

    elif (predicted_class == "Pongamia Pinnata (Indian Beech)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Treatment of tumors, piles, skin diseases, and ulcers,The root is effective for treating gonorrhea, cleaning gums, teeth, and ulcers, and is used in vaginal and skin diseases ')

    elif (predicted_class == "Psidium Guajava (Guava)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Gastrointestinal infections such as diarrhea, dysentery, stomach aches, and indigestion[4] and it is used across the world for these ailments.')

    elif (predicted_class == "Punica Granatum (Pomegranate)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Preventing and treating cancer,Cardiovascular disease,Osteoarthritis and rheumatoid arthritis,Wound healing,The reproductive system,Dysentery, diarrhea, and intestinal parasites,Throat infections,Nose bleeds,Bronchitis,Sore throats, coughs, urinary infections, digestive disorders, and arthritis')

    elif (predicted_class == "Santalum Album (Sandalwood)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Antipyretic, antiseptic, antiscabetic, and diuretic properties.It is also effective in treatment of bronchitis, cystitis, dysuria, and diseases of the urinary tract [17]. The main ingredient of sandalwood oil is α-santalol that has many therapeutic properties.')

    elif (predicted_class == "Syzygium Cumini (Jamun)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'It has astringent, carminative, stomachic, diuretic, antidiabetic, anti-diarrheal, anti-inflammatory, radioprotective, gastroprotective, antioxidant, anti-allergic, anticancer, antibacterial, and cardioprotective effects, among other things.')

    elif (predicted_class == "Syzygium Jambos (Rose Apple)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'Rich in vitamin C, the fruit can be eaten raw or cooked in various regional recipes. In South-East Asian countries, rose apple fruit is frequently served with spiced sugar.')

    elif (predicted_class == "Tabernaemontana Divaricata (Crape Jasmine)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'The roots, leaves, and flowers are all used to treat snake and scorpion poisoning. Non-medical uses include using the wood as incense and perfume or using the pulp around the seed to make red dyes.')

    elif (predicted_class == "Tabernaemontana Divaricata (Crape Jasmine)"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'The roots, leaves, and flowers are all used to treat snake and scorpion poisoning. Non-medical uses include using the wood as incense and perfume or using the pulp around the seed to make red dyes.')

    elif (predicted_class == "Butterfly Pea"):
        messagebox.showinfo("Result", predicted_class)
        messagebox.showinfo("Uses", 'It is rich in antioxidants and may be linked to several health benefits, including increased weight loss, better blood sugar control, and improvements in hair and skin health. It also versatile and associated with very few side effects, so it a great potential addition to your diet.')








def main_account_screen():
    global main_screen
    main_screen = Tk()
    width = 600
    height = 600
    screen_width = main_screen.winfo_screenwidth()
    screen_height = main_screen.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    main_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    main_screen.resizable(0, 0)
    # main_screen.geometry("300x250")
    main_screen.configure()
    main_screen.title(" Herbal Leaf Image Classification")

    Label(text="HerbalProject", width="300", height="5", font=("Calibri", 16)).pack()

    Button(text="UploadImage", font=(
        'Verdana', 15), height="2", width="30", command=training, highlightcolor="black").pack(side=TOP)
    Label(text="").pack()
    Button(text="Training", font=(
        'Verdana', 15), height="2", width="30", command=fulltraining, highlightcolor="black").pack(side=TOP)

    Label(text="").pack()
    Button(text="Testing", font=(
        'Verdana', 15), height="2", width="30", command=testing).pack(side=TOP)

    Label(text="").pack()

    main_screen.mainloop()


main_account_screen()

