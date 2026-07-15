from fastapi import FastAPI
from google import genai
from pydantic import BaseModel,Field
app=FastAPI()

client=client=genai.Client(api_key="os.environ["GEMINI_API_KEY"]")
class resumerequest(BaseModel):
    skills:str=Field(min_length=10,max_length=80)

@app.post("/resume")
def resume(req:resumerequest):
    prompt=f"""
       You are a resume generator.
       Generate a resume with the following skills.
       skills: {req.skills}
       1.Career objective
       ....
       2.Technical Skills
       ....
       3.Projects
       ....
       4.Education
       ....
       5.Achievements
       ....
       6.Strengths
       ....
       7.Hobbies
       ....
       """
    response=client.models.generate_content(model="gemini-2.5-flash",contents=prompt)
    return {"skills":req.skills,"resume":response.text}
