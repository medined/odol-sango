# odol-sango

Web Application To Track Twice Daily Blood Sugar Readings

[![wercker status](https://app.wercker.com/status/3090995c68882b60a1bfa44488517d20/s/master "wercker status")](https://app.wercker.com/project/byKey/3090995c68882b60a1bfa44488517d20)

## Database

### Postgres

```
docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres
```

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
