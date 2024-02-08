from fastapi import FastAPI
from pydantic import BaseModel
import random


class Facts(BaseModel):
    id: int
    fact: str


app = FastAPI()

facts_db = [Facts(id=0, fact="By age three, the child's brain is actually twice as active as an adult's."),
            Facts(id=1, fact="By 18 months, toddlers learn one new word every two waking hours."),
            Facts(id=2, fact="Newborns have 300 bones compared to 207 for an adult."),
            Facts(id=3, fact="Babies are born without kneecaps. Kneecap bones are grown between 2 and 6 years old."),
            Facts(id=4, fact="A child stops growing when they develop a common cold.")]


# @app.get("/")
# async def get_all():
#     return facts_db


@app.get("/fact")
async def get_fact():
    random_fact = random.choice(facts_db)
    return random_fact


@app.get("/fact/{id}")
async def get_by_id(id):
    return next((i for i in facts_db if i.id == int(id)), None)


@app.post("/")
async def add(new_fact: Facts):
    facts_db.append(new_fact)
    return facts_db
