# odol-sango

Web Application To Track Twice Daily Blood Sugar Readings

## Database

### Postgres

```
docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres
```
 pip install flask-sqlalchemy
## Package Installation

```
pip install -i requirements.txt
```

## Package Freeze

```
pip freeze > requirements.txt
```

## Python Configuration

```
echo "hamburger" > .gitignore
echo "__pycache__" >> .gitignore

python3 -m venv hamburger
source hamburger/bin/activate
```

## Name Derivation

* odol - blood in Basque
* sango - blood in Esperanto
