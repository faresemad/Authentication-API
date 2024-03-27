# Authentication-API

[![Account: LinkedIn](https://img.shields.io/badge/Fares%20Emad-LinkedIn-0077b5)](https://www.linkedin.com/in/faresemad/)
[![Account: Facebook](https://img.shields.io/badge/Fares%20Emad-Facebook-3B5998)](https://www.facebook.com/faresemadx)
[![Account: Twitter](https://img.shields.io/badge/Fares%20Emad-Twitter-0084b4)](https://twitter.com/faresemadx)
[![Account: Instagram](https://img.shields.io/badge/Fares%20Emad-Instagram-966842)](https://www.instagram.com/faresemadx/)
[![Account: GitHub](https://img.shields.io/badge/Fares%20Emad-GitHub-2b3137)](https://www.github.com/faresemad/)

Welcome to the Authentication API project. This project is a simple API that allows users to register, login, logout, change password, reset password, change email, and verify email. The API is built with Django and Django Rest Framework.

The API is built with the following technologies:

- Django
- Django Rest Framework
- Django All Auth

The API is built with the following features:

- User Registration
- User Login
- User Logout
- User Account Activation
- User Password Change
- User Password Reset
- User Email Change
- User Email Change Verification

## Running the project

To run the project, follow the instructions below:

1. Clone the repository

```bash
git clone https://github.com/faresemad/Authentication-API.git
```

2. Change into the project directory

```bash
cd Authentication-API
```

3. Create a virtual environment

```bash
python3 -m venv venv
```

4. Activate the virtual environment

```bash
source venv/bin/activate
```

5. Install the project dependencies

```bash
pip install -r requirements/local.txt
```

6. Build the project

```bash
make build
```

7. Run the project

```bash
make up
```

8. Access the project on your browser

```bash
http://localhost:8000
```

## API Endpoints

you can access the API endpoints on your browser by visiting the following URL:

```bash
http://localhost:8000/api/docs/
```

## Social Endpoints

you can access the social endpoints on your browser by visiting the following URL:

- Google: `http://localhost:8000/api/auth/o/google-oauth2/?redirect_uri=http://localhost:8000/api/social-auth/complete/google-oauth2/`
   - Notes:
        - You need to set redirect URI in the Google Developer Console to `http://localhost:8000/api/social-auth/complete/google-oauth2/`
        - You need to set the following environment variables in the `.env` (this file must be in `.envs/` directory) file:
            - `SOCIAL_AUTH_GOOGLE_OAUTH2_KEY`
            - `SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET`
        - You need to set the following Settings in Djoser Settings:
            ```python
                DJOSER = {
                    # ...
                    "LOGIN_FIELD": "email",
                    "SOCIAL_AUTH_TOKEN_STRATEGY": "djoser.social.token.jwt.TokenStrategy",
                    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": [
                        "http://localhost:8000/api/social-auth/complete/google-oauth2/",
                    ],
                    # ...
                }
            ```
