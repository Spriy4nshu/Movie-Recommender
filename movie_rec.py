from langcodes import*
import langcodes
import pandas as pd

language = input("Enter the language of the Movie: ")
cd = langcodes.find(language)
genre = input("Enter the genre Amoung the following: \n Action, Adult, Comedy, Horror, Adventure, Animation, Biography, \n Crime, Documentary, Drama, Family, Fantasy, History, Music, \n Mystery, Romance, Sci-Fi, Thriller, War, Western, Musical, Sport, \n Reality-TV, Film-Noir, News, Short, Talk-Show, Game-Show  \n Your input: ")

print(cd)
data = [{'Language' : cd, 'Genre' : genre}]
df = pd.DataFrame(data)

df.to_csv('user_data.csv')