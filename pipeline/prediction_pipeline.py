from config.path_config import *
from utils.helpers import *

def hybrid_recommendation(user_id , user_weight=0.5, content_weight =0.5):

    ## User Recommndation

    similar_users =find_similar_users(user_id,
                                      USER_WEIGHTS_PATH,
                                      USER2USERENCODED,
                                      USER2USERDECODED)

    user_pref = get_user_preferences(user_id, 
                                     RATING_DF,
                                     ANIME_DF)
    # print(user_pref)
    user_recommended_animes = get_user_recommendations(similar_users,
                                                user_pref,
                                                ANIME_DF,
                                                SYNONPSIS_DF,
                                                RATING_DF)
    print(user_recommended_animes)
    

    user_recommended_anime_list = user_recommended_animes["anime_name"].tolist()
    print(user_recommended_anime_list)


    #### Content recommendation
    content_recommended_animes = []

    for anime in user_recommended_anime_list:
        similar_animes = find_similar_anime(anime,
                                            ANIME_WEIGHTS_PATH,
                                            ANIME2ANIMEENCODED,
                                            ANIME2ANIMEDECODED,
                                            ANIME_DF)

        if similar_animes is not None and not similar_animes.empty:
            content_recommended_animes.extend(similar_animes["name"].tolist())
        else:
            print(f"No similar anime found {anime}")
    
    combined_scores = {}

    for anime in user_recommended_anime_list:
        combined_scores[anime] = combined_scores.get(anime,0) + user_weight

    for anime in content_recommended_animes:
        combined_scores[anime] = combined_scores.get(anime,0) + content_weight  

    sorted_animes = sorted(combined_scores.items() , key=lambda x:x[1] , reverse=True)

    return [anime for anime , score in sorted_animes[:10]]