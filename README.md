# PostApi :grinning:
A REST API for a blog app. I built it with Flask and FlaskSQLAlchemy

## The End Points
- **GET** /posts (returns all posts)

- **GET** /posts/<int:id> (returns a post with a certain id)

- **POST** /posts (creates a new post)

- **PUT** /posts/<int:id> (updates a post with a certain id)

- **DELETE** /posts/<int:id> (deletes a post with a certain id)

## The Testing Environment 
- Postman

## The Dependencies
- Flask
- Flask-SQLAlchemy
- Python3

## To run the project
`pipenv shell`
`python3 app.py`
