**Lerner Backend: Your Bridge to Knowledge**
This repository holds the backend engine of Lerner, your eLearning platform's nerve center. Here, robust algorithms and secure infrastructure work tirelessly to deliver a seamless and personalized learning experience.

**What powers Lerner's backend:**

Scalable architecture: Built to handle the demands of a growing user base and extensive learning content.
Secure data management: User information and learning progress are protected with industry-standard security measures.
Seamless API integration: Connects with external services to enrich the learning environment.

**For developers:**

Dive into the codebase to explore the technologies powering Lerner's backend intelligence.
Feel free to contribute with pull requests and suggestions to help shape the future of Lerner's engine.
Get ready to experience a learning platform fueled by cutting-edge technology and dedication to user success. The future of education is here!

**Technologies Used:**

* Django
* Django Rest Framework
* Django Channels
* Simple JWT
* Stripe
* Firebase Storage
* SQLite3/PostgreSQL
* Redis

**For cloning this repo locally:**

* git clone 'repo-link' ---> To clone the repo to your local machine
* pip install requirements.txt ---> To install the required package for the repo to run

* Change the channel layer in the settings.py file present in the project directory to the default channel layer code: (provided down)

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

* Set up the desired env files and all with your credentials
* Set up the local SMTP credentials in your account with your own email and password for otp verificaion
* Also set up the Stripe secret key in your settings file for having the stripe payment integration
* python manage.py runserver ---> To run the backend server on the local host.


This description emphasizes the technical prowess of the backend while keeping it accessible to a general audience. It highlights key features and encourages developer interaction. Feel free to customize it to further match your specific backend technologies and focus.
