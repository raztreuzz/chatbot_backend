import json
from pathlib import Path


class CourseService:
    def __init__(self):
        self.data_path = Path(__file__).resolve().parent.parent / "data" / "courses.json"
        with open(self.data_path, "r", encoding="utf-8") as file:
            self.courses = json.load(file)

    def normalize(self, course: str | None) -> str:
        if not course:
            return ""

        value = course.lower().strip()

        aliases = {
            "inteligencia artificial": "ia",
            "curso de ia": "ia",
            "ia": "ia",
            "analisis 2": "analisis 2",
            "análisis 2": "analisis 2",
            "a2": "analisis 2",
            "redes": "redes",
            "redes 1": "redes",
            "curso de redes": "redes"
        }

        return aliases.get(value, value)

    def save(self):
        with open(self.data_path, "w", encoding="utf-8") as file:
            json.dump(self.courses, file, ensure_ascii=False, indent=2)

    def get_schedule(self, course: str | None) -> str:
        key = self.normalize(course)
        data = self.courses.get(key)

        if not data:
            return "No tengo registrado el horario de ese curso."

        return f"{data['name']} se imparte: {data['schedule']}."

    def get_exam(self, course: str | None) -> str:
        key = self.normalize(course)
        data = self.courses.get(key)

        if not data:
            return "No tengo registrada la fecha de parcial de ese curso."

        return f"El parcial de {data['name']} está registrado para: {data['exam']}."

    def get_info(self, course: str | None) -> str:
        key = self.normalize(course)
        data = self.courses.get(key)

        if not data:
            return "No tengo información registrada de ese curso."

        topics = ", ".join(data["topics"])
        return f"{data['name']} incluye temas como: {topics}."

    def update_exam(self, course: str | None, date: str | None) -> str:
        key = self.normalize(course)
        data = self.courses.get(key)

        if not data:
            return "No encontré ese curso para actualizar el examen."

        if not date:
            return "Necesito una fecha para registrar el examen."

        data["exam"] = date
        self.save()

        return f"Listo, registré el examen de {data['name']} para {date}."