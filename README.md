# Anime-Recommender
End-to-End application that recommends new anime's based on your favorite anime.
---
Link to the site - https://animerecommendator.herokuapp.com/
## Description

Anime Recommender is an ent o end project that is deployed on heroku using a simple scraping api from https://cdn.animenewsnetwork.com and created a dataset from it.

The recommender system will use a cosine similarity metric to determine how similar two anime are and then create a count vectorizer matrix of all the animes. and save it into a pickle file to be used again.
        $$ Cos\theta =  \frac{\overrightarrow{a} . \overrightarrow{b}}{\| \overrightarrow{a}\| \|\overrightarrow{b} \|} =
        \frac{\displaystyle\sum_{i=1}^{n} a_ib_i}{\sqrt{\sum_{i=1}^{n} a_i^2} \sqrt{\sum_{i=1}^{n} a_i^2}} $$

### Executing program
To run this application you need to clone the repository and then afer installing all the dependencies from requirements.txt you can run the app.py file for run the FLASK server.
## License

This project is licensed under the MIT License - see the LICENSE.md file for details
