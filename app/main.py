from fastapi import FastAPI, Request
from app.services.course_service import CourseService

app = FastAPI()

course_service = CourseService()


@app.get("/")
def root():
    return {
        "status": "Zara webhook running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/webhook")
async def webhook(request: Request):
    body = await request.json()

    query_result = body.get("queryResult", {})
    intent = query_result.get("intent", {}).get("displayName", "")
    parameters = query_result.get("parameters", {})

    course = parameters.get("course")
    date = parameters.get("date")

    if intent == "ScheduleIntent":
        response = course_service.get_schedule(course)

    elif intent == "ExamsIntent":
        response = course_service.get_exam(course)

    elif intent == "CourseInfoIntent":
        response = course_service.get_info(course)

    elif intent == "UpdateExamIntent":
        response = course_service.update_exam(course, date)

    else:
        response = "Puedo ayudarte con horarios, parciales e información de cursos."

    return {
        "fulfillmentText": response
    }
