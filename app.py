import streamlit as st
import pandas as pd
import pickle 
import requests

#function




def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=0f7fb165634558fa02a26f56b645efb1&language=en-US")
    data342= response.json()
    
    return "https://image.tmdb.org/t/p/w500/" +data342['poster_path']


def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommend_movies_posters =[]
    movie_ids =[]
    for i in movie_list:
        movie_id =movies_list.iloc[i[0]].movie_id
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommend_movies_posters.append(fetch_poster(movie_id))
        movie_ids.append(movie_id)
    return recommended_movies,recommend_movies_posters,movie_ids

data = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies_list = pd.DataFrame(data)

st.title('Movie Recommender System')

selected_movie = st.selectbox(
'Enter a Movie you recently Watched',
movies_list['title'].values)

if st.button('Recommend'):
    name,posters,ids = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        image = posters[0]
        
        

        # st.image(posters[0])
        
        st.markdown(f'''
        <a href="https://www.themoviedb.org/movie/{ids[0]}" target="_blank">
        <img class="immg" src="{posters[0]}""  />
        </a>
        ''',
        unsafe_allow_html=True
        )
        st.text(name[0])

    with col2:
        st.markdown(f'''
        <a href="https://www.themoviedb.org/movie/{ids[1]}" target="_blank">
        <img class="immg" src="{posters[1]}"  />
        </a>''',
        unsafe_allow_html=True)
        st.text(name[1])
        

    with col3:
        st.markdown(f'''
        <a href="https://www.themoviedb.org/movie/{ids[2]}" target="_blank">
        <img class="immg" src="{posters[2]}"  />
        </a>''',
        unsafe_allow_html=True)
        st.text(name[2])
        

    with col4:
        st.markdown(f'''
        <a href="https://www.themoviedb.org/movie/{ids[3]}" target="_blank">
        <img class="immg" src="{posters[3]}"  />
        </a>''',
        unsafe_allow_html=True)
        st.text(name[3])
        

    with col5:
        st.markdown(f'''
        <a href="https://www.themoviedb.org/movie/{ids[4]}">
        <img class="immg" src="{posters[4]}"  />
        </a>''',
        unsafe_allow_html=True)
        st.text(name[4])
        

        ##ignore

st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")

st.header("Made By : ")
st.markdown('''<link rel="stylesheet" href="https://github.com/scavenOP/css/blob/main/style.css">
        <div class="blog-card">
        <input type="radio" name="select" id="tap-1" checked>
        <input type="radio" name="select" id="tap-2">
        <input type="radio" name="select" id="tap-3">
        <input type="radio" name="select" id="tap-4">
        <input type="radio" name="select" id="tap-5">
        <input type="radio" name="select" id="tap-6">
        <input type="checkbox" id="imgTap">
        <div class="sliders">
           <label for="tap-1" class="tap tap-1"></label>
           <label for="tap-2" class="tap tap-2"></label>
           <label for="tap-3" class="tap tap-3"></label>
           <label for="tap-4" class="tap tap-4"></label>
           <label for="tap-5" class="tap tap-5"></label>
           <label for="tap-6" class="tap tap-6"></label>
        </div>
        <div class="inner-part">
           <label for="imgTap" class="img">
           <img class="img-1" src="https://media.discordapp.net/attachments/628100625900765204/878605760089702430/niladri.jpeg?width=556&height=527">
           </label>
           <div class="content content-1">             
              <div class="title">
                 Niladri Samanta
              </div>
           </div>
        </div>
        <div class="inner-part">
           <label for="imgTap" class="img">
           <img class="img-2" src="https://media.discordapp.net/attachments/628100625900765204/878605427208765470/arijit.jpeg?width=602&height=527">
           </label>
           <div class="content content-2">           
              <div class="title">
                 Arijit Majumdar
            </div>
        </div>
        <div class="inner-part">
            <label for="imgTap" class="img">
            <img class="img-3" src="https://media.discordapp.net/attachments/628100625900765204/878605751038398525/akash.jpeg?width=524&height=527">
            </label>
            <div class="content content-3">            
               <div class="title">
                  Akash Sarkar
             </div>
         </div>
         <div class="inner-part">
            <label for="imgTap" class="img">
            <img class="img-4" src="https://media.discordapp.net/attachments/628100625900765204/878605751768199168/ahan.jpeg">
            </label>
            <div class="content content-4">              
               <div class="title">
                  Ahan Das
             </div>
         </div>
         <div class="inner-part">
            <label for="imgTap" class="img">
            <img class="img-5" src="https://media.discordapp.net/attachments/628100625900765204/878605755752804393/ananya.jpeg?width=514&height=527">
            </label>
            <div class="content content-5">              
               <div class="title">
                  Ananya Das
             </div>
         </div>
         <div class="inner-part">
            <label for="imgTap" class="img">
            <img class="img-6" src="https://media.discordapp.net/attachments/628100625900765204/878605757556338738/deba.jpeg?width=497&height=527">
            </label>
            <div class="content content-6">           
               <div class="title">
                Debanjali Karmakar
             </div>
         </div>
     </div>
     <style>
     @import url("https://fonts.googleapis.com/css?family=Fira+Sans:400,500,600,700,800");
           *{
           margin: 0;
           padding: 0;
           box-sizing: border-box;
           }
           body{
           display: flex;
           align-items: center;
           justify-content: center;
           height: 100vh;
           font-family: 'Fira Sans', sans-serif;
           background: linear-gradient(147deg,#f6b323 0%, #f23b26 74%);
           }
           .blog-card{
           position: absolute;
           height: 200px;
           width: 90%;
           max-width: 850px;
           margin: auto;      
           border-radius: 25px;
           background: white;
           box-shadow: 0px 10px 50px rgba(252,56,56,.3);
           }
           .inner-part{
           position: absolute;
           display: flex;
           height: 200px;
           align-items: center;
           justify-content: center;
           padding: 0 13px;
           }
           #imgTap:checked ~ .inner-part {
           padding: 0;
           transition: .1s ease-in;
           }
           .inner-part .img{
           height: 150px;
           width: 150px;
           flex-shrink: 0;
           overflow: hidden;
           border-radius: 20px;
           box-shadow: 2px 3px 15px rgba(252,56,56,.1);          
           }
           #imgTap:checked ~ .inner-part .img{
           height: 370px;
           width: 850px;
           z-index: 99;
           margin-top: 10px;
           transition: .3s .2s ease-in;
           }
           .img img{
           height: 100%;
           width: 100%;
           object-fit: cover;
           cursor: pointer;
           opacity: 0;
           transition: .6s;
           }
           #tap-1:checked ~ .inner-part .img-1,
           #tap-2:checked ~ .inner-part .img-2,
           #tap-3:checked ~ .inner-part .img-3,
           #tap-4:checked ~ .inner-part .img-4,
           #tap-5:checked ~ .inner-part .img-5,
           #tap-6:checked ~ .inner-part .img-6{
           opacity: 1;
           transition-delay: .2s;
           }
           .content{
           padding: 0 20px 0 35px;
           width: 530px;
           margin-left: 50px;
           opacity: 0;
           transition: .6s;
           }
           #imgTap:checked ~ .inner-part .content{
           display: none;
           }
           #tap-1:checked ~ .inner-part .content-1,
           #tap-2:checked ~ .inner-part .content-2,
           #tap-3:checked ~ .inner-part .content-3,
           #tap-4:checked ~ .inner-part .content-4,
           #tap-5:checked ~ .inner-part .content-5,
           #tap-6:checked ~ .inner-part .content-6{
           opacity: 1;
           margin-left: 0px;
           z-index: 100;
           transition-delay: .3s;
           }
           .content span{
           display: block;
           color: #7b7992;
           margin-bottom: 15px;
           font-size: 22px;
           font-weight: 500
           }
           .content .title{
           font-size: 20px;
           font-weight: 700;
           color: #0d0925;
           margin-bottom: 20px;
           }
           .content .text{
           color: #4e4a67;
           font-size: 19px;
           margin-bottom: 30px;
           line-height: 1.5em;
           text-align: justify;
           }
           .content button{
           display: inline-flex;
           padding: 15px 20px;
           border: none;
           font-size: 16px;
           text-transform: uppercase;
           color: #fff0e6;
           font-weight: 600;
           letter-spacing: 1px;
           border-radius: 50px;
           cursor: pointer;
           outline: none;
           border: 1px solid #fd3535;
           background: linear-gradient(147deg, #fe8a39  0%, #fd3838 74%);
           }
           .content button:hover{
           background: linear-gradient(147deg, #fe791b 0%, #fd1c1c 74%);
           }
           .sliders{
           position: absolute;
           bottom: 25px;
           left: 65%;
           transform: translateX(-50%);
           z-index: 12;
           }
           #imgTap:checked ~ .sliders{
           display: none;
           }
           .sliders .tap{
           position: relative;
           height: 10px;
           width: 15px;
           background: #d9d9d9;
           border-radius: 5px;
           display: inline-flex;
           margin: 0 3px;
           cursor: pointer;
           }
           .sliders .tap:hover{
           background: #cccccc;
           }
           .sliders .tap:before{
           position: absolute;
           content: '';
           top: 0;
           left: 0;
           height: 100%;
           width: -100%;
           background: linear-gradient(147deg,#f6b323 0%, #f23b26 74%);
           border-radius: 10px;
           transform: scaleX(0);
           transition: transform .6s;
           transform-origin: left;
           }
           input[type="radio"],
           input[type="checkbox"]{
           display: none;
           }
           #tap-1:checked ~ .sliders .tap-1:before,
           #tap-2:checked ~ .sliders .tap-2:before,
           #tap-3:checked ~ .sliders .tap-3:before,
           #tap-4:checked ~ .sliders .tap-4:before,
           #tap-5:checked ~ .sliders .tap-5:before,
           #tap-6:checked ~ .sliders .tap-6:before{
           transform: scaleX(1);
           width: 100%;
           }
           @media (max-width:640px){
            .immg{
            width: 200px;
            height: 200px;
            }   
        }
           @media (max-width: 498px){          
            .inner-part .img{
           height: 77px;
           width: 77px;
           flex-shrink: 0;
           overflow: hidden;
           border-radius: 20px;
           box-shadow: 2px 3px 15px rgba(252,56,56,.1);          
           }
           .content{
           padding: 0 20px 0 15px;
           width: 530px;
           margin-left: 50px;
           opacity: 0;
           transition: .6s;
           }
           .sliders{
           position: absolute;
           bottom: 25px;
           left: 53%;
           transform: translateX(-50%);
           z-index: 12;
           }
           #imgTap:checked ~ .sliders{
           display: none;
           }
        }
        @media (max-width: 381px){ 
        .sliders{
        position: absolute;
        bottom: 10px;
        left: 42%;
        transform: translateX(-50%);
        z-index: 12;
        }
        #imgTap:checked ~ .sliders{
        display: none;
        }
        .content .title{
        font-size: 16px;
        font-weight: 700;
        color: #0d0925;
        margin-bottom: 20px;
        }
        }
        @media (min-width: 642px){ 
           .immg{
            width: 100px;
            height: 100px;
           }
            }             
     </style>
      ''',
    unsafe_allow_html=True)
  

