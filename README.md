<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kanishchugh/Anime-Recommender">
    <img src="static/logo/Anime Recommender-logos_transparent.png" alt="Logo" width="80" height="36.7">
  </a>

  <h3 align="center">Anime Recommender</h3>

  <p align="center">
    An End-to-End Anime reccomendation project!
    <br />
    <br />
    <a href="https://web-production-6205.up.railway.app/">View Demo</a>
    ·
    <a href="https://github.com/kanishchugh/Anime-Recommender/issues">Report Bug</a>
    ·
    <a href="https://github.com/kanishchugh/Anime-Recommender/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot](static/Screenshot%20.png)]()

Anime Recommender is an end-to-end project that is deployed on railway using a simple scraping api from https://cdn.animenewsnetwork.com and created a dataset from it.

The recommender system will use a cosine similarity metric after using a sentence transformer to tokenize the strings to determine how similar two anime are and then create a count vectorizer matrix of all the animes. and save it into a pickle file to be used again and again without having the need to calculate the data again and again. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section contains the list of the major frameworks/libraries used in this particular project. 

* [![Python][python.org]][python-url]
* [![Sklearn][scikit-learn.org]][sklearn-url]
* [![Flask][flask.palletsprojects.com]][flask-url]
* [![Numpy][numpy.org]][numpy-url]
* [![Pandas][pandas.org]][pandas-url]
* [![Tableau][tableau.com]][tableau-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To use this application you can visit the link https://anime-recommender-production.up.railway.app/ and use the application directly from there. 
_Try Naruto, AKIRA._ You can also explore the data using the tableau dashboard created byt clicking on the _OTAKU INVESTIGATION_ button in the top-bar.
To use the tableau dashboard. click on the type of media. Then select the genre of the media to get the filtered results in the grid. You may then hover over the tiles to get the information about the filtered media.


### Installation

_Below are instructions of how you can install/run this app._

1. Clone the repo
   ```sh
   git clone https://github.com/kanishchugh/Anime-Recommender.git
   ```
2. Install all requirements
   ```sh
   pip install -r requirements.txt
   ```
3.  Run `app.py`
   ```js
   python3 app.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Kanish Chugh - [@kanishchugh2001](https://twitter.com/kanishchugh2001) - kanishchugh2001@gmail.com

Project Link: [https://github.com/kanishchugh/Anime-Recommender/](https://github.com/kanishchugh/Anime-Recommender)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: static/Screenshot.png
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-000000?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com

[python.org]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://python.org

[scikit-learn.org]: https://img.shields.io/badge/scikitlearn-000000?style=for-the-badge&logo=scikitlearn&logoColor=white
[sklearn-url]: https://scikit-learn.org

[flask.palletsprojects.com]: https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white
[flask-url]: https://flask.palletsprojects.com

[numpy.org]: https://img.shields.io/badge/numpy-000000?style=for-the-badge&logo=numpy&logoColor=white
[numpy-url]: https://numpy.org/

[pandas.org]: https://img.shields.io/badge/pandas-000000?style=for-the-badge&logo=pandas&logoColor=white
[pandas-url]: https://pandas.pydata.org/

[tableau.com]: https://img.shields.io/badge/tableau-000000?style=for-the-badge&logo=tableau&logoColor=white
[tableau-url]: tableau.com/
