import pickle

favorite_color= {"lion":"yello","kitty":"red"}
pickle.dump(favorite_color, open("save.pkl","wb"))
favorite_color_load = pickle.load(open("save.pkl","rb"))
print(favorite_color_load)